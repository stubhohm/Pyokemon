from .Creature import Creature
from .Inventory import Inventory
from .Attack import Attack
from ..Move_List.moves import mvstruggle
from ..Keys import t_ally, t_enemy, t_enemy_side, t_self, t_self_side
from ..Keys import hp
from ..Function_Lib.General_Functions import random, rand85_100, rand100, rand256
from ..Function_Lib.Combat_Fx import get_attack_typing_multiplier
from ..Move_List.moves import mvstruggle
from ..Function_Lib.Debug_Fxs import Debugging as db
from .ActorBattleInfo import ActorBattleInfo

class EnemyAI():
    def __init__(self) -> None:
        pass
    
    def select_self_buff_move(self,active:Creature)-> Attack:
        # if the move is self modifying and works on self
        # If our modifier is 0 or less use the move
        self_buff_move = None
        for move in active.moves.move_list:
            if not move:
                continue
            if move.points == 0:
                continue
            if not move.modifiying_stat:
                continue
            if not (move.target == t_self_side or move.target == t_self):
                continue
            if active.stats.modifiers[move.modifiying_stat] > 0:
                continue
            self_buff_move = move
            break
        return self_buff_move
    
    def select_enemy_debuff_move(self,active:Creature, player_active:Creature)-> Attack:
        # if the move is enemy modifying
        # If enemy modifier is 2 or greater the move
        enemy_debuff_move = None
        for move in active.moves.move_list:
            if not move:
                continue
            if move.points == 0:
                continue
            if not move.modifiying_stat:
                continue
            if not (move.target == t_enemy_side or move.target == t_enemy):
                continue
            if not player_active.stats.modifiers[move.modifiying_stat] < 2:
                continue
            enemy_debuff_move = move
            break
        return enemy_debuff_move

    def select_type_advantage(self, active:Creature, player_active:Creature)->Attack:
        best_damage = 0
        best_attack = None
        for move in active.moves.move_list:
            if not move:
                continue
            if move.points == 0:
                continue
            if move.base_power == 0:
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

    def get_npc_action(self, npc:ActorBattleInfo, player_active:Creature):
        remaining_hp = npc.active.stats.get_remaining_hp()
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
            if move and move.points > 0:
                break
            loop +=1
        if not move or move.points == 0:
            move = mvstruggle()
        return move