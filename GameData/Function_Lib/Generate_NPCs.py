from ..Class_lib.NPC import NPC
from ..Class_lib.Quests import Quest, Trade, Delivery, Fetch, Gift
from ..Item_List.ItemsList import make_potion, make_mail
from ..Creatures.Wurmple_Line.Full import instance_wurmple, instance_beautifly

def test_recipient():
    npc = NPC('recipient')
    npc.set_position((15,15))
    return npc
    
def test_woman():
    quest = Trade()
    rewards = []
    for i in range(5):
        rewards.append(make_potion())
    quest_item = make_mail()
    name = 'test trade'
    tgt_npc = 'recipient'
    initial_dlg = 'initial'
    trd_dlg = 'trade for wumple'
    request = instance_wurmple(3)
    given = instance_beautifly(3)

    npc = NPC('Oldale_Woman')
    npc.set_position((10,10))  

    quest.define(name, npc.name, initial_dlg, trd_dlg, request, given)

    npc.set_quest(quest)
    return npc