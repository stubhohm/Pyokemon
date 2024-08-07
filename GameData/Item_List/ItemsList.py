from ..Keys import potion, super_potion, hyper_potion, max_potion
from ..Keys import pokeball, greatball, ultraball, masterball
from ..Keys import antidote, burnheal, awakening, paralyzeheal, iceheal
from ..Keys import status_item_dict
from ..Keys import burned, badly_poisoned, poisoned, frozen, paralysis, asleep, confused
from ..Class_lib.Item import Item, HealingItem, StatusItem, CaptureItem, KeyItem


# Healing Items
def make_potion():
    item =  HealingItem(potion, 1, 'Restores 20 hp to a Pokemon')
    item.set_buy_sell(300, 150)
    return item

def make_super_potion():
    item =  HealingItem(super_potion, 1, 'Restores 50 hp to a Pokemon')
    item.set_buy_sell(700, 350)
    return item

def make_hyper_potion():
    item =  HealingItem(hyper_potion, 1, 'Restores 200 hp to a Pokemon')
    item.set_buy_sell(1500, 750)
    return item

def make_max_potion():
    item = HealingItem(max_potion, 1, 'Fully restores a Pokemons HP')
    item.set_buy_sell(2500, 1250)
    return item

# Status Items
def make_antidote():
    item_name = antidote
    item = StatusItem(item_name, 1, 'Removes the poisoned status from a Pokemon')
    item.set_buy_sell(100, 50)
    statuses = status_item_dict[item_name]
    item.removed_statuses(statuses)
    return item

def make_burnheal():
    item_name = burnheal
    item = StatusItem(item_name, 1, 'Removes the burned status from a Pokemon')
    item.set_buy_sell(200, 100)
    statuses = status_item_dict[item_name]
    item.removed_statuses(statuses)
    return item

def make_iceheal():
    item_name = iceheal
    item = StatusItem(item_name, 1, 'Removes the frozen status from a Pokemon')
    item.set_buy_sell(250, 125)
    statuses = status_item_dict[item_name]
    item.removed_statuses(statuses)
    return item

def make_paralyzeheal():
    item_name = paralyzeheal
    item = StatusItem(item_name, 1, 'Removes the paralysis status from a Pokemon')
    item.set_buy_sell(250, 125)
    statuses = status_item_dict[item_name]
    item.removed_statuses(statuses)
    return item

def make_awakening():
    item_name = awakening
    item = StatusItem(item_name, 1, 'Removes the asleep status from a Pokemon')
    item.set_buy_sell(250, 125)
    statuses = status_item_dict[item_name]
    item.removed_statuses(statuses)
    return item

# Capture Items
def make_pokeball():
    item = CaptureItem(pokeball, 1, 'A tool for catching wild Pokemon')
    item.set_ball_multipler(1)
    item.set_buy_sell(200, 100)
    return item

def make_greatball():
    item = CaptureItem(greatball, 1, 'A good ball with a higher catchrate than a PokeBall')
    item.set_ball_multipler(1.5)
    item.set_buy_sell(600, 300)
    return item

def make_ultraball():
    item = CaptureItem(ultraball, 1, 'A ball with a high rate of success')
    item.set_ball_multipler(1.5)
    item.set_buy_sell(1200, 600)
    return item

def make_masterball():
    item = CaptureItem(greatball, 1, 'The best ball. It never misses.')
    item.set_ball_multipler(255)
    return item