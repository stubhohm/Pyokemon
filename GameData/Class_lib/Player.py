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
from .Quests import Quest
from .PlayerAnimation import PlayerAnimation
from .UI import ui
from .ActorBattleInfo import ActorBattleInfo
from .PlayerCombatInput import PlayerCombatInput



class Player():
    def __init__(self, name:str, gender:str) -> None:
        self.set_player_name(name)
        self.pc:list[Creature] = []
        self.gender = gender
        self.quests:list[Quest] = []
        self.animation = PlayerAnimation(gender, name)
        self.last_healing_location = None
        
    def set_player_name(self, name:str):
        self.name = name

    def print_to_terminal(self, text):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)

    def add_quest(self, quest:Quest):
        self.quests.append(quest)

    def remove_quest(self, quest:Quest):
        self.quests.remove(quest)

    def get_quests(self):
        if not self.quests:
            return []
        return self.quests

    def print_roster(self):
        print('printing roster')
        for i, creature in enumerate(self.roster):
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