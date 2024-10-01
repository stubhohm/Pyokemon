from ..Class_lib.NPC import NPC
from ..Class_lib.Quests import Quest, Trade, Delivery, Fetch, Gift
from ..Item_List.ItemsList import make_potion, make_mail

def test_recipient():
    npc = NPC('recipient')
    npc.set_position((15,15))
    return npc
    
def test_woman():
    quest = Delivery()
    rewards = []
    for i in range(5):
        rewards.append(make_potion())
    quest_item = make_mail()
    name = 'Potions from Oldale Woman'
    tgt_npc = 'recipient'
    quest.define(name, tgt_npc, 'Start Quest dlg', 'End Quest dlg', quest_item, rewards)
    npc = NPC('Oldale_Woman')
    npc.set_quest(quest)
    npc.set_position((10,10))
    return npc