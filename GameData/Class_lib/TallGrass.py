from ..Keys import pokemon, level_range
from ..Constants import wild_encounters_on
from ..Function_Lib.General_Functions import random, rand100
from .Creature import Creature
from .Item import Item

class TallGrass():
    def __init__(self, name:str) -> None:
        self.name = name
        self.coordinates = []
        self.encounter_trigger_rate = 10
        self.make_blank_encounter_list()
        
    def make_blank_encounter_list(self):
        self.encounter_list:list = []

    def add_coordinates(self, array):
        self.coordinates = array

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
        return random.randrange(lower, upper)

    def generate_wild_encounter(self):
        '''
        Randomly picks a pokemon from encounter array
        '''
        if not wild_encounters_on:
            print('wild encounters turned off')
            return None
        encounter_dicts, encounter_chance = zip(*self.encounter_list)
        total_chances = sum(encounter_chance)
        weights = [p / total_chances for p in encounter_chance]
        active_encounter = random.choices(encounter_dicts, weights, k=1)[0]
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
        wild_pokemon = None
        if rng <= self.encounter_trigger_rate:
            wild_pokemon = self.generate_wild_encounter()
        return wild_pokemon