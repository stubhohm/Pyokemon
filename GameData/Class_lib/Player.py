from ..Function_Lib.General_Functions import get_confirmation
from ..Keys import player, hp
from ..Keys import male, female
from ..Colors import black
from ..Constants import terminal_font_size
from .Creature import Creature
from .Inventory import Inventory
from .Item import Item
from .UI import ui
from .ActorBattleInfo import ActorBattleInfo
from .PlayerCombatInput import PlayerCombatInput
from ..Sprites.PlayerSprites.Sprites import male_idle_sprite
from ..Sprites.ImageImport import Sprite


class Player():
    def __init__(self, name:str, gender) -> None:
        self.pc:list[Creature] = []
        self.gender = gender
        self.set_player_name(name)
        self.set_sprite_library()
        self.is_surfing = False

    def set_player_name(self, name:str):
        self.name = name

    def set_sprite_library(self):
        if self.gender == male:
            self.sprite_library = {'idle' : male_idle_sprite}
        else:
            self.sprite_library = {'idle' : male_idle_sprite}
        self.set_active_sprite(self.sprite_library['idle'])

    def set_active_sprite(self, sprite:Sprite):
        self.active_sprite = sprite

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