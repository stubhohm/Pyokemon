from ..Modules.External_Modules import Surface, time
from ..Keys import player, hp
from ..Keys import male, female
from ..Keys import up, down, left, right, directional_inputs
from ..Keys import walk, idle, run, jump, movement_types
from ..Colors import black
from ..Constants import terminal_font_size, step_distance
from .Creature import Creature
from .Inventory import Inventory
from .Item import Item
from .UI import ui
from .ActorBattleInfo import ActorBattleInfo
from .PlayerCombatInput import PlayerCombatInput
from ..Sprites.PlayerSprites.ImageImports import get_player_sprite_dict
from .Sprite import Sprite



class Player():
    def __init__(self, name:str, gender:str) -> None:
        self.set_player_name(name)
        self.pc:list[Creature] = []
        self.gender = gender
        self.movement_type = idle
        self.last_direction = down
        self.steps = 0
        self.pixels = 0
        self.active_sprite = Sprite(f'{self.name} Sprite', 2)
        self.set_sprite_library()
        
    def set_player_name(self, name:str):
        self.name = name

    def set_sprite_library(self):
        self.sprite_library = get_player_sprite_dict(self.gender)
        image_array = self.get_image_array()
        self.active_sprite.set_animation_loop(len(image_array))
        self.set_active_image(image_array[0])
        self.active_sprite.y_shift = self.active_sprite.image.get_height() * 3 / 8
        self.active_sprite.x_center = self.active_sprite.image.get_width() / 2

    def set_active_sprite(self, sprite:Sprite):
        self.active_sprite = sprite

    def set_active_image(self, image:Surface):
        self.active_sprite.image = image

    def update_player_sprite(self):
        frame = self.active_sprite.get_current_frame(self.steps)
        image_array = self.get_image_array()
        self.set_active_image(image_array[frame])

    def incriment_steps(self):
        self.pixels += 1
        if self.pixels % (step_distance / 4) == 0:
            self.steps += 1
            self.pixels = 0
        if self.pixels % (step_distance / 8) == 0:
            self.update_player_sprite

    def reset_steps(self):
        self.steps = 0

    def get_image_array(self) -> list:
        return self.sprite_library[self.get_last_direction()][self.get_movement_type()]

    def get_last_direction(self):
        if not self.last_direction in directional_inputs:
            return down
        else:
            return self.last_direction

    def get_movement_type(self):
        if not self.movement_type:
            return idle
        else:
            return self.movement_type

    def get_animation_start(self):
        frame = 1
        while not frame == 0:
            self.incriment_steps()
            frame = self.active_sprite.get_current_frame(self.steps)

    def set_movement_type(self, movement_type):
        if movement_type not in movement_types:
            return
        elif self.movement_type not in movement_types:
            self.movement_type = idle
        else:
            self.movement_type = movement_type
        self.active_sprite.set_animation_loop(len(self.get_image_array()))
        is_jumping = (self.movement_type == jump)
        self.active_sprite.set_jumping(is_jumping)
        if is_jumping:
            self.get_animation_start()

    def set_last_direction(self, direction):
        if direction not in directional_inputs:
            return
        elif self.last_direction not in directional_inputs:
            self.last_direction = down
        else:
            self.last_direction = direction

    def print_to_terminal(self, text):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)

    def print_roster(self):
        for i, creature in self.roster:
            text = f'{i+1}: {creature.name}'
            print(text)

    def add_to_pc(self, sent_pokemon:Creature):
        self.pc.append(sent_pokemon)

    def add_pokemon_to_roster(self, new_pokemon:Creature):
        self.roster.append(new_pokemon)
        while len(self.roster) > 6:
            text = 'You need to send a pokemon to the PC, who would you like to send?'
            self.print_to_terminal(text)
            print(text)
            self.set_battle_info()
            send_back = self.combat_inputs.pick_from_roster(self.battle_info, 'send to the PC')
            if send_back:
                self.roster.remove(send_back)
                text = f'Sending {send_back.name} to the PC.'
                self.print_to_terminal(text) 
                print(text)
                self.add_to_pc(send_back)

    def set_roster(self):
        self.roster:list[Creature] = []

    def set_inventory(self, inventory:Inventory):
        self.inventory = inventory

    def set_combat_inputs(self, combat_inputs:PlayerCombatInput):
        self.combat_inputs = combat_inputs

    def set_battle_info(self):
        self.battle_info = ActorBattleInfo()
        self.update_battle_info()

    def update_battle_info(self):
        self.battle_info.define_battle_info(self.roster, self.inventory, player, self.name)

    def get_battle_info(self):
        self.set_battle_info()
        return self.battle_info

    def use_an_item(self):
        self.update_battle_info()
        choice = self.combat_inputs.combat_item(self.battle_info)
        if choice:
            item:Item = choice[0]
            target:Creature = choice[-1]
            item.use_item(target)
        self.inventory.update_inventory()