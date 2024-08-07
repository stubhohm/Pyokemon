from ..Keys import leave, exit
from ..Function_Lib.General_Functions import get_confirmation, try_again
from .Creature import Creature
from .ActorBattleInfo import ActorBattleInfo
from .PlayerCombatInput import PlayerCombatInput
from .UI import ui
from ..Colors import black
from ..Constants import terminal_font_size

class PC():
    def __init__(self) -> None:
        self.stored_pokemon:list[Creature] = []
        self.page = 0
        self.page_max = 0

    def print_to_terminal(self, text:str):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)

    def update_page_max(self):
        pc_size = self.get_stored_count()
        self.page_max = int(pc_size / 10)

    def add_creatrue(self, stored_pokemon:Creature, index: int | None):
        if index:
            self.stored_pokemon.insert(index,stored_pokemon)
        else:
            self.stored_pokemon.append(stored_pokemon)
        self.update_page_max()

    def remove_creature(self, removed_pokemon:Creature):
        i = self.stored_pokemon.index(removed_pokemon)
        self.stored_pokemon.remove(removed_pokemon)
        self.update_page_max()
        return i

    def get_stored_count(self):
        number = len(self.stored_pokemon)
        return number

    def validate_range(self):
        lower = self.page * 10
        upper = lower + 10
        num_stored = self.get_stored_count()
        if upper > num_stored:
            upper = num_stored
        if lower > upper:
            lower = upper
        return lower, upper

    def get_pc_slice(self):
        lower, upper = self.validate_range()
        pc_slice = self.stored_pokemon[lower:upper]
        return pc_slice

    def print_pokemon(self):
        text = f'Current PC page: {self.page + 1}\n'
        self.print_to_terminal(text)
        print(text)
        lower, upper = self.validate_range()
        pc_slice = self.stored_pokemon[lower:upper]
        if len(pc_slice)== 0:
            print('There are no pokemon to show on this page.')
            return
        for i, pc_pokemon in enumerate(pc_slice):
            ten_multi = self.page * 10
            print(f'{ten_multi + i + 1}: {pc_pokemon.name}')
        
    def change_page(self, change:int):
        self.page += change
        if self.page > self.page_max:
            self.page = 0
        if self.page < 0:
            self.page = self.page_max
        self.pc_info.roster = self.get_pc_slice()

    def swap_from_pc(self):
        swapping = True
        end_swapping_text = 'Would you like to end swapping operations?'
        while swapping:
            self.pc_info.roster = self.get_pc_slice()
            taken_pokemon = self.combat_fx.pick_from_roster(self.pc_info, 'swap from the pc')
            if not taken_pokemon:
                print('That did not match anyone on this PC page.')
                if get_confirmation(end_swapping_text):
                    break
                else:
                    continue  
            stored_pokemon = self.combat_fx.pick_from_roster(self.pc_user, 'place in the pc')
            if not stored_pokemon:
                print('That did not match anyone on your roster.')
                if get_confirmation(end_swapping_text):
                    break
                else:
                    continue
            if get_confirmation(f'Take {taken_pokemon.name} and store {stored_pokemon.name}?'):
                i = self.pc_user.roster.index(stored_pokemon)
                self.pc_user.roster.remove(stored_pokemon)
                self.pc_user.roster.insert(i, taken_pokemon)
                i = self.remove_creature(taken_pokemon)
                self.add_creatrue(stored_pokemon, i)
                text = f'Stored {stored_pokemon.name} and took {taken_pokemon.name}'
                self.print_to_terminal(text)
                print(text)
            swapping = get_confirmation('Continue swapping?')
        text = 'Finished swapping operation.'
        self.print_to_terminal(text)
        print(text)

    def store_pokemon(self):
        storing = True
        while storing:
            stored_pokemon = self.combat_fx.pick_from_roster(self.pc_user, 'store')
            if not stored_pokemon and try_again():
                continue
            if get_confirmation(f'Store {stored_pokemon.name}?'):
                self.add_creatrue(stored_pokemon, None)
                self.pc_user.roster.remove(stored_pokemon)
                text = f'Stored {stored_pokemon.name} in the pc.'
                self.print_to_terminal(text)
                print(text)
                break
            elif try_again():
                continue
            break
        text = 'Finished storing operation.'
        self.print_to_terminal(text)
        print(text)

    def take_pokemon(self):
        selecting = True
        while selecting:
            self.pc_info.roster = self.get_pc_slice()
            taken_pokemon = self.combat_fx.pick_from_roster(self.pc_info, 'take')
            if not taken_pokemon:
                if try_again():
                    continue
                else:
                    break
            if get_confirmation(f'Take {taken_pokemon.name}?'):
                i = self.remove_creature(taken_pokemon)
                self.pc_user.roster.append(taken_pokemon)
                text = f'Took {taken_pokemon.name} from the pc.'
                self.print_to_terminal(text)
                print(text)
                break
            elif try_again():
                continue
            break
        text = 'Finished taking operation.'
        self.print_to_terminal(text)
        print(text)

    def determine_pc_action(self, response:str):
        if 'next' in response:
            if get_confirmation('Go to the next page?'):
                self.change_page(1)
        elif 'previous' in response:
            if get_confirmation('Go to the previous page?'):
                self.change_page(-1)
        elif 'swap' in response:
            if len(self.stored_pokemon) == 0:
                text = 'There a no pokemon to swap with.'
                self.print_to_terminal(text)
                print(text)
            elif get_confirmation('Select a Pokemon to take from the PC?'):
                self.swap_from_pc()
        elif 'store' in response:
            if len(self.pc_user.roster) == 1:
                text = 'You cannot store your only pokemon.'
                self.print_to_terminal(text)
                print(text)
            elif get_confirmation('Would you like to store a pokemon?'):
                self.store_pokemon()
        elif 'take' in response:
            if len(self.pc_user.roster) == 6:
                print('You have no space on your team right now.')
            elif len(self.pc_info.roster) == 0:
                text = 'You have no pokemon to take at this time.'
                self.print_to_terminal(text)
                print(text)
            elif get_confirmation('Would you like to take a pokemon?'):
                self.take_pokemon()
        return response

    def navigate_pc(self):
        text = '\nWould you like to the next or previous page, or would you like to swap, store or take a pokemon, or leave?: '
        response = input(text).strip().lower()
        return self.determine_pc_action(response)

    def init_active_pc(self, pc_user:ActorBattleInfo):
        self.pc_user = pc_user
        self.combat_fx = PlayerCombatInput()
        pc_list = self.get_pc_slice()
        self.pc_info = ActorBattleInfo()
        self.pc_info.define_battle_info(pc_list, None, None, None)

    def use_pc(self, pc_user:ActorBattleInfo):
        self.init_active_pc(pc_user)
        using_pc = True
        while using_pc:
            self.print_pokemon()
            response = self.navigate_pc()
            if response and leave in response:
                if get_confirmation('Would you like to leave the PC?'):
                    using_pc = False