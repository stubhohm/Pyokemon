from ..Keys import hp


def get_flail_base_power(self):
    n = self.attacker.get_remaining_hp()
    print(f'n: {n}')
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