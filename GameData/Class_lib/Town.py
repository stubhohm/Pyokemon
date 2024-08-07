from ..Keys import no_weather, exit, leave
from ..Keys import select, cancel, up, down, left, right
from ..Colors import black
from ..Constants import step_distance, screen_size
from ..Function_Lib.General_Functions import get_confirmation, try_again, rand100
from .ActorBattleInfo import ActorBattleInfo
from ..Sprites.ImageImport import Sprite
from .Creature import Creature
from .Item import Item
from .Player import Player
from .Building import Building
from .Battle import Battle
from .NPC import NPC
from .Route import Route
from .ActorBattleInfo import ActorBattleInfo
from .LocalTrainers import LocalTrainers
from .UI import ui

class Town():
    def __init__(self, name:str) -> None:
        self.name = name
        self.player:Player = None
        self.buildings:list[Building] = []
        self.npcs:list[NPC] = []
        self.trainers:LocalTrainers = LocalTrainers()
        self.adjacent_areas:list[Route] = []
        self.blocked_spaces = []
        self.transition_dict = {}
        self.ledges = []
        self.starting_position = (0,0)

    def set_sprite(self, sprite:Sprite):
        self.map = sprite

    def add_building(self, building:Building):
        self.buildings.append(building)

    def define_blocked_spaced(self, array:list):
        self.blocked_spaces = array

    def add_npc(self, npc:NPC):
        self.npcs.append(npc)

    def add_trainer(self, trainer:ActorBattleInfo):
        self.trainers.add_trainer(trainer)

    def add_route(self, route:Route):
        self.adjacent_areas.append(route)

    def define_area_transitions(self, transition_dict:dict):
        self.transition_dict = transition_dict

    def define_blocked_spaced(self, array:list[tuple[int,int]]):
        self.blocked_spaces = array

    def define_ledges(self, array:list[tuple[int,int]]):
        self.ledges = array

    def draw_map(self):
        if not self.map:
            print('no map')
            return
        ui.display.active.set_player_sprite(self.player.active_sprite)
        self.map.draw(ui.display.active.window)
        ui.display.active.update()

    def print_buildings(self):
        text = '\nAvailable Buildings:'
        print(text)
        for i, building in enumerate(self.buildings):
            text = f'{i+1}: {building.name}'
            print(text)

    def select_building(self, response:str):
        for i, building in enumerate(self.buildings):
            i_str = str(i+1)
            building_name = building.name.strip().lower()
            if response == i_str or response == building_name:
                text = f'Enter the {building.name}?'
                if get_confirmation(text):
                    return building
        return None

    def enter_a_building(self):
        looking_for_building = True
        building = None
        while looking_for_building:
            self.print_buildings()
            text = '\nWhich building would you like to enter? '
            response = input(text).strip().lower()
            building = self.select_building(response)
            if not building:
                text = f'No match found for {response}.'
                print(text)
                if not try_again():
                    looking_for_building = False
            else:
                building.enter_building(self.player)
                looking_for_building = False

    def talk_to_npc(self):
        pass

    def determine_encounter(self):
        '''
        Takes player position to see they enouncter a trainer or wild pokemon.'
        '''
        encounter = None
        #encounter = self.check_trainer_line_of_sight()
        if encounter:
            return encounter
        #encounter = self.search_tall_grass()
        return encounter

    def select_route(self, target_coords):
        for key in self.transition_dict.keys():
            value = self.transition_dict[key]
            if target_coords not in value[0]:
                return
        print('atempting transition')
        print(target_coords)

    def start_on_route(self, starting_pos, key):
        route = None
        for area in self.adjacent_areas:
            if area.name != key:
                continue
            area.starting_position = starting_pos
            route = area
            break
        return route

    def check_route_transition(self, target_coords):
        for key in self.transition_dict.keys():
            value:list[list] = self.transition_dict[key]
            print(value)
            if target_coords not in value[0]:
                continue
            index = value[0].index(target_coords)
            action = self.start_on_route(value[1][index], key)
            if action:
                return action

    def reset_velocity(self):
        self.player.active_sprite.velocity.y = 0
        self.map.velocity.y = 0
        self.player.active_sprite.velocity.x = 0
        self.map.velocity.x = 0

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
            print(self.map.pos.y)
            print(self.map.vertical_bound)
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
        target_coords = (coords[0] + x, coords[1]+ y)
        if target_coords in self.blocked_spaces:
            return
        if target_coords in self.ledges:
            if y != 1:
                return
            self.map.velocity.y += self.map.velocity.y
            self.player.active_sprite.velocity.y += self.player.active_sprite.velocity.y
        route = self.check_route_transition(target_coords)
        if route:
            return route
        self.map.move_image()
        self.player.active_sprite.move_image()

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

    def navigate_area(self):
        ui.display.active.window.fill(black)
        action = ui.input.get_player_input(True)
        if action:
            print(action)
        moving = self.map.moving or self.player.active_sprite.moving
        if moving:
            self.map.move_image()
            self.player.active_sprite.move_image()
            moving = self.map.moving or self.player.active_sprite.moving
            if not moving:
                self.determine_encounter()
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

    def set_player_start_pos(self):
        self.map.pos.x, self.map.pos.y = 0, 0
        self.player.active_sprite.x, self.player.active_sprite.y = 0, 0
        starting_position = self.starting_position
        print('start pos')
        print(starting_position)
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
            print(self.get_coordinate())
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
            if self.get_coordinate()[1] == starting_position[1]:
                break
        print('finished y')

    def enter_area(self, player:Player):
        text = f'Entering {self.name}.'
        print(text)
        self.player = player
        in_area = True
        self.constructed_array = []
        self.set_player_start_pos()
        while in_area:
            self.draw_map()
            action = self.get_action()
            if type(action) == Route:
                return action
            if action == exit:
                return action
            if self.player.battle_info.white_out:
                return leave

    def get_action(self):
        action = self.navigate_area()
        if action == exit:
            return action
        elif type(action) == Route:
            return action
        elif action == leave:
            return action
        if action == exit:
            return action
        if action == select:
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
        if action == 'b':
            return exit
