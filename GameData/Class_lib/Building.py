from ..Keys import pokemon_center, pokemart, building, gym, leave, exit
from ..Keys import no_weather, hp, select, name
from ..Function_Lib.General_Functions import get_confirmation, try_again
from .ActorBattleInfo import ActorBattleInfo
from .NPC import NPC
from .PC import PC
from .ShopCounter import ShopCounter
from .Player import Player
from .Battle import Battle
from .Sprite import Sprite
from .Navigation import Navigation
from .LocalTrainers import LocalTrainers
from .Interactable import Interactable
from ..Interactable_Items.HealingStation import HealingStation
from .UI import ui

class Building():
    def __init__(self, name:str) -> None:
        self.set_name(name)
        self.npcs:list[NPC] = []
        self.trainers:LocalTrainers = LocalTrainers()
        self.interactables:list[Interactable] = []
        self.draw_above_player = []
        self.draw_below_player = []
        self.pc_interface = False
        self.healing_station = False
        self.shop_interface = False
        self.is_gym = False
        self.navigation = Navigation()
        self.door_coordinate_in:list[tuple] = [(0,0)]
        self.door_coordinate_out:list[tuple] = [(0,0)]
        self.map = Sprite('None Attributes', 1)

    def set_name(self, name:str):
        self.name = name

    def set_sprite(self, sprite:Sprite):
        self.map = sprite

    def set_door_in(self, entry:list[tuple]):
        self.door_coordinate_in = entry

    def set_door_out(self, exit:list[tuple]):
        self.door_coordinate_out = exit

    def define_blocked_spaces(self, blocked_spaces_dict:dict):
        self.navigation.blocked_spaces = blocked_spaces_dict

    def set_type(self, type:str):
        self.type = type
        if type == pokemon_center:
            self.add_healing_station()
            self.pc_interface = True
        if type == pokemart:
            self.shop_interface = True
        if type == gym:
            self.is_gym = True

    def add_pc_interface(self, pc:PC):
        self.pc_interface = True
        self.pc = pc

    def add_interactable(self, item:Interactable):
        self.interactables.append(item)

    def talk_to_npc(self):
        print('talking to an npc')

    def open_pc(self):
        self.pc.use_pc(self.player.get_battle_info())

    def get_matching_trainer(self, response:str, viable_trainers:list[ActorBattleInfo]):
        '''
        Returns a matching trainer by name or number or none if not found.
        '''
        selected_trainer = None
        for i, trainer in enumerate(viable_trainers):
            i_str = str(i+1)
            trainer_name = trainer.name.strip().lower()
            if trainer_name == response or i_str == response:
                selected_trainer = trainer
                break
        return selected_trainer

    def talk_to_clerk(self):
        self.shop_counter.go_to_counter()

    def determine_encounter(self, action):
        '''
        Takes player response to see if it is npc, item leave, pc, or heal'
        '''
        encounter = None
        if not action:
            return None
        print(action)
        if action == exit:
            return action
        return
        if 'npc' in action and len(self.npcs) > 0:
            encounter = self.talk_to_npc()  
        elif 'heal' in action and self.healing_station:
            text = 'Have the nurse heal your pokemon?'
            if get_confirmation(text):
                encounter = self.heal_roster()
        elif 'pc' in action and self.pc_interface:
            text = 'Open the PC?'
            if get_confirmation(text):
                encounter = self.open_pc()
        elif 'trainer' in action and len(self.trainers.trainers) > 0:
            text = 'Battle a trainer?'
            if get_confirmation(text):
                self.trainers.engage_trainer(self.player.get_battle_info())
        elif 'leader' in action and self.is_gym:
            text = 'Try Battleing the Gym Leader?'
            if get_confirmation(text):
                self.trainers.engage_leader(self.player.get_battle_info())
        elif 'item' in action:
            encounter = 'item'
            if get_confirmation('Use an item?'):
                self.player.use_an_item()
        elif 'clerk' in action and self.shop_interface:
            if get_confirmation('Talk to the store clerk?'):
                self.talk_to_clerk()
        elif leave in action:
            encounter = leave
        return encounter
  
    def add_npc(self, non_player_character:NPC):
        self.npcs.append(non_player_character)

    def add_trainer(self, trainer:ActorBattleInfo):
        self.trainers.add_trainer(trainer)
       
    def add_to_draw_below_player(self, sprite:Sprite):
        self.draw_below_player.append(sprite)

    def add_to_draw_above_player(self, sprite:Sprite):
        self.draw_above_player.append(sprite)

    def building_actions(self):
        if self.player.battle_info.white_out:
            return leave
        text = '\nWould you like to use an item, '
        if len(self.trainers.trainers) > 0:
            text += 'battle a trainer, '
            if self.is_gym:
                text += 'or gym leader, '
        if len(self.npcs) > 0:
            text += 'talk with an NPC, '
        if self.shop_interface:
            text += 'talk to the clerk, '
        if self.healing_station:
            text += 'heal your pokemon, '
        if self.pc_interface:
            text += 'use the PC, '
        text += 'or leave?: '
        response = input(text).strip().lower()
        return response

    def check_leave_building(self):
        if self.navigation.get_coordinate() in self.door_coordinate_out:
            print('leaving')
            return True
        return False

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
        self.check_item_interactions()
        ui.input.key_last = None

    def set_building_start_pos(self):
        starting_pos = (self.door_coordinate_out[-1][0], self.door_coordinate_out[-1][1] - 1)
        self.navigation.starting_position = starting_pos

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

    def draw_map(self):
        if not self.map:
            print('no map')
            return
        ui.display.active.set_player_sprite(self.player.animation.active_sprite)
        self.map.draw(ui.display.active.window)
        self.draw_items_below_player()
        ui.display.active.draw_player()
        self.draw_items_above_player()
        ui.display.active.update()

    def enter_building(self, player:Player):
        self.navigation.define_navigation(player, self.map)
        self.set_building_start_pos()
        self.navigation.set_player_start_pos()
        self.player = player
        in_building= True
        self.ticks = 0
        while in_building:
            self.draw_map()
            action = self.navigation.navigate_area()
            if action in [exit, leave]:
                return action
            if action == select:
                self.check_interaction()
            self.determine_encounter(action)
            if player.battle_info.white_out:
                return
            if self.check_leave_building():
                return
            self.ticks += 1
            if self.ticks % 60 == 0:
                self.ticks = 0
            
            
