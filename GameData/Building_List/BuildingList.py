from ..Modules.External_Modules import os
from ..Constants import step_distance
from ..Keys import pokemart, pokemon_center, building
from ..Keys import antidote
from ..Class_lib.Player import Player
from ..Class_lib.Sprite import Sprite
from ..Class_lib.Building import Building
from ..Class_lib.PC import PC
from ..Class_lib.ShopCounter import ShopCounter
from ..Class_lib.ActorBattleInfo import ActorBattleInfo
from ..Interactable_Items.HealingStation import HealingStation
from ..Sprites.MapComponents.MapImports import generate_pokemon_center_map, generate_pokemart_map
from ..Sprites.MapComponents.TerrainItemsImports import get_image_array
from ..Sprites.MapComponents.NPCImports import get_npc_image_array
from .NavigationDicts import pokemon_center_blocked_spaces_dict, pokemart_blocked_spaces_dict


class PokemonCenter(Building):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        super().set_type(pokemon_center)
        super().set_sprite(generate_pokemon_center_map())
        super().set_door_out([(8,11), (9,11)])
        super().define_blocked_spaces(pokemon_center_blocked_spaces_dict)
        self.add_healing_station()
        self.get_nurse_sprite()
        self.get_recovering_pokeballs_sprite()

    def add_healing_station(self):
        self.healing_station = HealingStation('Healing Station')
        self.healing_station.set_coordinate((9, 5))

    def get_recovering_pokeballs_sprite(self):
        self.pokeballs = get_image_array('HealingPokeballs', 6)
        sprite = Sprite('recovering pokeballs', 2)
        sprite.set_image_array(self.pokeballs)
        sprite.set_sprite_coordinates([(self.healing_station.coordinate[0] - 2, self.healing_station.coordinate[1] - 4)])
        sprite.tickrate = 15
        sprite.y_shift = 15
        sprite.x_shift = 10
        self.recovering_pokeballs = sprite
        self.active_recovering = None
        self.add_to_draw_below_player(self.active_recovering)

    def get_nurse_sprite(self):
        directory_path = os.path.join('Nurse', 'Down')
        self.nurse_down = get_npc_image_array(directory_path, 1)
        directory_path = os.path.join('Nurse', 'Left')
        self.nurse_left = get_npc_image_array(directory_path, 1)
        sprite = Sprite('Nurse Joy', 2)
        sprite.set_image_array(self.nurse_down)
        sprite.set_sprite_coordinates([(self.healing_station.coordinate[0], self.healing_station.coordinate[1] - 3)])
        sprite.tickrate = 60
        sprite.y_shift = - 16
        sprite.x_shift = - 8
        self.nurse_sprite = sprite
        self.add_to_draw_below_player(self.nurse_sprite)

    def play_heal_animation(self):
        healing = True
        ticks = 0
        start_time = 20
        finish_heal_tick= 0
        heal_time = 120
        done = False
        while healing:
            if ticks == start_time:
                self.nurse_sprite.set_image_array(self.nurse_left)
                self.active_recovering = self.recovering_pokeballs
                self.add_to_draw_below_player(self.active_recovering)
                print('set self.active_recovering to self.recovering_pokeballs')
                print(self.active_recovering.frames_in_loop)
            if ticks > start_time and not done:
                if self.active_recovering.animation_frame == len(self.player.roster) - 1:
                    print('adding')
                    done = True
                    finish_heal_tick = ticks + heal_time
                else:
                    adjusted_ticks = ticks - start_time
                    self.active_recovering.set_image_from_clock_ticks(adjusted_ticks)
                    print(self.active_recovering.animation_frame)      
            if done:
                if self.active_recovering.animation_frame == 0:
                    healing = False
                    self.nurse_sprite.set_image_array(self.nurse_down)
                    self.draw_below_player.remove(self.active_recovering)
                if ticks == finish_heal_tick:
                    self.active_recovering.animation_frame = 0
            ticks += 1
            self.draw_map()

    def heal_roster(self):
        self.healing_station.interact()
        self.play_heal_animation()
        for roster_pokemon in self.player.roster:
            roster_pokemon.heal_at_pokecenter()
        print('You roster has been fully healed.')

    def check_interaction(self):
        super().check_interaction()
        forward_pos = self.navigation.get_coordinate_plus_one(self.navigation.get_coordinate())
        if forward_pos == self.healing_station.coordinate:
            self.heal_roster()
        if forward_pos == self.pc.coordinates:
            self.pc.use_pc(self.player.get_battle_info())
    
    def enter_building(self, player: Player):
        super().add_pc_interface(player.pc)
        return super().enter_building(player)


class Pokemart(Building):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        super().set_type(pokemart)
        super().set_sprite(generate_pokemart_map())
        super().set_door_out([(11,12), (12,12)])
        super().define_blocked_spaces(pokemart_blocked_spaces_dict)
        self.add_shop_counter()
        self.get_shopkeep_sprite()

    def add_shop_counter(self):
        self.shop_interface = True
        self.shop_counter = ShopCounter(f'{self.name} counter')
        self.shop_counter.set_coordinates([(10,7), (9,8)])

    def get_shopkeep_sprite(self):
        directory_path = os.path.join('ShopKeep', 'Down')
        self.shopkeep_down = get_npc_image_array(directory_path, 1)
        directory_path = os.path.join('ShopKeep', 'Left')
        self.shopkeep_left = get_npc_image_array(directory_path, 1)
        directory_path = os.path.join('ShopKeep', 'Right')
        self.shopkeep_right = get_npc_image_array(directory_path, 1)
        sprite = Sprite('ShopKeep John', 2)
        sprite.set_image_array(self.shopkeep_right)
        sprite.set_sprite_coordinates([(1,2)])
        sprite.tickrate = 60
        sprite.y_shift = -8
        sprite.x_shift = 0
        self.shopkeep_sprite = sprite
        self.add_to_draw_below_player(self.shopkeep_sprite)

    def get_shopkeep_direction(self):
        player_pos = self.navigation.get_coordinate()
        x, y = int(self.shopkeep_sprite.pos.x / step_distance) - player_pos[0] + 4 , int(self.shopkeep_sprite.pos.y / step_distance) - player_pos[1] + 2
        if abs(x) > abs(y):
            self.shopkeep_sprite.set_image_array(self.shopkeep_right)
        if abs(x) < abs(y):
            self.shopkeep_sprite.set_image_array(self.shopkeep_down)

    def draw_map(self):
        self.get_shopkeep_direction()
        super().draw_map()

    def check_interaction(self):
        super().check_interaction()
        target_coord = self.navigation.get_coordinate_plus_one(self.navigation.get_coordinate())
        if target_coord in self.shop_counter.coordinates:
            self.shop_counter.go_to_counter(self.player.inventory)

class Gym(Building):
    def __init__(self, name: str, trainers:list[ActorBattleInfo], leader:ActorBattleInfo) -> None:
        super().__init__(name)
        for trainer in trainers:
            super().add_trainer(trainer)
        self.set_gym_leader(leader)

    def set_gym_leader(self, gym_leader:ActorBattleInfo):
        self.trainers.set_gym_leader(gym_leader)

def make_building(name:str, entry_coords:list[tuple], exit_coords:list[tuple], map, blocked_spaces:dict):
    bbuilding = Building(name)
    bbuilding.set_door_in(entry_coords)
    bbuilding.set_door_out(exit_coords)
    bbuilding.set_sprite(map)
    bbuilding.define_blocked_spaces(blocked_spaces)
    return bbuilding


