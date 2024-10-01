from ..Keys import not_taken, taken, completed, rewarded
from .Item import Item
from .Creature import Creature
from .UI import ui
from ..Function_Lib.General_Functions import get_terminal_confirmation

class Quest():
    def __init__(self) -> None:
        self.name = 'unnamed quest'
        self.status = not_taken
        self.target_npc_name = None
        self.quest_item = None
        self.quest_rewards = [None]

    def define(self, name:str, target_npc:str, initial_dialog:str, quest_item:Item, rewards:list[Item]):
        self.name = name
        self.target_npc_name = target_npc
        self.set_initial_dialog(initial_dialog)
        self.set_quest_items(quest_item)
        self.set_quest_rewards(rewards)

    def check_quest_status(self):
        if self.get_quest_status() in [not_taken, taken, rewarded]:
            return None
        if self.get_quest_status() == completed:
            self.set_quest_status(rewarded)
            return self.get_quest_rewards() 

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

    def reward_claimed(self):
        self.set_quest_rewards([None])
        self.set_quest_status(rewarded)

    def initiate_quest(self):
        if self.get_quest_status() != not_taken:
            return False
        if get_terminal_confirmation(self.get_initial_dialog()):
            self.accept_quest()
            return True
        return False

    def progress_quest(self):
        '''Returns True if the quest is completed or rewarded.'''
        if self.get_quest_status() in [completed, rewarded]:
            return True
        else:
            return False

class Fetch(Quest):
    def __init__(self) -> None:
        super().__init__()

class Delivery(Quest):
    def __init__(self) -> None:
        super().__init__()
    
    def define(self, name:str, target_npc:str, initial_dialog:str, delivery_dialog:str, quest_item: Item, rewards: list[Item]):
        super().define(name, target_npc, initial_dialog, quest_item, rewards)
        self.set_recipient_name(target_npc)
        self.set_delivery_dialog(delivery_dialog)

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
        if super().progress_quest():
            return
        if self.get_current_npc_name() != self.get_recipient_name():
            return 
        if get_terminal_confirmation(self.get_delivery_dialog()):
            self.complete_quest()
            self.quest_item.use_item(None)
            return self.get_quest_rewards()
        
class Trade(Quest):
    def __init__(self) -> None:
        super().__init__()

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

class Gift(Quest):
    def __init__(self) -> None:
        super().__init__()
        self.completed_dialog = 'undefined'

    def define(self, name:str, target_npc: str, initial_dialog: str,  completed_dialog:str, quest_item: Item, rewards: list[Item]):
        super().define(name, target_npc, initial_dialog, quest_item, rewards)
        self.set_completed_dialog(completed_dialog)

    def set_completed_dialog(self, dialog:str):
        self.completed_dialog = dialog

    def get_completed_dialog(self):
        return self.completed_dialog

    def progress_quest(self):
        if self.get_quest_status() in [completed, rewarded]:
            get_terminal_confirmation(self.get_completed_dialog())
        self.complete_quest()
        return self.get_quest_rewards()