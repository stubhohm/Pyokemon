from ..Keys import no_weather, exit, leave
from ..Keys import select, cancel, up, down, left, right, terminate
from ..Keys import idle
from ..Keys import navigation, wild
from ..Keys import name, door_location
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
from .Interactable import Interactable
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
        self.draw_below_player:list[Sprite] = []
        self.draw_above_player:list[Sprite] = []
        self.interactables:list[Interactable] = []
        self.transition_dict = {}

    def set_sprite(self, sprite:Sprite):
        self.map = sprite

    def add_building(self, building:Building):
        self.buildings.append(building)
        building_dict = { name: building.name,
                    door_location: building.door_coordinate_in}
        print(f'{self.name}, {building.name}')
        self.navigation.add_to_building_dicts(building_dict)

    def add_npc(self, npc:NPC):
        self.npcs.append(npc)

    def add_trainer(self, trainer:ActorBattleInfo):
        self.trainers.add_trainer(trainer)

    def add_tall_grass(self, tall_grass:TallGrass):
        self.tall_grass_zones.append(tall_grass)   

    def add_route(self, route:Route):
        self.navigation.adjacent_areas.append(route)

    def add_to_draw_below_player(self, sprite:Sprite):
        self.draw_below_player.append(sprite)

    def add_to_draw_above_player(self, sprite:Sprite):
        self.draw_above_player.append(sprite)

    def add_interactable(self, interactable:Interactable):
        self.interactables.append(interactable)

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

    def draw_item_sprites(self, sprite:Sprite):
        sprite.set_image_from_clock_ticks(self.ticks)
        for position in sprite.image_coordinates:
            sprite.jump_to_coordinate(position, self.map.pos)    
            sprite.draw(ui.display.active.window)

    def draw_items_above_player(self):
        for sprite in self.draw_above_player:
            self.draw_item_sprites(sprite)

    def draw_items_below_player(self):
        for sprite in self.draw_below_player:
            if not sprite:
                continue
            self.draw_item_sprites(sprite)
        for item in self.interactables:
            if not item.sprite:
                continue
            self.draw_item_sprites(item.sprite)

    def draw_npcs(self, under_player_image:bool):
        player_y = self.player.animation.active_sprite.get_pos()[1]
        for npc in self.npcs:
            npc_y = npc.sprite.get_pos()[1]
            if npc_y > player_y:
                self.draw_item_sprites(npc.sprite)
            else:
                if under_player_image:
                    self.draw_item_sprites(npc.sprite)

    def draw_map(self):
        if not self.map:
            print('no map')
            return
        
        ui.display.active.set_player_sprite(self.player.animation.active_sprite)
        self.map.draw(ui.display.active.window)
        self.draw_items_below_player()
        self.draw_npcs(True)
        ui.display.active.draw_player()
        self.draw_npcs(False)
        self.draw_items_above_player()
        ui.display.active.update()

    def select_building(self):
        coordinate = self.navigation.get_coordinate()
        for building in self.buildings:
            if not building:
                continue
            if coordinate in building.door_coordinate_in:
                return building
        return None

    def enter_a_building(self):
        building = self.select_building()
        if not building:
            return
        else:
            building.enter_building(self.player)
            self.navigation.starting_position = (building.door_coordinate_in[-1][0], building.door_coordinate_in[-1][1] + 1)
            self.navigation.set_player_start_pos()
            self.player.animation.set_last_direction(down)
            self.player.animation.set_movement_type(idle)
            if building.healing_station:
                self.player.last_healing_location = self

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

    def check_npc_interactions(self):
        for npc in self.npcs:
            print(npc.name)
            if not npc:
                continue
            facing_space = self.navigation.get_coordinate_plus_one(self.navigation.get_coordinate())
            print(facing_space)
            print(npc.interaction.coordinate)
            if facing_space != npc.interaction.coordinate:
                continue
            npc.interact(self.player)

    def check_item_interactions(self):
        for item in self.interactables:
            if not item:
                continue
            facing_space = self.navigation.get_coordinate_plus_one(self.navigation.get_coordinate())
            if facing_space != item.coordinate:
                continue
            if item.is_lootable:
                loot = item.interact()
                if not loot:
                    return
                self.player.inventory.add_loot(loot)
            else:
                item.interact()

    def check_interaction(self):
        self.enter_a_building()
        self.check_item_interactions()
        self.check_npc_interactions()

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
        if encounter:
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

    def resolve_action(self):
        self.enter_a_building()
        encounter = self.determine_encounter()
        if type(encounter) == Creature:
            self.battle_wild_pokemon(encounter, self.player)
        elif type(encounter) == ActorBattleInfo:
            self.trainers.engage_trainer(encounter, self.player)

    def enter_area(self, player:Player):
        self.ticks = 0
        text = f'Entering {self.name}.'
        print(text)
        self.player = player
        self.navigation.define_navigation(self.player, self.map)
        in_area = True
        self.constructed_array = []
        self.navigation.set_player_start_pos()
        while in_area:
            action = self.navigation.navigate_area()
            self.draw_map()
            self.ticks += 1
            if action in [exit, leave]:
                return action
            elif action == select:
                self.check_interaction() 
            elif action:
                self.resolve_action()
          
            if self.ticks % 60 == 0:
                self.ticks = 0
            elif action == 'item':
                self.player.use_an_item()
            if self.navigation.switch_area:
                self.navigation.switch_area = False
                return action
