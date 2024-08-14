
class AttackAttributes():
    def __init__(self, element:str, base_power:int, points:int, accuracy:int, crit:int, target:str, type:str, contact:bool):
        self.element = element
        self.base_power = base_power
        self.points = points
        self.pp_max = int(points)
        self.accuracy = accuracy
        self.crit = crit
        self.target = target
        self.type = type
        self.contact = contact
        self.priority = 0

    def get_base_power(self):
        return self.base_power
    
    def set_base_power(self, value:int):
        self.base_power = value

    def set_attacker(self, attacker):
        self.attacker = attacker