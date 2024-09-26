from ..Class_lib.NPC import NPC
from ..Class_lib.Quests import Quest, Trade, Delivery, Fetch, Gift
from ..Item_List.ItemsList import make_potion


def oldale_woman():
    quest = Gift('Potions from Oldale Woman')
    rewards = []
    for i in range(5):
        rewards.append(make_potion())
    quest.set_quest_rewards(rewards)
    quest.set_initial_dialog('Being a trainer is tough, have some potions!')
    quest.set_completed_dialog('I hope those potions work well for you!')
    npc = NPC('Oldale_Woman')
    npc.set_quest(quest)
    npc.set_position((10,10))
    return npc