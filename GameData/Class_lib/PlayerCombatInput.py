from ..Keys import hp
from .ActorBattleInfo import ActorBattleInfo
from .Attack import Attack
from ..Function_Lib.General_Functions import get_terminal_confirmation, get_confirmation, try_again
from .Item import HealingItem, StatusItem, CaptureItem, Item
from ..Move_List.moves import mvstruggle
from .UI import ui
from ..Keys import fight, item, run, swap, cancel, select, combat_inputs
from ..Keys import up, down, left, right, directional_inputs
from ..Keys import moves, default
from ..Keys import description, quant
from ..Keys import t_all, t_ally, t_enemy, t_enemy_side, t_self, t_self_side
from ..Constants import terminal_font_size
from ..Colors import black

class PlayerCombatInput():
    def __init__(self) -> None:
        pass

    def print_to_terminal(self, text):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)
    '''
    def select_move(self, player:ActorBattleInfo):
        terminal = ui.display.active.battle_terminal
        active = player.active
        moves_list = active.moves.get_moves_list()
        terminal.define_list(moves_list, 2)
        while True:
            ui.display.active.update()
            input_value = ui.input.get_player_input()
            output = terminal.use_combat_terminal(input_value)
            if output == cancel:
                return output
            if not output:
                continue
            for move_item in player.active.moves.move_list:
                if not move_item:
                    continue
                if move_item == output:
                    selected_move = move_item
            return selected_move
    '''        
    def combat_fight(self, player:ActorBattleInfo):
        terminal = ui.display.active.battle_terminal
        moves_list = player.active.moves.get_moves_list()
        terminal.mode = moves
        terminal.define_list(moves_list, 2)
        selecting_move = True
        while selecting_move:
            if player.check_for_struggle():
                return mvstruggle()
            selected_move = player.active.moves.select_move()
            if not selected_move or selected_move == cancel:
                return cancel
            elif selected_move.points == 0:
                print('You cannot select a move with no remaining PP.')
            else:
                return selected_move
        return False
           
    def pick_from_roster(self, player:ActorBattleInfo, action_text):
        roster = player.roster
        roster_selection = ui.display.active.roster_selection
        index = roster_selection.selection_index
        roster_selection.set_parent_window(ui.display.active.window)
        roster_selection.make_display_blocks(roster)
        roster_selection.draw_display_blocks()
        text = f'Who would you like to {action_text}?'
        self.print_to_terminal(text)
        selecting = True
        while selecting:
            input_value = ui.input.get_player_input()
            if input_value:
                print('Roster selection')
                print(input_value)
                print(roster_selection.selection_index)
                print(len(roster))
            if input_value == up:
                index -= 1 
                print(index)
                index = index % len(roster)
                print(index)
            elif input_value == down:
                index += 1 
                print(index)
                index = index % len(roster)
                print(index)
            elif input_value == cancel:
                return cancel
            elif input_value == select:
                creature = roster[roster_selection.selection_index]
                print(creature.name)
                return creature
            roster_selection.selection_index = index
            roster_selection.draw_display_blocks()
        print('Here is the available roster:')
        for i, creature in enumerate(roster):
            print(f'Pokemon {i + 1}: {creature.name}')
        print('')
        
        choice = input(text).strip().lower()
        swap_target = None
        for i, creature in enumerate(roster):
            if creature.stats.active_value[hp] == 0:
                continue
            i_str = str(i + 1)
            lower_name = creature.name.lower()
            if choice == lower_name or choice == i_str:
                swap_target = creature
                return swap_target

    def combat_swap(self, player:ActorBattleInfo):
        ui.display.active.roster_selection.selection_index = 0
        active = player.active
        choosing_swap = True
        while choosing_swap:
            swap_target = self.pick_from_roster(player, 'make your active pokemon')
            if swap_target:
                print(swap_target)
            if not swap_target:
                continue
            elif swap_target == active:
                self.print_to_terminal('You cannot swap to your active pokemon.')
            elif swap_target == cancel:
                return cancel
            else:
                if not get_terminal_confirmation(f'Would you like to make {swap_target.name} your active pokemon?'):
                    continue
                return swap_target    
        return cancel

    def pick_item_from_list(self, player:ActorBattleInfo):
        inventory = player.inventory
        inventory.print_inventory_list()
        print('')
        text = 'Which item would you like to use?: '
        self.print_to_terminal(text)
        choice = input(text).strip().lower()
        item = inventory.search_for_matching_item_name(choice)
        if not item:
            return False
        else:
            return item

    def select_heal_or_status_removal_target(self, player:ActorBattleInfo, target_item:Item):
        target = self.pick_from_roster(player, f'use a {target_item.name} on')
        if not target:
            print('That did not match anyone on your roster.')
            if not try_again():
                return 'exit'
            else:
                return 'continue'
        if get_confirmation(f'Use {target_item.name} on {target.name}?'):
            return [target_item, target]
        else:
            return 'exit'

    def combat_item(self, player:ActorBattleInfo):
        choosing_item = True
        while choosing_item:
            target_item = self.pick_item_from_list(player)
            if not target_item:
                print('Your entry did not match any of your current items.')
            else:
                if get_confirmation(f'Would you like to use a {target_item.name}?'):
                    choosing_target = True
                    while choosing_target:
                        target = 'continue'
                        if type(target_item) == HealingItem or type(target_item) == StatusItem:
                            target = self.select_heal_or_status_removal_target(player, target_item)
                            if target == 'exit':
                                return False
                            if target == 'continue':
                                continue
                            return target
                        if type(target_item) == CaptureItem:
                            return [target_item, target]
            if not try_again():
                break
        return False    
            
    def combat_run(self):
        if get_terminal_confirmation('Are you sure you would like to run away?'):
            return run
        else:
            return cancel

    def check_combat_option(self, char:str, option:str, input_text:str):
        if char == option[0]:
            text = f'Would you like to {input_text}?'
            if not get_confirmation(text):
                return False
            else:
                return option

    def get_choice_action(self, choice, player):
        if choice == fight:
            action = self.combat_fight(player)
        elif choice == item:
            action = self.combat_item(player)
        elif choice == swap:
            action = self.combat_swap(player)
        elif choice == run:
            action = self.combat_run()
        else:
            action = choice
        print('getting choice')
        print(action)
        return action

    def get_player_action(self, player:ActorBattleInfo):
        terminal = ui.display.active.battle_terminal
        if player.active.stats.active_value[hp] == 0:
            new_active = self.combat_swap(player)
            return new_active
        if terminal.mode != moves:
            terminal.define_list(combat_inputs, 2)
        pending_response = True
        choice = ''
        while pending_response:
            action = None
            input_value = ui.input.get_player_input()
            choice = terminal.use_combat_terminal(input_value)
            if type(choice) == str:
                print(choice)
                action = self.get_choice_action(choice, player)
            if action == cancel:
                choice = cancel
                terminal.define_list(combat_inputs, 2)
            elif action:
                return action
            ui.display.active.update()
        pending_response = True
    
    def pick_enemy(self, npcs:list[ActorBattleInfo]):
        picking_target = True
        while picking_target:
            print(f'Potential Targets are: ')
            for npc in npcs:
                text = f"{npc.name}'s {npc.active.name}"
                print(text)
            response = input('Would you like to target the first one or the second one? (first/second) : ').strip().lower()
            if response[0] == 'f':
                print(f"You selected the first option: {npcs[0].name}'s {npcs[0].active.name}")
                if get_confirmation('Is this correct?'):
                    creature = npcs[0].active
                    return creature
            else:
                print(f"You selected the second option: {npcs[1].name}'s {npcs[1].active.name}")
                if get_confirmation('Is this correct?'):
                    creature = npcs[1].active
                    return creature
            print('Type in first or second to make your selection.')
        return None

    def get_target(self, move:Attack, npcs:list[ActorBattleInfo], player:ActorBattleInfo):
        creature_list = None
        if len(npcs) == 1:
            creature_list = [npcs[0].active]
        elif move.target in (t_enemy_side, t_all):
            creature_list = [npcs[0].active, npcs[1].active]
        elif move.target in (t_self, t_self_side):
            creature_list = [player.active]
        elif move.target == t_enemy:
            creature_list = [self.pick_enemy(npcs)]
        return creature_list
