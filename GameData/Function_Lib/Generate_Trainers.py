from ..Creatures.Wurmple_Line.Full import instance_wurmple, instance_cascoon, instance_silcoon, instance_dustox, instance_beautifly
from ..Class_lib.Inventory import Inventory
from ..Class_lib.ActorBattleInfo import ActorBattleInfo
from ..Keys import npc

def generate_bug_trainers():
    trainer_1 = ActorBattleInfo()
    trainer_2 = ActorBattleInfo()
    trainer_3 = ActorBattleInfo()
    trainer_4 = ActorBattleInfo()
    roster = [instance_wurmple(4), instance_wurmple(4), instance_wurmple(8)]
    trainer_1.define_battle_info(roster, Inventory(), npc, 'Bug Catcher Jimmy')
    roster = [instance_wurmple(4), instance_cascoon(12), instance_silcoon(12)]
    trainer_2.define_battle_info(roster, Inventory(), npc, 'Bug Catcher Rick')
    roster = [instance_wurmple(4), instance_beautifly(13)]
    trainer_3.define_battle_info(roster, Inventory(), npc, 'Bug Master John')
    roster = [instance_wurmple(4), instance_dustox(13)]
    trainer_4.define_battle_info(roster, Inventory(), npc, 'Bug Master Alan')
    return [trainer_1, trainer_2, trainer_3, trainer_4]

