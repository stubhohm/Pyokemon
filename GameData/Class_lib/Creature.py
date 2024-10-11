from ..Keys import hp, attack, sp_attack, defense, sp_defense, speed
from ..Colors import black
from ..Constants import terminal_font_size
from ..Function_Lib.General_Functions import get_sign, get_confirmation, get_terminal_confirmation
from .Stats import Stats
from .Moves import Moves
from .Status import Status
from .Item import Item
from .UI import ui
stats = [hp, attack, sp_attack, defense, sp_defense, speed]

class Creature():
    def __init__(self, name):
        self.name:str = name
        self.stats:Stats = Stats()
        self.moves:Moves = Moves()
        self.hold_item:Item = Item()
        self.owner:str = None
        self.original_owner_is_player:bool = False
        self.captured:bool = False
        self.custom_name:bool = False
        self.set_name(name)

    def set_name(self, name:str):
        self.name = name
        self.stats.name = name
    
    def start_battle(self):
        self.stats.start_battle()

    def end_battle(self):
        self.stats.end_battle()
        self.moves.end_battle()
        self.check_evolve()

    def print_to_terminal(self, text:str):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)

    def set_typing(self, primary, secondary):
        self.primary_type = primary
        self.secondary_type = secondary

    def set_attributes(self, hp, defense, sp_defense, attack, sp_attack, speed, primary_type, secondary_type):
        self.set_typing(primary_type, secondary_type)
        self.stats.set_stats(hp, defense, sp_defense, attack, sp_attack, speed)
        self.stats.set_typing(primary_type, secondary_type)

    def heal_at_pokecenter(self):
        self.stats.reset_modifers()
        self.stats.status.remove_status()
        self.moves.full_restore_pp()
        self.stats.set_hp(1000)
        self.stats.remove_special_situation()

    def set_catch_rate(self, value:int):
        self.catch_rate = value

    def set_attacks():
        pass

    def succeed_capture(self, player_name):
        self.owner = player_name
        self.original_owner_is_player = True
        return True

    def attempt_capture(self):
        pass

    def set_evolution(self, evolution: 'Creature'):
        text = f'{self.name} evolved into {evolution.name}!'
        self.print_to_terminal(text)
        if not self.custom_name:
            self.name = evolution.name
        self.stats = self.stats.evolve_stats(evolution)
        self.moves = self.moves.evolve_moves(evolution)

    def start_evolve(self):
        if not self.stats.leveling.evolution:
            return
        text = f'{self.name} is trying to evolve!'
        self.print_to_terminal(text)
        if not get_terminal_confirmation(f'Let {self.name} evolve?'):
            return
        evolution = self.stats.leveling.evolution(self.stats.leveling.level)
        self.set_evolution(evolution)

    def check_evolve(self):
        if self.stats.leveling.battle_start_level == self.stats.leveling.level:
            return self
        if self.stats.leveling.start_evolve <= self.stats.leveling.level:
            return self.start_evolve()

    def print_info(self):
        text = f'Name: {self.name}'
        print(text)
        for moves in self.moves.move_list:
            text = f'Move: name: {moves.name} pp: {moves.attributes.points}, element: {moves.attributes.element}'
            print(text)
        text = f'Ability {self.stats.ability.name}'
        print(text)
        text = f'Base Stats: {self.stats.base_stats}'
        print(text)



