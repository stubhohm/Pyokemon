from ..Class_lib.Quests import Delivery, Fetch, Trade
from ..Item_List.ItemsList import Item, make_potion

def define_delivery(quest_name:str, recipient_name:str, initial_dialog:str, delivery_dialog:str, delivery_item:Item, rewards:list[Item]):
    quest = Delivery(quest_name)
    quest.set_initial_dialog(initial_dialog)
    quest.set_delivery_dialog(delivery_dialog)
    quest.set_quest_items(delivery_item)
    quest.set_quest_rewards(rewards)
    quest.set_recipient_name(recipient_name)
    return quest

def old_dale_woman_quest():
    quest_name = 'Oldale Potion Quest'
    recipient_name = 'Oldale Woman'
    initial_dialog = 'initial'
    delivery_dialog = 'delivered final'
    delivery_item = None
    rewards = []
    for i in range(3):
        rewards.append(make_potion())
    return define_delivery(quest_name, recipient_name, initial_dialog, delivery_dialog, delivery_item, rewards)