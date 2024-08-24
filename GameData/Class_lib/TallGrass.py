from ..Keys import pokemon, level_range
from ..Constants import wild_encounters_on
from ..Function_Lib.General_Functions import random, rand100
from .Creature import Creature
from .Item import Item

class TallGrass():
    def __init__(self, name:str) -> None:
        self.name = name
        self.coordinates = []
        self.encounter_trigger_rate:int = 10
        self.make_blank_encounter_list()
        
    def make_blank_encounter_list(self):
        self.encounter_list:list = []

    def add_coordinates(self, dict:dict):
        self.coordinates = dict

    def add_pokemon(self, Creature_fx, lvl_range:list[int], encounter_chance:float):
        '''
        Takes an instance function, list with level ranges, and a list of two numbers between 0 and 100 for encounter chance.  
        '''
        pokemon_encounter = {pokemon: Creature_fx,
                     level_range: lvl_range}
        encounter = (pokemon_encounter, encounter_chance)
        self.encounter_list.append(encounter)

    def select_level(self, range:list[int]):
        '''
        Randomly picks a level within the given range.
        '''
        lower, upper = range[0], range[-1]
        if lower == upper:
            return lower
        else:
            return random.randrange(lower, upper)

    def set_encounter_rate(self, rate:int):
        '''
        Default of 10%, set between 0 and 100 for percent change to proc encounter.
        '''
        self.encounter_trigger_rate = rate

    def roll_wild_pokemon(self) -> dict:
        encounter_dicts, encounter_chance = zip(*self.encounter_list)
        total_chances = sum(encounter_chance)
        weights = [p / total_chances for p in encounter_chance]
        active_encounter:dict = random.choices(encounter_dicts, weights, k=1)[0]
        return active_encounter

    def generate_wild_encounter(self):
        '''
        Randomly picks a pokemon from encounter array
        '''
        active_encounter = self.roll_wild_pokemon()
        if not active_encounter:
            return
        level = self.select_level(active_encounter[level_range])
        creature = active_encounter[pokemon](level)
        if type(creature) == Creature:
            return creature

    def check_for_encounter(self):
        '''
        Checks to see if we trigger a random encounter. Returns None or an instanced wild pokemon if we do.
        '''
        rng = rand100()
        print(self.name)
        if not wild_encounters_on:
            print('wild encounters turned off')
            return None
        if rng <= self.encounter_trigger_rate:
            return self.generate_wild_encounter()
        else:
            return None
        