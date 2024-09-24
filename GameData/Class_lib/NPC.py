from ..Keys import up, down, left, right
from .Creature import Creature
from .Quests import Quest, Trade, Fetch, Delivery
from .Interactable import Interactable

invert_direction = {up: down, down:up, left:right, right:left}

class NPC():
    def __init__(self, name:str) -> None:
        self.set_name(name)
        self.interaction = Interactable(name)

    def set_coordiante(self, coordiante:tuple[int, int]):
        self.interaction.set_coordinate(coordiante)

    def get_coordinate(self):
        return self.interaction.coordinate

    def set_name(self, name:str):
        self.name = name

    def set_quest(self, quest:Quest):
        self.quest = quest

    def get_quest(self):
        if not self.quest:
            return
        return self.quest

    def face_player(self, player):
        direction = player.get_last_direction()
        npc_direction = invert_direction.get(direction,down)
        

    def interact(self, player):
        self.face_player(player)
        if quest := self.get_quest():
            if quest.initiate_quest():
                player.inventory.add_items(quest.get_quest_items())
                player.add_quest(quest)
        for quest in player.quests:
            if type(quest) != Quest:
                continue
            quest.set_current_npc_name(self.name)
            quest.progress_quest()
            if rewards:= quest.check_quest_status():
                player.inventory.add_loot(rewards)          