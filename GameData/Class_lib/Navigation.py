from ..Constants import step_distance, screen_size
from ..Constants import ghost_mode
from ..Colors import black
from ..Keys import exit, leave, cancel
from ..Keys import up, down, left, right, directional_inputs
from ..Keys import walk, idle, jump, run, surfing
from .Player import Player
from .Sprite import Sprite
from .UI import ui


class Navigation():
    def __init__(self) -> None:
        self.adjacent_areas = []
        self.constructed_dict = {}
        self.top_left = ()
        self.bottom_right = ()
        self.blocked_spaces = {}
        self.ledges = {}
        self.ledge_tops = {}
        self.water_spaces = {}
        self.transition_dict:dict = {}
        self.switch_area = False
        self.starting_position:list[tuple[int,int]] = (0,0) 
        self.ghost_mode = ghost_mode

    def define_navigation(self, player:Player, map:Sprite):
        self.player = player
        self.map = map
        self.player.get_animation_start()

    def set_player_start_pos(self):
        setup = True
        self.map.pos.x, self.map.pos.y = 0, 0
        self.player.active_sprite.x, self.player.active_sprite.y = 0, 0
        starting_position = self.starting_position
        print(f'Start pos: {self.starting_position}')
        sum_x, sum_y = 0, 0
        while not (self.get_coordinate()[0] == starting_position[0]):
            if (self.get_coordinate()[0] > starting_position[0]):
                mod = -1
            elif (self.get_coordinate()[0] < starting_position[0]):
                mod = 1
            else:
                mod = 0
            sum_x += mod
            print(sum_x)
            self.handle_x_movement(mod, setup)
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
            sum_y += mod
            print(sum_y)
            self.handle_y_movement(mod, setup)
            self.map.jump_image()
            self.player.active_sprite.jump_image()
        print('finished y')
        self.reset_velocity()
        self.player.get_animation_start()

    def move_sprites(self):
        self.map.move_image()
        self.player.active_sprite.move_image()
        self.player.incriment_steps()
        self.player.update_player_sprite()

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

    def handle_x_movement(self, x:int, setup = False):
        screen_width = screen_size[0]
        screen_height = screen_size[1]
        half_step = step_distance / 2
        horizontal_pin = False
        self.reset_velocity()
        if x < 0:
            horizontal_pin = (self.map.pos.x == 0)
            if not setup:
                self.player.set_last_direction(left)
        else: 
            horizontal_pin = (self.map.pos.x <= self.map.horizontal_bound)
            if not setup:
                self.player.set_last_direction(right)
        player_off_center = not((screen_width / 2 - half_step) <= self.player.active_sprite.pos.x <= (screen_width / 2 + half_step))
        player_off_screen = (self.player.active_sprite.pos.x > screen_width or self.player.active_sprite.pos.y > screen_height)
        if horizontal_pin or player_off_center:
            self.player.active_sprite.set_velocity(x, 0)
        else:
            self.map.set_velocity(x, 0)

    def handle_y_movement(self, y:int, setup = False):
        screen_width = screen_size[0]
        screen_height = screen_size[1]
        half_step = step_distance / 2
        vertical_pin = False
        self.reset_velocity()
        if y < 0:
            vertical_pin = (self.map.pos.y == 0)
            if not setup:
                self.player.set_last_direction(up)
        else: 
            vertical_pin = (self.map.pos.y <= self.map.vertical_bound)
            if not setup:
                self.player.set_last_direction(down)
        player_off_center = not((screen_height / 2 - half_step) <= self.player.active_sprite.pos.y <= (screen_height / 2 + half_step))
        player_off_screen = (self.player.active_sprite.pos.x > screen_width or self.player.active_sprite.pos.y > screen_height)
        if (vertical_pin or player_off_center) and not player_off_screen:
            self.player.active_sprite.set_velocity(0, y)
        else:
            self.map.set_velocity(0, y)

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
        target_area.navigation.starting_position = starting_pos
        self.switch_area = True
        return target_area

    def check_area_departure(self):
        coords =  self.get_coordinate()
        target_coords = self.get_coordinate_plus_one(coords)
        for key in self.transition_dict.keys():
            value:list[list] = self.transition_dict[key]
            if target_coords in value[0]:
                print(f'Target: {target_coords}')
                print(key)
                index = value[0].index(target_coords)
                return self.select_new_area(value[1][index], key)

    def handle_movement(self, x:int, y:int):
        self.player.set_movement_type(walk)
        if x != 0:
            self.handle_x_movement(x)
        if y != 0:
            self.handle_y_movement(y)
        coords =  self.get_coordinate()
        target_coords = self.get_coordinate_plus_one(coords)
        target_coords_1 = self.get_coordinate_plus_one(target_coords)
        if self.blocked_spaces.get(target_coords, False) and not self.ghost_mode:
            self.player.set_movement_type(idle)
            self.player.update_player_sprite()
            return
        if self.water_spaces.get(target_coords, False):
            if not self.player.movement_type == surfing:
                return
        else:
            if self.player.movement_type == surfing:
                self.player.movement_type = idle
                self.jump_ledge()
        
        if self.ledges.get(target_coords, False) and not self.ghost_mode:
            if not self.ledge_tops.get(self.get_coordinate(), False):
                self.player.set_movement_type(idle)
                self.player.update_player_sprite()
                print('not at a ledgetop')
                return
            if self.blocked_spaces.get(target_coords_1, False) or self.ledges.get(target_coords_1, False):
                self.player.set_movement_type(idle)
                self.player.update_player_sprite()
                print('target space is blocked')
                return
            else:
                self.jump_ledge()
        self.move_sprites()

    def jump_ledge(self):
        self.player.set_movement_type(jump)
        self.map.set_jumping(True)

    def print_coordinate_list(self, name, coords):
        if self.blocked_spaces.get(coords, False):
            print(f'{name} is in blocked.')
        if self.ledges.get(coords, False):
            print(f'{name} is in ledges.')
        if self.ledge_tops.get(coords, False):
            print(f'{name} is in ledge tops.')
        if self.water_spaces.get(coords, False):
            print(f'{name} is in water space.')

    def print_coordinates_lists(self):
        coord_names = ['Current Position', 'Target', 'Target + 1']
        coords =  self.get_coordinate()
        target_coords = self.get_coordinate_plus_one(coords)
        target_coords_1 = self.get_coordinate_plus_one(target_coords)
        coord_list = [coords, target_coords, target_coords_1]
        for i, name in enumerate(coord_names):
            self.print_coordinate_list(name, coord_list[i])

    def add_to_dict(self):
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
                if self.constructed_dict.get(coords, False):
                    continue
                print(coords)
                self.constructed_dict[coords] = True
        print('finished adding set')
        self.top_left = None
        self.bottom_right = None

    def map_area_helper_function(self, key_input):
        if key_input == 'm':
            self.add_to_dict()
        if key_input == 'a':
            self.top_left = self.get_coordinate()
            print(self.top_left)
        if key_input == 's':
            self.bottom_right = self.get_coordinate()
            print(self.bottom_right)
        if key_input == 'c':
            self.constructed_dict = {}
        if key_input == 'p':
            print(self.constructed_dict)
        if key_input == 't':
            self.print_coordinates_lists()
        if key_input == 'g':
            self.ghost_mode = (not self.ghost_mode)
            if self.ghost_mode:
                print("Ghost mode on.")
            else:
                print("Ghost mode off.")

    def navigate_area(self):
        ui.display.active.window.fill(black)
        action = ui.input.get_player_input(True)    
        moving = self.map.moving or self.player.active_sprite.moving
        if moving:
            self.move_sprites()
            moving = self.map.moving or self.player.active_sprite.moving
            if not moving:
                self.player.set_movement_type(idle)
                self.map.set_jumping(False)
                self.player.update_player_sprite()
                return True
            return False
        if self.player.battle_info.white_out:
            return leave
        if action == cancel:
            return exit
        if not action in directional_inputs:
            self.map_area_helper_function(action)
            return False
        x, y = self.determine_velocity(action)        
        if x != 0 or y != 0:
            action = self.handle_movement(x,y)
        area = self.check_area_departure()
        if area:
            return area
        return False