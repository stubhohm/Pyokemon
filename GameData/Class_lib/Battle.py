from ..Modules.External_Modules import pygame
from .Creature import Creature
from .Inventory import Inventory
from .Attack import Attack
from .AttackType import SpecialAttack, PhysicalAttack, StatusAttack
from .Item import Item, CaptureItem, HealingItem, StatusItem
from .ActorBattleInfo import ActorBattleInfo
from ..Move_List.moves import mvstruggle
from ..Function_Lib.Combat_Fx import get_defeated_creature_exp
from ..Keys import fight, item, run, swap, combat_inputs
from ..Keys import player, wild, npc, double_battle
from ..Keys import hp, defense, sp_defense, attack, sp_attack, speed
from ..Keys import t_all, t_ally, t_enemy, t_enemy_side, t_self, t_self_side, t_field
from ..Keys import typing_dict
from ..Keys import no_weather, battle, navigation
from ..Colors import black
from ..Constants import terminal_font_size
from ..Function_Lib.General_Functions import rand256, rand100, random
from ..Function_Lib.Debug_Fxs import Debugging
from .EnemyAI import EnemyAI
from .PlayerCombatInput import PlayerCombatInput
from .UI import ui

db = Debugging()

class Battle():
    def __init__(self):
        pass
    
    def define_battle_start(self, battle_info_player:ActorBattleInfo, npcs:list[ActorBattleInfo], weather:str):
        self.player = battle_info_player
        self.npcs = npcs
        self.enemy_ai = EnemyAI()
        self.player_input = PlayerCombatInput()
        self.define_npcs(npcs)
        self.define_combatants()
        self.set_weather(weather)
        self.start_battle()

    def new_active_entry(self, actor:ActorBattleInfo):
        active_ability = actor.active.stats.ability
        weather = active_ability.check_entry_weather(self.weather)
        self.set_weather(weather)
        active_ability.check_entry_self_stat(actor.active.stats)
        foes = []
        for combatant in self.combatants:
            if combatant.actor_type == actor.actor_type:
                continue
            foes.append(combatant)
        active_ability.check_entry_foe_stat(foes)
        actor.active.stats.stat_block.update_info(actor.active)

    def set_weather(self, weather:str):
        for combatant in self.combatants:
            negate = combatant.active.stats.ability.check_negate_weather(weather)
            if negate:
                self.weather = no_weather
                return
        self.weather = weather

    def define_npcs(self, npcs:list[ActorBattleInfo]): 
        if len(npcs) > 1:
            self.npc_a = npcs[0]
            self.npc_b = npcs[1]
            self.combat_type = double_battle
        else:
            self.npc_a = npcs[0]
            self.npc_b = None
            self.npcs = [npcs[0]]
            self.combat_type = self.npc_a.actor_type

    def define_combatants(self):
        self.combatants:list[ActorBattleInfo] = []
        for npc_actor in self.npcs:
            if not npc_actor:
                continue
            self.combatants.append(npc_actor)
        self.combatants.append(self.player)

    def print_to_terminal(self, text:str):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)

    def send_out_starting(self):
        for combatant in self.combatants:
            if combatant.actor_type == wild:
                text = f'You encounted a wild {combatant.active.name}!'
            elif combatant.actor_type == npc:
                text = f'{combatant.name} sent out {combatant.active.name}!'
            else:
                text = f'Go {combatant.active.name}!'
            self.print_to_terminal(text)
            self.new_active_entry(combatant)

    def get_action(self, actor:ActorBattleInfo, player_active:Creature):
        if actor.actor_type == player:
            action = self.player_input.get_player_action(actor)
        elif actor.actor_type == wild:
            action = self.enemy_ai.select_random_attack(actor.active)
        elif actor.actor_type == npc:
            action = self.enemy_ai.get_npc_action(actor, player_active)
            if not action:
                action = self.enemy_ai.select_random_attack(actor.active)
        return action

    def get_npc_actions(self):
        self.npc_a.action = self.get_action(self.npc_a, self.player.active)
        if len(self.npcs) > 1:
            self.npc_b.action = self.get_action(self.npc_b, self.player.active)
        else:
            self.npc_b = None

    def get_player_actions(self):
        self.player.action = self.player_input.get_player_action(self.player)

    def make_turn_order_groups(self, actors:list[ActorBattleInfo]):
        flee_order:list[ActorBattleInfo] = []
        swap_order:list[ActorBattleInfo] = []
        use_item_order:list[ActorBattleInfo] = []
        attack_order:list[ActorBattleInfo] = []
        for actor in actors:
            if not actor:
                continue
            action = actor.action
            actor_info:ActorBattleInfo = actor
            if type(action) in (PhysicalAttack, SpecialAttack, StatusAttack):
                actor.effective_speed = actor_info.active.stats.get_speed()
                attack_order.append(actor)
            # This is a swap:
            elif type(action) == Creature:
                swap_order.append(actor)
            # This is an attempt to flee
            elif type(action) == str:
                flee_order.append(actor)
            else:
                # This is an attempt to use an Item
                use_item_order.append(actor)
        return flee_order, swap_order, use_item_order, attack_order

    def attempt_flee(self):
        for npc_actor in self.npcs:
            if not npc_actor:
                continue
            ability = npc_actor.active.stats.ability
            if ability.check_prevent_fleeing(self.player.active.stats):
                return False
        if self.combat_type == wild:
            player_speed = self.player.active.stats.get_speed()
            wild_pokemon_speed = self.npc_a.active.stats.get_speed()
            if player_speed > wild_pokemon_speed:
                text = 'You successfully ran away!'
                self.print_to_terminal(text)
                return True
            else:
                text = 'You Failed to get away!'
                self.print_to_terminal(text)
                return False
        text = 'You cannot flee from a trainer battle!'
        self.print_to_terminal(text)
        return False

    def teleport(self, actor:ActorBattleInfo):
        for combatant in self.combatants:
            if combatant == actor:
                continue
            if combatant.active.stats.ability.check_prevent_fleeing(actor.active.stats):
                continue
            if self.combat_type == wild:
                if actor.actor_type == player:
                    text = 'You successfully ran away!'
                else:
                    text = f'{actor.name} escaped!'
                self.print_to_terminal(text)
                self.battling = False
            else:
                text = 'Teleport Failed!'
                self.print_to_terminal(text)
        
    def determine_attack_order(self, attack_group:list[ActorBattleInfo]):     
        sorted_attack_group = sorted(attack_group, key=lambda x: (x.action.get_priority(), x.effect_speed), reverse=True)
        return sorted_attack_group

    def check_pursuit(self, attack_group:list[ActorBattleInfo], actor:ActorBattleInfo):
        if len(attack_group) == 0:
            return False
        for attacker in attack_group:
            if attacker.target != actor.active:
                continue 
            if type(attacker.action) != PhysicalAttack:
                continue
            if attacker.action.name == 'Pursuit':
                attacker.action.base_power = attacker.action.base_power * 2
                attack_group.remove(attacker)
                return attacker

    def make_turn_order(self, flee_group:list[ActorBattleInfo], swap_group:list[ActorBattleInfo], item_group:list[ActorBattleInfo], attack_group:list[ActorBattleInfo]):
        turn_order:list[ActorBattleInfo] = []
        successful_flee = False
        if len(item_group) > 0:
            for actor in item_group:
                turn_order.append(actor)
        if len(flee_group) > 0:
            for actor in flee_group:
                successful_flee = self.attempt_flee()
                turn_order.append(actor)
        if len(swap_group) > 0:
            for actor in swap_group:
                pursuer = self.check_pursuit(attack_group, actor)
                if pursuer:
                    turn_order.append(pursuer)
                turn_order.append(actor)
        if len(attack_group) > 0:
            attack_order = self.determine_attack_order(attack_group)
            for entry in attack_order:
                turn_order.append(entry)
        return turn_order, successful_flee
        
    def determine_turn_order(self):
        if type(self.player.action) in (SpecialAttack, PhysicalAttack, StatusAttack, Attack): 
            self.player.target = self.player_input.get_target(self.player.action, self.npcs, self.player)
        turn_order = []
        actors = [self.player, self.npc_a, self.npc_b]
        flee_group, swap_group, item_group, attack_group = self.make_turn_order_groups(actors)
        turn_order, successful_flee = self.make_turn_order(flee_group, swap_group, item_group, attack_group)
        return turn_order, successful_flee

    def check_faint(self, actor:ActorBattleInfo):
        if actor.actor_type != player:
            if self.player.active.stats.active_value[hp] == 0:
                text = f'{self.player.active.name} has fianted!'
                self.print_to_terminal(text)
            return
        fainting = []
        for npc_actor in self.npcs:
            if npc_actor.active.stats.active_value[hp] == 0:
                tag = 'Wild'
                if npc_actor.actor_type == npc:
                    tag = 'Foe'
                text = f'{tag} {npc_actor.active.name} has fainted!'
                self.print_to_terminal(text)
                fainting.append(npc_actor)
        if len(fainting) > 0:
            total_exp = 0
            for fainted in fainting:
                exp = get_defeated_creature_exp(fainted, actor)
                actor.active.stats.gain_evs(fainted.active.stats.ev_yield_dict)
                total_exp += exp
            self.player.level_up_roster(total_exp)
            
    def resolve_swap(self, new_active:Creature, actor:ActorBattleInfo):
        new_statblock = None
        if actor.actor_type != player:
            if type(self.player.action) in (SpecialAttack, PhysicalAttack, StatusAttack):
                if actor.active in self.player.target:
                    actor.active.stats.end_battle()
                    self.player.target.remove(actor.active)
                    self.player.target.append(new_active)
        if actor.actor_type == player:
            for npc_actor in self.npcs:
                if type(npc_actor.action) in (SpecialAttack, PhysicalAttack, StatusAttack):
                    if not npc_actor.target:
                        continue
                    if actor.active in npc_actor.target:
                        actor.active.stats.end_battle()
                        npc_actor.target.remove(self.player.active)
                        npc_actor.target.append(new_active)
        if actor.actor_type == player:
            new_active.stats.stat_block = ui.display.active.player_stat_block
        else:
            for block in ui.display.active.npc_stat_blocks:
                if actor.active.stats.stat_block == block:
                    new_active.stats.stat_block = block 
        new_active.stats.stat_block.update_info(new_active)
        actor.active.stats.stat_block = None
        actor.active = new_active
        self.new_active_entry(actor)
        ui.display.active.update()

    def resolve_hit(self, action:Attack, target_actor:ActorBattleInfo):
        action.check_weather_change(self.combatants)
        new_active = action.check_forced_swap([target_actor], target_actor.active)
        for combatant in self.combatants:
            self.check_faint(combatant)
        if not new_active:
            return
        for combatant in self.combatants:
            if target_actor.target == combatant.active:
                self.resolve_swap(new_active, target_actor)
        
    def resolve_move(self, actor:ActorBattleInfo, action:Attack):
        active = actor.active
        # If the active fainted during the turn order, skip their action
        if active.stats.active_value[hp] == 0:
            return
        # Display the move being used by the actor and their name
        if actor.actor_type == wild:
            if actor.active.captured:
                return
            text = f'Wild {actor.active.name} used {action.name}!'
        elif actor.actor_type == npc:
            text = f'Foe {actor.active.name} used {action.name}!'
        else:
            text = f'{actor.active.name} used {action.name}!'
        print(text)
        self.print_to_terminal(text)
        
        # If the move targets self submit self stats to the move funtion
        if action.get_target() in (t_self, t_self_side):
            self_stats = actor.active.stats
            hit = action.use_move(self_stats, self_stats, self.weather)
            if not hit:
                return
            self.resolve_hit(action, actor)
        
        # If the target not self and not an arena move
        if action.get_target() in (t_enemy, t_enemy_side, t_all, t_ally):
            # if the actor is an NPC
            if actor.actor_type != player:
                hit = action.use_move(self.player.active.stats, actor.active.stats, self.weather)
                if not hit:
                    return
                self.resolve_hit(action, self.player)
            # Otherwise check the targets in the players target list
            # hit them and check each for a faint
            elif actor.actor_type == player:
                target_actor:ActorBattleInfo
                for npc_actor in self.npcs:
                    if npc_actor.active not in actor.target:
                        continue
                    target_actor = npc_actor
                for target in actor.target:
                    if not target:
                        continue
                    if action.name == 'Mirror Move':
                        action = target.stats.last_attack
                    if not action:
                        text = 'Mirror Move failed!'
                        self.print_to_terminal(text)
                        hit = False
                    else:
                        hit = action.use_move(target.stats, actor.active.stats, self.weather)
                    if not hit:
                        return
                    self.resolve_hit(action, target_actor)
            if hit and action.flee:
                self.teleport(actor)

    def resolve_combat_turn(self, turn_order:list[ActorBattleInfo]):
        for actor in turn_order:
            if not self.battling:
                continue
            action = actor.action
            # Only fleeing will be of type string
            if type(action) == str:
                continue
            # Swapping just makes the active the selected mon
            elif type(action) == Creature:
                text = f'{actor.active.name}, return!'
                self.print_to_terminal(text)
                self.resolve_swap(action, actor)
                text = f'Go {actor.active.name}!'
                self.print_to_terminal(text)
                continue
            # Function will select targets then apply attack to all targets
            elif type(action) in (SpecialAttack, PhysicalAttack, StatusAttack):
                self.resolve_move(actor, action)
                continue
            # User selected item on selected pokemon
            else:
                item:Item = action[0]
                if type(item) == CaptureItem:
                    if self.npc_a.actor_type == wild:
                        target = self.npc_a.active
                        item.set_player(self.player)
                        item.use_item(target)
                    else:
                        text = 'You cannot capture another trainers pokemon.'
                        self.print_to_terminal(text)
                else:
                    target = action[1]
                    item.use_item(target)
                actor.inventory.update_inventory()

    def check_for_team_wipe(self):
        # If the player wipes, end the battle
        self.player.check_white_out()
        if self.player.white_out:
            text = 'You whited out!'
            self.print_to_terminal(text)
            return False
        
        # If either enemy has not wiped, continue
        continue_battle = False
        for npc_actor in self.npcs:
            npc_actor.check_white_out()
            if not npc_actor.white_out:
                continue_battle = True
        return continue_battle

    def check_for_status_ailments(self):
        dmg_mod = self.player.active.stats.status.check_status_dmg()
        if dmg_mod:
            dmg = int(self.player.active.stats.active_max[hp] * dmg_mod)
            self.player.active.stats.change_hp(-dmg)
            text = f'{self.player.active.name} took {dmg} damage from being {self.player.active.stats.status.name}.'
            self.print_to_terminal(text)
        for npc_actor in self.npcs:
            if npc_actor.active.stats.active_value[hp] == 0:
                continue
            dmg_mod = npc_actor.active.stats.status.check_status_dmg()
            if dmg_mod:
                dmg = int(npc_actor.active.stats.active_max[hp] * dmg_mod)
                npc_actor.active.stats.change_hp(-dmg)
                text = f'{npc_actor.active.name} took {dmg} damage from being {npc_actor.active.stats.status.name}.'
                self.print_to_terminal(text)
                self.check_faint(self.player)

    def check_for_weather_boosts(self):
        for combatant in self.combatants:
            active_stats = combatant.active.stats
            active_ability = active_stats.ability
            active_ability.check_weather_boost(active_stats, self.weather)

    def update_stat_block(self, active:Creature, stat_block):
        stat_block.update_info(active)

    def clear_protection(self):
        print('')
        for combatant in self.combatants:
            combatant.active.stats.protected = False
        
    def end_battle(self):
        roster = self.player.roster
        for pokemon in roster:
            pokemon.end_battle()

    def start_battle(self):
        ui.display.set_screen_state(battle)
        ui.display.active.init_battle_screen((255,255,255), len(self.npcs))
        ui.display.active.player_stat_block.define(self.player.active)
        ui.display.active.battle_terminal.set_active_name(self.player.active.name)
        self.player.active.stats.stat_block = ui.display.active.player_stat_block
        for i, npc_actor in enumerate(self.npcs):
            if not npc_actor:
                continue
            ui.display.active.npc_stat_blocks[i].define(npc_actor.active)
            npc_actor.active.stats.stat_block = ui.display.active.npc_stat_blocks[i]
        for combatant in self.combatants:
            if not combatant:
                continue
            for pokemon in combatant.roster:
                pokemon.start_battle()
        ui.display.active.battle_terminal.define_list(combat_inputs, 2)
        ui.display.active.update()

    def battle_loop(self):
        self.battling = True
        self.send_out_starting()
        while self.battling:
            self.get_player_actions()
            if not self.player.action:
                continue 
            else:  
                self.get_npc_actions()
                if not self.npc_a.action:
                    battling = False
                    continue
                ui.display.active.update()
                turn_order, successful_flee  = self.determine_turn_order()
                if successful_flee:
                    self.battling = False
                    continue
                self.resolve_combat_turn(turn_order)
                self.check_for_status_ailments()
                self.battling = self.check_for_team_wipe()
                self.check_for_weather_boosts()
                self.clear_protection()
                if self.npc_a.active.captured:
                    self.battling = False
                ui.display.active.update()
        if not self.player.white_out and not self.npc_a.active.captured and not successful_flee:
            text = 'Congratulations, you beat the foe!'
            self.print_to_terminal(text)
        self.end_battle()
                