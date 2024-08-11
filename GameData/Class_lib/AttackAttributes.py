
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