from ..Class_lib.Attack import Attack
from ..Keys import special, physical, status
from ..Keys import fire, ice, water, electric, dragon, normal 
from ..Keys import base_crit

class SpecialAttack(Attack):
    def __init__(self, name:str, target:str, element:str, base_power:int, points:int, accuracy:int):
        type = special
        crit = base_crit
        contact = False
        super().__init__(name, element, base_power, points, accuracy, crit, target, type, contact)

class PhysicalAttack(Attack):  
    def __init__(self, name:str, target:str, element:str, base_power:int, points:int, accuracy:int):
        type = physical
        contact = True
        crit = base_crit
        super().__init__(name, element, base_power, points, accuracy, crit, target, type, contact)

class StatusAttack(Attack):  
    def __init__(self, name:str, target:str, element:str, points:int, accuracy:int):
        type = status
        contact = False
        super().__init__(name, element, 0, points, accuracy, 0, target, type, contact)
