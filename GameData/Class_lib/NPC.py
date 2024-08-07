from .Creature import Creature

class NPC():
    def __init__(self, name:str) -> None:
        self.set_name(name)

    def set_name(self, name:str):
        self.name = name

    def set_trade(self, requesting:Creature, offering:Creature):
        self.trading = True
        self.requested_pokemon = requesting
        self.offering_pokemon = offering
