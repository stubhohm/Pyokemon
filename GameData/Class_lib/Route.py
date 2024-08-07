from ..Function_Lib.General_Functions import get_confirmation, try_again, rand100
from ..Keys import name, area_dictionary, area_class, route, wild, npc
from ..Keys import exit, leave
from ..Keys import directional_inputs, left, right, up, down, select, cancel
from ..Keys import no_weather
from ..Keys import navigation, battle
from ..Constants import screen_size, step_distance
from ..Colors import black
from ..Sprites.ImageImport import Sprite
from .TallGrass import TallGrass
from .Battle import Battle
from .Building import Building
from .ActorBattleInfo import ActorBattleInfo
from .Creature import Creature
from .Item import Item
from .Player import Player
from .LocalTrainers import LocalTrainers
from .UI import ui


class Route():
    def __init__(self, route_name:str) -> None:
        self.name = route_name
        self.type = route
        self.buildings:list[Building] = []
        self.tall_grass_zones:list[TallGrass] = []
        self.trainers:LocalTrainers = LocalTrainers()
        self.starting_position:list[tuple[int,int]] = (0,0)
        self.adjacent_areas:list = []
        self.switch_area = False
        self.weather = no_weather
        self.blocked_spaces = []
        self.ledges = []
        self.ledge_tops = []
        self.water_spaces = []
        self.transition_dict:dict = {}

    def set_sprite(self, sprite:Sprite):
        self.map = sprite

    def add_tall_grass(self, tall_grass:TallGrass):
        self.tall_grass_zones.append(tall_grass)
    
    def add_trainer(self, trainer:ActorBattleInfo):
        self.trainers.add_trainer(trainer)

    def add_adjacent_area(self, area_class_object):
        self.adjacent_areas.append(area_class_object)

    def define_area_transitions(self, transition_dict:dict):
        self.transition_dict = transition_dict

    def define_blocked_spaced(self, array:list[tuple[int,int]]):
        self.blocked_spaces = array

    def define_ledges(self, array:list[tuple[int,int]]):
        self.ledges = array

    def define_ledge_tops(self, array:list[tuple[int,int]]):
        self.ledge_tops = array

    def draw_map(self):
        if not self.map:
            print('no map')
            return
        ui.display.active.set_player_sprite(self.player.active_sprite)
        self.map.draw(ui.display.active.window)
        ui.display.active.update()

    def search_tall_grass(self):
        '''
        Checks tall grass coords to see if you are in one.
        Checks that grasses encounter table.
        '''
        coords = self.get_coordinate()
        encounter = None
        for tall_grass in self.tall_grass_zones:
            if coords in tall_grass.coordinates:
                encounter = tall_grass.check_for_encounter()
            if encounter:
                return encounter

    def select_new_area(self, starting_pos, key:str):
        '''
        Matches player leaving area to a new area.
        '''
        target_area = None
        for area in self.adjacent_areas:
            if area.name != key:
                continue
            else:
                target_area = area
                break
        if not target_area:
            return
        target_area.starting_position = starting_pos
        self.switch_area = True
        return target_area

    def check_area_departure(self, target_coords):
        for key in self.transition_dict.keys():
            value = self.transition_dict[key]
            if target_coords in value[0]:
                index = value[0].index(target_coords)
                return self.select_new_area(value[1][index], key)

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

    def determine_velocity(self, action:str):
        self.map.set_velocity(0,0)
        self.player.active_sprite.set_velocity(0,0)
        x, y = 0, 0
        if action == up:
            y = -1
        elif action == down:
            y = 1
        elif action == left:
            x = -1
        elif action == right:
            x = 1
        return x, y

    def reset_velocity(self):
        self.player.active_sprite.velocity.y = 0
        self.map.velocity.y = 0
        self.player.active_sprite.velocity.x = 0
        self.map.velocity.x = 0

    def handle_x_movement(self, x:int):
        screen_width = screen_size[0]
        half_step = step_distance / 2
        horizontal_pin = False
        self.reset_velocity()
        if x < 0:
            horizontal_pin = (self.map.pos.x == 0)
        else: 
            horizontal_pin = (self.map.pos.x <= self.map.horizontal_bound)
        player_off_center = not((screen_width / 2 - half_step) <= self.player.active_sprite.pos.x <= (screen_width / 2 + half_step))
        if horizontal_pin or player_off_center:
            self.player.active_sprite.set_velocity(x, 0)
        else:
            self.map.set_velocity(x, 0)

    def handle_y_movement(self, y:int):
        screen_height = screen_size[1]
        half_step = step_distance / 2
        vertical_pin = False
        self.reset_velocity()
        if y < 0:
            vertical_pin = (self.map.pos.y == 0)
        else: 
            vertical_pin = (self.map.pos.y <= self.map.vertical_bound)
        player_off_center = not((screen_height / 2 - half_step) <= self.player.active_sprite.pos.y <= (screen_height / 2 + half_step))
        if vertical_pin or player_off_center:
            self.player.active_sprite.set_velocity(0, y)
        else:
            self.map.set_velocity(0, y)

    def handle_movement(self, x:int, y:int):
        if x != 0:
            self.handle_x_movement(x)
        if y != 0:
            self.handle_y_movement(y)

        coords =  self.get_coordinate()
        target_coords = self.get_coordinate_plus_one(coords)
        target_coords_1 = self.get_coordinate_plus_one(target_coords)
        if target_coords in self.blocked_spaces:
            print('blocked')
            return
        if target_coords in self.water_spaces:
            if not self.player.is_surfing:
                return
        else:
            if self.player.is_surfing:
                self.player.is_surfing = False
                self.jump_ledge()
        
        if target_coords in self.ledges:
            if self.get_coordinate() not in self.ledge_tops:
                print('not at a ledgetop')
                return
            if target_coords_1 in self.blocked_spaces or target_coords_1 in self.ledges:
                print('target space is blocked')
                return
            else:
                self.jump_ledge()
        area = self.check_area_departure(target_coords)
        if area:
            return area
        self.map.move_image()
        self.player.active_sprite.move_image()

    def jump_ledge(self):
        self.map.velocity.y += self.map.velocity.y
        self.player.active_sprite.velocity.y += self.player.active_sprite.velocity.y
        self.map.velocity.x += self.map.velocity.x
        self.player.active_sprite.velocity.x += self.player.active_sprite.velocity.x

    def navigate_area(self):
        ui.display.active.window.fill(black)
        action = ui.input.get_player_input(True)    
        moving = self.map.moving or self.player.active_sprite.moving
        if moving:
            self.map.move_image()
            self.player.active_sprite.move_image()
            moving = self.map.moving or self.player.active_sprite.moving
            if not moving:
                return self.determine_encounter()
            return
        if self.player.battle_info.white_out:
            return leave
        if action == cancel:
            return exit
        x, y = self.determine_velocity(action)        
        if x != 0 or y != 0:
            action = self.handle_movement(x,y)
        return action

    def get_coordinate(self):
        map_x, map_y = abs(self.map.pos.x), abs(self.map.pos.y)
        player_x, player_y = abs(self.player.active_sprite.pos.x), abs(self.player.active_sprite.pos.y)
        x, y = int((map_x + player_x) / step_distance), int((map_y + player_y) / step_distance)
        return x, y

    def get_coordinate_plus_one(self, coordinate):
        x = self.map.velocity.x + self.player.active_sprite.velocity.x
        y = self.map.velocity.y + self.player.active_sprite.velocity.y
        target_coords = (coordinate[0] + x, coordinate[1]+ y)
        return target_coords


    def set_player_start_pos(self):
        self.map.pos.x, self.map.pos.y = 0, 0
        self.player.active_sprite.x, self.player.active_sprite.y = 0, 0
        starting_position = self.starting_position
        while not (self.get_coordinate()[0] == starting_position[0]):
            if (self.get_coordinate()[0] > starting_position[0]):
                mod = -1
            elif (self.get_coordinate()[0] < starting_position[0]):
                mod = 1
            else:
                mod = 0
            self.handle_x_movement(mod)
            self.map.jump_image()
            self.player.active_sprite.jump_image()
        print('finished x')
        while not (self.get_coordinate()[1] == starting_position[1]):
            if (self.get_coordinate()[1] > starting_position[1]):
                mod = -1
            elif (self.get_coordinate()[1] < starting_position[1]):
                mod = 1
            else:
                mod = 0
            self.handle_y_movement(mod)
            self.map.jump_image()
            self.player.active_sprite.jump_image()
        print('finished y')

    def battle_wild_pokemon(self, creature:Creature, player:Player):
        player.update_battle_info()
        wild_pokemon = ActorBattleInfo()
        wild_pokemon.define_battle_info([creature], None, wild, '')
        battle = Battle()
        battle.define_battle_start(player.battle_info, [wild_pokemon], no_weather)
        battle.battle_loop()
        ui.display.set_screen_state(navigation)
        ui.input.key_last = None

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
        if coords in self.blocked_spaces:
            print(f'{name} is in blocked.')
        if coords in self.ledges:
            print(f'{name} is in ledges.')
        if coords in self.ledge_tops:
            print(f'{name} is in ledge tops.')
        if coords in self.water_spaces:
            print(f'{name} is in water space.')
        
    def print_coordinates_lists(self):
        coord_names = ['Current Position', 'Target', 'Target + 1']
        coords =  self.get_coordinate()
        target_coords = self.get_coordinate_plus_one(coords)
        target_coords_1 = self.get_coordinate_plus_one(target_coords)
        coord_list = [coords, target_coords, target_coords_1]
        for i, name in enumerate(coord_names):
            self.print_coordinate_list(name, coord_list[i])


    def enter_area(self, player:Player):
        text = f'Entering {self.name}'
        print(text)
        self.player = player
        in_area = True
        self.constructed_array = []
        self.set_player_start_pos()
        while in_area:
            self.draw_map()
            action = self.navigate_area()
            if action == exit:
                return action
            if type(action) == Creature:
                self.battle_wild_pokemon(action, player)
            elif type(action) == ActorBattleInfo:
                self.trainers.engage_trainer(action, player)
            
            if action == 'm':
                self.add_to_array()
            if action == 'a':
                self.top_left = self.get_coordinate()
                print(self.top_left)
            if action == 's':
                self.bottom_right = self.get_coordinate()
                print(self.bottom_right)
            if action == 'c':
                self.constructed_array = [] 
            if action == 'p':
                print(self.constructed_array)
            if action == 't':
                self.print_coordinates_lists()

            elif action == 'item':
                self.player.use_an_item()
            if self.switch_area:
                self.switch_area = False
                return action

        