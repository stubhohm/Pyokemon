from ..Keys import not_taken, taken, completed, rewarded
from .Item import Item
from .Creature import Creature
from .UI import ui
from ..Function_Lib.General_Functions import get_terminal_confirmation

class Quest():
    def __init__(self, name:str) -> None:
        self.name = name
        self.status = not_taken
        self.target_npc_name = None

    def check_quest_status(self):
        print(self.status)

    def get_quest_status(self):
        return self.status
    
    def set_quest_status(self, status:str):
        self.status = status

    def set_current_npc_name(self, current_npc_name:str):
        self.current_npc_name = current_npc_name

    def get_current_npc_name(self):
        if not self.current_npc_name:
            return None
        return self.current_npc_name

    def set_initial_dialog(self, initial_dialog:str):
        self.initial_dialog = initial_dialog

    def get_initial_dialog(self):
        if not self.initial_dialog:
            return None
        return self.initial_dialog

    def set_quest_rewards(self, quest_rewards:list[Item]):
        self.quest_rewards = quest_rewards

    def get_quest_rewards(self):
        if not self.quest_rewards:
            return None
        return self.quest_rewards

    def set_quest_items(self, quest_item:Item):
        self.quest_item = quest_item

    def get_quest_items(self):
        if not self.quest_item:
            return None
        return self.quest_item

    def accept_quest(self):
        self.set_quest_status(taken)

    def complete_quest(self):
        self.set_quest_status(completed)

    def initiate_quest(self):
        if self.get_quest_status() != not_taken:
            return False
        if get_terminal_confirmation(self.get_initial_dialog()):
            self.accept_quest()
            return True
        return False

    def progress_quest(self):
        return None

class Fetch(Quest):
    def __init__(self, name: str) -> None:
        super().__init__(name)

class Delivery(Quest):
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    def set_recipient_name(self, recipient_name:str):
        self.recipient_name = recipient_name

    def get_recipient_name(self):
        if not self.recipient_name:
            return None
        return self.recipient_name
    
    def set_delivery_dialog(self, dialog:str):
        self.delivery_dialog = dialog

    def get_delivery_dialog(self):
        if not self.delivery_dialog:
            return None
        return self.delivery_dialog

    def progress_quest(self):
        parent_output = super().progress_quest()
        if self.get_current_npc_name() != self.get_recipient_name():
            return 
        if get_terminal_confirmation(self.get_delivery_dialog()):
            self.complete_quest()

    def check_quest_status(self):
        self.check_quest_status()
        if self.get_quest_status() in [not_taken, taken, rewarded]:
            return None
        if self.get_quest_status() == completed:
            self.set_quest_status(rewarded)
            return self.get_quest_rewards() 
        
class Trade(Quest):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def set_requested_pokemon(self, requested_pokemon:Creature):
        self.requested_pokemon = requested_pokemon

    def get_requested_pokemon(self):
        if not self.requested_pokemon:
            return None
        return self.requested_pokemon
    
    def set_given_pokemon(self, given_pokemon:Creature):
        self.given_pokemon = given_pokemon

    def get_given_pokemon(self):
        if not self.given_pokemon:
            return None
        return self.given_pokemon
    
    def check_quest_status(self):
        return super().check_quest_status()

    