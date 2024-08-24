from ..Keys import pokemon_center, pokemart, building, gym, leave, exit
from ..Keys import no_weather, hp
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
from .UI import ui

class Building():
    def __init__(self, name:str) -> None:
        self.set_name(name)
        self.npcs:list[NPC] = []
        self.trainers:LocalTrainers = LocalTrainers()
        self.pc_interface = False
        self.healing_station = False
        self.shop_interface = False
        self.is_gym = True
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

    def add_healing_station(self):
        self.healing_station = True

    def add_shop_counter(self, shop_counter:ShopCounter):
        self.shop_interface = True
        self.shop_counter = shop_counter

    def talk_to_npc(self):
        print('talking to an npc')

    def heal_roster(self):
        for roster_pokemon in self.player.roster:
            roster_pokemon.heal_at_pokecenter()
        print('You roster has been fully healed.')

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
    
    def set_gym_leader(self, gym_leader:ActorBattleInfo):
        self.trainers.set_gym_leader(gym_leader)

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

    def set_building_start_pos(self):
        starting_pos = (self.door_coordinate_out[-1][0], self.door_coordinate_out[-1][1] - 1)
        self.navigation.starting_position = starting_pos

    def draw_map(self):
        if not self.map:
            print('no map')
            return
        ui.display.active.set_player_sprite(self.player.active_sprite)
        self.map.draw(ui.display.active.window)
        ui.display.active.update()

    def enter_building(self, player:Player):
        self.navigation.define_navigation(player, self.map)
        self.set_building_start_pos()
        self.navigation.set_player_start_pos()
        self.player = player
        in_building= True
        if self.pc_interface:
            self.add_pc_interface(player.pc)
        while in_building:
            self.draw_map()
            action = self.navigation.navigate_area()
            if action in [exit, leave]:
                return action
            self.determine_encounter(action)
            if player.battle_info.white_out:
                return
            if self.check_leave_building():
                return
            
