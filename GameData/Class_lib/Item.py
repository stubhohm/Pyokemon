from ..Keys import paralysis, poisoned, burned, frozen, confused, badly_poisoned, asleep
from ..Keys import hp, defense, sp_defense, attack, sp_attack, speed
from ..Keys import accuracy, evasion
from ..Keys import unnamed
from ..Keys import healing_item_dict
from ..Modules.External_Modules import math, time
from ..Function_Lib.General_Functions import rand_16bit

class Item():
    def __init__(self) -> None: 
        self.name = unnamed
        self.quantity = 0
        self.description = 'No Description'
        self.is_key = False
        self.is_unlimited_use = False
        self.buy = None
        self.sell = None

    def define_item(self, name:str, quantity:int, description:str):
        self.name = name
        self.quantity = quantity
        self.description = description
        self.is_key = False
        self.is_unlimited_use = False

    def item_is_key(self):
        self.is_key = True

    def item_is_unlimited_use(self):
        self.is_unlimited_use = True
    
    def consume_item(self):
        if self.is_unlimited_use:
            return
        if self.quantity > 0:
            self.quantity -= 1
        return
        
    def use_item(self, target):
        self.consume_item()

    def set_buy_sell(self, buy:int, sell:int):
        self.buy, self.sell = buy, sell

class HealingItem(Item):
    def __init__(self, name:str, quantity:int, description:str) -> None:
        super().__init__()
        self.define_item(name, quantity, description)
        self.set_healing_ammount()
    
    def set_healing_ammount(self):
        ammount_healed = healing_item_dict[self.name]
        self.ammount_healed = ammount_healed

    def use_item(self, target):
        start_hp = target.stats.active_value[hp]
        super().consume_item()
        target.stats.change_hp(self.ammount_healed)
        current = target.stats.active_value[hp]
        difference = current - start_hp
        text = f"{target.name}'s hp was increased by {difference} from {start_hp} to {current}."
        
class StatusItem(Item):
    def __init__(self, name:str, quantity:int, description:str) -> None:
        super().__init__()
        self.define_item(name, quantity, description)

class CaptureItem(Item):
    def __init__(self, name:str, quantity:int, description:str) -> None:
        super().__init__()
        self.define_item(name, quantity, description)
        self.num_of_shakes = 3

    def set_ball_multipler(self, value:float):
        self.ball_multipler = value

    def get_status_bonus(self, target):
        if not target.stats.status.is_active:
            return 1
        elif target.stats.status.name in [asleep, frozen]:
            return 2
        elif target.stats.status.name in [paralysis, poisoned, badly_poisoned, burned]:
            return 1.5
        else:
            return 1

    def set_player(self, player):
        self.player = player
    
    def clear_player(self):
        self.player = None

    def get_catch_rate(self, target):
        hp_current:int = target.stats.active_value[hp]
        hp_max:int = target.stats.active_max[hp]
        rate:int = target.catch_rate
        bonus_status:int|float = self.get_status_bonus(target)
        hp_mod:float = ((3 * hp_max) - (2 * hp_current))/(3 * hp_max)
        a = int(hp_mod * rate * self.ball_multipler *  bonus_status)
        return a

    def shake_success(self, catch_rate:int):
        rng = rand_16bit()
        denominator = int(math.sqrt(int(math.sqrt(int(16711680 / catch_rate)))))
        b = 1048560 / denominator
        if rng >= b:
            return False
        else:
            return True

    def use_item(self, target):
        super().consume_item()
        capture = True
        a = self.get_catch_rate(target)
        for shakes in range(self.num_of_shakes):
            time.sleep(1)
            if self.shake_success(a):
                print('~shake~')
            else:
                capture = False
                text = f'{target.name} broke free!'
                break   
        if capture:
            time.sleep(1)
            text = f'You captured {target.name}'
            self.player.add_pokemon_to_roster(target)
        target.captured = capture
        self.clear_player()

class StatusItem(Item):
    def __init__(self, name:str, quantity:int, description:str) -> None:
        super().__init__()
        self.define_item(name, quantity, description)
        self.healing = None

    def removed_statuses(self, statuses:list[str]):
        self.statuses = statuses

    def set_healing_ammount(self, ammount:int):
        self.healing = ammount

    def heal_target(self, target):
        start_hp = target.stats.active_value[hp]
        target.stats.change_hp(self.ammount_healed)
        current = target.stats.active_value[hp]
        difference = current - start_hp
        text = f"{target.name}'s hp was increased by {difference} to {current}."

    def use_item(self, target):
        super().consume_item()
        if not target.stats.status.is_active:
            return
        if target.stats.status.name in self.statuses:
            text = f'{self.name} removed {target.stats.status.name} from {target.name}.'
            target.stats.status.remove_status()   
        if self.healing:
            self.heal_target(target)

class KeyItem(Item):
    def __init__(self, name:str, quantity:int, description:str) -> None:
        super().__init__()
        self.define_item(name, quantity, description)
        self.item_is_key()

class UseItem(Item):
    def __init__(self, name:str, quantity:int, description:str) -> None:
        super().__init__()
        self.define_item(name, quantity, description)
        self.item_is_unlimited_use()