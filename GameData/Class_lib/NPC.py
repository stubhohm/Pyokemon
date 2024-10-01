from ..Keys import up, down, left, right
from .Creature import Creature
from .Quests import Quest, Trade, Fetch, Delivery
from ..Interactable_Items.Sign import Sign
from .Sprite import Sprite

invert_direction = {up: down, down:up, left:right, right:left}

class NPC():
    def __init__(self, name:str) -> None:
        self.set_name(name)
        self.sprite = Sprite(name, 2)
        self.quest = None
        self.interaction = Sign(name)
        self.set_dialog('Not Defined')

    def set_name(self, name:str):
        self.name = name

    def set_quest(self, quest:Quest):
        self.quest = quest

    def set_dialog(self, dialog:str):
        self.interaction.set_display_text(dialog)

    def set_position(self, position:tuple[int, int]):
        self.interaction.set_coordinate(position)
        self.sprite.set_sprite_coordinates(self.interaction.coordinate)

    def get_quest(self):
        if not self.quest:
            return
        return self.quest

    def face_player(self, player):
        direction = player.animation.get_last_direction()
        npc_direction = invert_direction.get(direction, down)
        
    def interact(self, player):
        self.face_player(player)
        if quest := self.get_quest():
            if quest.initiate_quest():
                player.inventory.add_item(quest.get_quest_items())
                player.add_quest(quest)
        for quest in player.quests:
            if not isinstance(quest, Quest):
                continue
            quest.set_current_npc_name(self.name)
            quest.progress_quest()
            if rewards:= quest.check_quest_status():
                player.inventory.add_loot(rewards)
                player.inventory.update_inventory()
                quest.reward_claimed()
                return
        self.interaction.interact()     