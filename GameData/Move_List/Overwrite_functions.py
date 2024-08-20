from ..Keys import hp
from ..Class_lib.AttackType import PhysicalAttack, SpecialAttack, StatusAttack

def get_flail_base_power(self):
    n = self.attacker.get_remaining_hp()
    if n < 5:
        self.base_power = 200
    elif n < 11:
        self.base_power = 150
    elif n < 21:
        self.base_power = 100
    elif n < 36:
        self.base_power = 80
    elif n < 69: # nice
        self.base_power = 40
    else:
        self.base_power = 20
    return self.base_power

def get_counter_base_power(self):
    self.base_power = None
    last_attack = self.target.last_attack
    if type(last_attack) != PhysicalAttack:
        self.print_to_terminal(f'{self.name} failed.')
    elif not last_attack.attributes.get_base_power() or last_attack.attributes.get_base_power() == 0:
        self.print_to_terminal(f'{self.name} failed.')
    else:
        self.set_base_power(last_attack.attributes.get_base_power() * 2) 

def false_swipe_damage_cap(self, damage:int):
    if self.target.active_value[hp] > damage:
            return damage
    return int(self.target.active_value[hp] - 1)

def miss_if_not_first_turn(self):
    if self.target.moved:
        text = f'{self.name} Failed!'
        self.print_to_terminal(text)
        return False
    return True

