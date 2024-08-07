from .Creature import Creature
from .Inventory import Inventory
from .UI import ui
from ..Keys import wild, npc, player
from ..Keys import hp
from ..Colors import black
from ..Constants import terminal_font_size

class ActorBattleInfo():
    def __init__(self) -> None:
        self.name:str
        self.roster:list[Creature]
        self.active:Creature
        self.inventory:Inventory
        self.actor_type:str
        self.target:list[Creature] = []
        self.action = None
        self.effect_speed:int = 0
        self.white_out = False

    def define_battle_info(self, roster:list[Creature], inventory:Inventory, actor_type:str, actor_name:str = ''):
        if actor_type == wild:
            self.name = 'Wild ' + roster[0].name.lower()
        else:
            self.name = actor_name
        self.roster = roster
        if len(roster) > 0:
            self.active = roster[0]
        else:
            self.active = None
        self.inventory = inventory
        self.actor_type = actor_type

    def print_to_terminal(self, text):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)

    def check_white_out(self):
        viable = 0
        for creature in self.roster:
            if creature.stats.active_value[hp] > 0:
                viable += 1
        if viable > 0:
            self.white_out = False
        else:
            self.white_out = True

    def add_pokemon_to_roster(self, target:Creature):
        self.roster.append(target)

    def check_for_struggle(self):
        for move in self.active.moves.move_list:
            if not move:
                continue
            if move.points > 0:
                return False
        return True
    
    def check_available_swap(self):
        viable_swaps:list[Creature] = []
        for creature in self.roster:
            if creature == self.active:
                continue
            if creature.stats.active_value[hp] > 0:
                continue
            viable_swaps.append(creature)
        if len(viable_swaps) > 0:
            return True
        else:
            return False
        
    def level_up_roster(self, total_exp:int, ):
        for pokemon in self.roster:
            start_level = pokemon.stats.leveling.level
            if pokemon == self.active:
                active = True
            else:
                active = False
            pokemon.stats.leveling.add_exp(total_exp, active)
            missing_hp = pokemon.stats.active_max[hp] - pokemon.stats.active_value[hp] 
            pokemon.stats.update_active_max_stats()
            pokemon.stats.active_value[hp] = pokemon.stats.active_max[hp] - missing_hp
            if pokemon.stats.stat_block:
                pokemon.stats.stat_block.update_info(pokemon)
            ui.display.active.update()
            if start_level != pokemon.stats.leveling.level:
                pokemon.moves.learn_via_levelup(start_level, pokemon.stats.leveling.level, pokemon.name)
                text = f'{pokemon.name} grew to {pokemon.stats.leveling.level}!'
                self.print_to_terminal(text)
