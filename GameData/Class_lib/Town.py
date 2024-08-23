from ..Keys import no_weather, exit, leave
from ..Keys import select, cancel, up, down, left, right
from ..Keys import navigation, wild
from ..Colors import black
from ..Constants import step_distance, screen_size
from ..Function_Lib.General_Functions import get_confirmation, try_again, rand100
from .ActorBattleInfo import ActorBattleInfo
from .Sprite import Sprite
from .Creature import Creature
from .Item import Item
from .Player import Player
from .Building import Building
from .Battle import Battle
from .TallGrass import TallGrass
from .NPC import NPC
from .Route import Route
from .Navigation import Navigation
from .ActorBattleInfo import ActorBattleInfo
from .LocalTrainers import LocalTrainers
from .UI import ui

class Town():
    def __init__(self, name:str) -> None:
        self.name = name
        self.player:Player = None
        self.buildings:list[Building] = []
        self.npcs:list[NPC] = []
        self.tall_grass_zones:list[TallGrass] = []
        self.trainers:LocalTrainers = LocalTrainers()
        self.navigation = Navigation()
        self.transition_dict = {}

    def set_sprite(self, sprite:Sprite):
        self.map = sprite

    def add_building(self, building:Building):
        self.buildings.append(building)

    def add_npc(self, npc:NPC):
        self.npcs.append(npc)

    def add_trainer(self, trainer:ActorBattleInfo):
        self.trainers.add_trainer(trainer)

    def add_tall_grass(self, tall_grass:TallGrass):
        self.tall_grass_zones.append(tall_grass)   

    def add_route(self, route:Route):
        self.navigation.adjacent_areas.append(route)

    def define_area_transitions(self, transition_dict:dict):
        self.navigation.transition_dict = transition_dict

    def define_blocked_spaced(self, array:list[tuple[int,int]]):
        self.navigation.blocked_spaces = array

    def define_ledges(self, array:list[tuple[int,int]]):
        self.navigation.ledges = array

    def define_ledge_tops(self, array:list[tuple[int,int]]):
        self.navigation.ledge_tops = array

    def define_water(self, dict:dict):
        self.navigation.water_spaces = dict

    def draw_map(self):
        if not self.map:
            print('no map')
            return
        ui.display.active.set_player_sprite(self.player.active_sprite)
        self.map.draw(ui.display.active.window)
        ui.display.active.update()

    def select_building(self, coordinate:tuple[int, int]):
        for i, building in enumerate(self.buildings):
            i_str = str(i+1)
            building_name = building.name.strip().lower()
            if coordinate == i_str or coordinate == building_name:
                text = f'Enter the {building.name}?'
                if get_confirmation(text):
                    return building
        return None

    def enter_a_building(self, coordinate):
        looking_for_building = True
        building = None
        while looking_for_building:
            building = self.select_building(coordinate)
            if not building:
                text = f'No match found at {coordinate}.'
                print(text)
                if not try_again():
                    looking_for_building = False
            else:
                building.enter_building(self.player)
                looking_for_building = False

    def talk_to_npc(self):
        pass

    def search_tall_grass(self):
        '''
        Checks tall grass coords to see if you are in one.
        Checks that grasses encounter table.
        '''
        coords = self.navigation.get_coordinate()
        encounter = None
        for tall_grass in self.tall_grass_zones:
            if coords in tall_grass.coordinates:
                encounter = tall_grass.check_for_encounter()
            if encounter:
                return encounter

    def battle_wild_pokemon(self, creature:Creature, player:Player):
        player.update_battle_info()
        wild_pokemon = ActorBattleInfo()
        wild_pokemon.define_battle_info([creature], None, wild, '')
        battle = Battle()
        battle.define_battle_start(player.battle_info, [wild_pokemon], no_weather)
        battle.battle_loop()
        ui.display.set_screen_state(navigation)
        ui.input.key_last = None

    def determine_encounter(self):
        '''
        Takes player position to see they enouncter a trainer or wild pokemon.'
        '''
        encounter = None
        #encounter = self.check_trainer_line_of_sight()
        if encounter:
            return encounter
        encounter = self.search_tall_grass()
        return encounter

    def add_to_array(self):
        print('adding')
        ui.input.get_player_input()
        if not self.top_left or not self.bottom_right:
            return
        bottom = self.top_left[1]
        top = self.bottom_right[1]
        left = self.top_left[0]
        right = self.bottom_right[0]
        print(right)
        print(left)
        print(bottom)
        print(top)
        for x in range(left, right + 1):
            for y in range(bottom, top + 1):
                coords = (x,y)
                if coords in self.constructed_array:
                    continue
                print(coords)
                self.constructed_array.append(coords)
        print('finished adding set')
        self.top_left = None
        self.bottom_right = None

    def print_coordinate_list(self, name, coords):
        if coords in self.navigation.blocked_spaces:
            print(f'{name} is in blocked.')
        if coords in self.navigation.ledges:
            print(f'{name} is in ledges.')
        if coords in self.navigation.ledge_tops:
            print(f'{name} is in ledge tops.')
        if coords in self.navigation.water_spaces:
            print(f'{name} is in water space.')
        
    def print_coordinates_lists(self):
        coord_names = ['Current Position', 'Target', 'Target + 1']
        coords =  self.navigation.get_coordinate()
        target_coords = self.navigation.get_coordinate_plus_one(coords)
        target_coords_1 = self.navigation.get_coordinate_plus_one(target_coords)
        coord_list = [coords, target_coords, target_coords_1]
        for i, name in enumerate(coord_names):
            self.print_coordinate_list(name, coord_list[i])

    def enter_area(self, player:Player):
        text = f'Entering {self.name}.'
        print(text)
        self.player = player
        self.navigation.define_navigation(self.player, self.map)
        in_area = True
        self.constructed_array = []
        self.navigation.set_player_start_pos()
        while in_area:
            self.draw_map()
            encounter = None
            action = self.navigation.navigate_area()
            if action in [exit, leave]:
                return action
            if action:
                encounter = self.determine_encounter()
            if type(encounter) == Creature:
                self.battle_wild_pokemon(encounter, player)
            elif type(encounter) == ActorBattleInfo:
                self.trainers.engage_trainer(encounter, player)
            

            key_input = None
            if key_input:
                print(key_input)
            if key_input == 'm':
                self.add_to_array()
            if key_input == 'a':
                self.top_left = self.navigation.get_coordinate()
                print(self.top_left)
            if key_input == 's':
                self.bottom_right = self.navigation.get_coordinate()
                print(self.bottom_right)
            if key_input == 'c':
                self.constructed_array = [] 
            if key_input == 'p':
                print(self.constructed_array)
            if key_input == 't':
                self.print_coordinates_lists()

            elif action == 'item':
                self.player.use_an_item()
            if self.navigation.switch_area:
                self.navigation.switch_area = False
                return action

    def get_action(self):
        action = self.navigation.navigate_area()
        if action in [exit, leave]:
            return action
        elif type(action) == Route:
            return action
        if action == select:
            self.add_to_array()
        if action == 'a':
            self.top_left = self.navigation.get_coordinate()
            print(self.top_left)
        if action == 's':
            self.bottom_right = self.navigation.get_coordinate()
            print(self.bottom_right)
        if action == 'c':
            self.constructed_array = [] 
        if action == 'p':
            print(self.constructed_array)
        if action == 'b':
            return exit
