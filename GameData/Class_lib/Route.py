from ..Keys import route, wild, npc
from ..Keys import exit, leave
from ..Keys import no_weather
from ..Keys import navigation, battle
from .Sprite import Sprite
from .TallGrass import TallGrass
from .Battle import Battle
from .Building import Building
from .ActorBattleInfo import ActorBattleInfo
from .Creature import Creature
from .Item import Item
from .Player import Player
from .LocalTrainers import LocalTrainers
from .Navigation import Navigation
from .UI import ui


class Route():
    def __init__(self, route_name:str) -> None:
        self.name = route_name
        self.type = route
        self.buildings:list[Building] = []
        self.tall_grass_zones:list[TallGrass] = []
        self.trainers:LocalTrainers = LocalTrainers()
        self.adjacent_areas:list = []
        self.navigation = Navigation()
        self.weather = no_weather

    def set_sprite(self, sprite:Sprite):
        self.map = sprite

    def add_tall_grass(self, tall_grass:TallGrass):
        self.tall_grass_zones.append(tall_grass)
    
    def add_trainer(self, trainer:ActorBattleInfo):
        self.trainers.add_trainer(trainer)

    def add_adjacent_area(self, area_class_object):
        self.navigation.adjacent_areas.append(area_class_object)

    def define_area_transitions(self, transition_dict:dict):
        self.navigation.transition_dict = transition_dict

    def define_blocked_spaced(self, dict:dict):
        self.navigation.blocked_spaces = dict

    def define_ledges(self, dict:dict):
        self.navigation.ledges = dict

    def define_ledge_tops(self, dict:dict):
        self.navigation.ledge_tops = dict

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
        coords = self.navigation.get_coordinate()
        encounter = None
        for tall_grass in self.tall_grass_zones:
            if coords in tall_grass.coordinates:
                encounter = tall_grass.check_for_encounter()
            if encounter:
                return encounter

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

    def battle_wild_pokemon(self, creature:Creature, player:Player):
        player.update_battle_info()
        wild_pokemon = ActorBattleInfo()
        wild_pokemon.define_battle_info([creature], None, wild, '')
        battle = Battle()
        battle.define_battle_start(player.battle_info, [wild_pokemon], no_weather)
        battle.battle_loop()
        ui.display.set_screen_state(navigation)
        ui.input.key_last = None

    
        

    def enter_area(self, player:Player):
        text = f'Entering {self.name}'
        print(text)
        self.player = player
        self.navigation.define_navigation(self.player, self.map)
        in_area = True
        self.constructed_array = []
        self.navigation.set_player_start_pos()
        while in_area:
            self.draw_map()
            encounter = None
            action = self.navigation.navigate_area()
            if action in [exit, leave]:
                return action
            if action:
                encounter = self.determine_encounter()
            if type(encounter) == Creature:
                self.battle_wild_pokemon(encounter, player)
            elif type(encounter) == ActorBattleInfo:
                self.trainers.engage_trainer(encounter, player)
            elif action == 'item':
                self.player.use_an_item()
            if self.navigation.switch_area:
                self.navigation.switch_area = False
                return action

        