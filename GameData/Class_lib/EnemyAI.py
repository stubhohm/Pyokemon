from .Creature import Creature
from .Inventory import Inventory
from .Attack import Attack
from ..Move_List.moves import mvstruggle
from ..Keys import t_ally, t_enemy, t_enemy_side, t_self, t_self_side
from ..Keys import status, taunted, tormented, imprisoned
from ..Keys import hp
from ..Function_Lib.General_Functions import random, rand85_100, rand100, rand256
from ..Function_Lib.Combat_Fx import get_attack_typing_multiplier
from ..Move_List.moves import mvstruggle
from ..Function_Lib.Debug_Fxs import Debugging as db
from .ActorBattleInfo import ActorBattleInfo

class EnemyAI():
    def __init__(self) -> None:
        pass

    def is_valid_move(self, move:Attack, active:Creature):
        if not move:
            return False
        if move.attributes.points == 0:
            return False
        if self.is_taunted and move.type == status:
            return False
        if self.is_tormented and active.stats.last_attack == move:
            return False
        if self.is_imprisoned and move in active.moves.move_list:
            return False
        return True

    def select_self_buff_move(self, active:Creature)-> Attack:
        # if the move is self modifying and works on self
        # If our modifier is 0 or less use the move
        self_buff_move = None
        for move in active.moves.move_list:
            if not self.is_valid_move(move):
                continue
            if not move.stat_attributes.modifiying_stat:
                continue
            if not (move.target == t_self_side or move.target == t_self):
                continue
            if active.stats.modifiers[move.stat_attributes.modifiying_stat] > 0:
                continue
            self_buff_move = move
            break
        return self_buff_move
    
    def select_enemy_debuff_move(self,active:Creature, player_active:Creature)-> Attack:
        # if the move is enemy modifying
        # If enemy modifier is 2 or greater the move
        enemy_debuff_move = None

        for move in active.moves.move_list:
            if not self.is_valid_move(move, active):
                continue
            if not move.modifiying_stat:
                continue
            if not (move.target == t_enemy_side or move.target == t_enemy):
                continue
            enemy_debuff_move = move
            break
        return enemy_debuff_move

    def select_type_advantage(self, active:Creature, player_active:Creature)->Attack:
        best_damage = 0
        best_attack = None
        for move in active.moves.move_list:
            if not self.is_valid_move(move, active):
                continue
            attack_multiplier = get_attack_typing_multiplier(move, player_active.stats)
            estimated_damage = attack_multiplier * move.base_power
            if estimated_damage > best_damage:
                best_attack = move
                best_damage = estimated_damage
        return best_attack
            
    def select_npc_move(self, actor_active:Creature, player_active:Creature) -> Attack:
        buff_move = self.select_self_buff_move(actor_active)
        debuff_move = self.select_enemy_debuff_move(actor_active, player_active)
        type_advantage_move = self.select_type_advantage(actor_active, player_active)
        possible_moves = [buff_move, debuff_move, type_advantage_move]
        viable_moves = []
        for move in possible_moves:
            if not move:
                continue
            appearances = possible_moves.count(move)
            if appearances > 1:
                viable_moves = [move]
                break
            else:
                viable_moves.append(move)
        count = len(viable_moves)
        if count == 0:
            move = mvstruggle()
        else:
            rand = random.randrange(0,count)
            move = viable_moves[rand]
        return None

    def select_next_creature(self, npc:ActorBattleInfo):
        for creature in npc.roster:
            if creature.stats.active_value[hp] != 0:
                return creature
        return None

    def set_torment_and_taunt(self, active:Creature):
        self.is_taunted = False
        self.is_tormented = False
        self.is_imprisoned = False
        for effect in active.stats.lingering_effects:
            if effect.name == taunted:
                self.is_taunted = True
            if effect.name == tormented:
                self.is_tormented = True
            if effect.name == imprisoned:
                self.is_imprisoned = True

    def get_npc_action(self, npc:ActorBattleInfo, player_active:Creature):
        remaining_hp = npc.active.stats.get_remaining_hp()
        self.set_torment_and_taunt(npc.active)
        if npc.check_for_struggle() and not npc.check_available_swap():
            move = mvstruggle()
        elif remaining_hp == 0:
            new_active_creature = self.select_next_creature(npc)
            return new_active_creature
        elif remaining_hp < 33 and npc.inventory.healing:
            item = npc.inventory.get_healing_item()
            return item
        else:
            move = self.select_npc_move(npc.active, player_active)
            return move

    def select_random_attack(self, active:Creature) -> Attack:
        if active.stats.active_value[hp] == 0:
            return None
        move_list = active.moves.move_list
        loop = 0
        move = None
        while loop < 100:
            rng = random.randrange(len(move_list))
            move = move_list[rng]
            if not move:
                continue
            if move and move.get_pp() > 0:
                break
            loop +=1
        if not move or move.get_pp() == 0:
            move = mvstruggle()
        return move