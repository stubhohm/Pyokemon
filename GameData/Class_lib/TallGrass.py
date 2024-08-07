from ..Keys import pokemon, level_range, rng_range
from ..Function_Lib.General_Functions import random, rand100
from .Creature import Creature
from .Item import Item

class TallGrass():
    def __init__(self, name:str) -> None:
        self.name = name
        self.coordinates = []
        self.make_blank_encounter_list()
        
    def make_blank_encounter_list(self):
        self.encounter_list:list = []
        for i in range(0,100):
            self.encounter_list.append(None)

    def add_coordinates(self, array):
        self.coordinates = array

    def add_pokemon(self, Creature_fx, lvl_range:list[int], rng_ranges:list[int]):
        '''
        Takes an instance function, list with level ranges, and a list of two numbers between 0 and 100 for encounter chance.  
        '''
        lower, upper = rng_ranges[0], rng_ranges[-1]
        encounter = {pokemon: Creature_fx,
                     level_range: lvl_range}
        for i in range(lower, upper):
            self.encounter_list[i] = encounter

    def select_level(self, range:list[int]):
        '''
        Randomly picks a level within the given range.
        '''
        lower, upper = range[0], range[-1]
        return random.randrange(lower, upper)

    def generate_wild_encounter(self):
        '''
        Randomly picks a pokemon from encounter array
        '''
        rng = rand100()
        active_encounter = self.encounter_list[rng]
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
        print(rng)
        if rng < 0:
            wild_pokemon = self.generate_wild_encounter()
        return wild_pokemon