from ..Modules.External_Modules import random
from ..Class_lib.UI import ui
from ..Colors import black
from ..Constants import terminal_font_size
from ..Keys import wild, npc
from ..Keys import select, cancel
from ..Keys import erratic, fast, medium_fast, medium_slow, slow, fluctuating

def get_sign(value:int):
    sign = value/ abs(value)
    return sign

def rand31():
    '''
    Returns a random number between 0 and 31.
    '''
    value = random.randrange(0,31)
    return value

def rand100():
    '''
    Returns a random number between 1 and 100.
    '''
    value = random.randrange(1,100)
    return value

def rand256():
    '''
    Returns a random number between 1 and 256.
    '''
    value = random.randrange(1,256)
    return value

def rand85_100():
    '''
    Returns a random number between 85 and 100.
    '''
    value = random.randrange(85,100)
    return value

def rand_16bit():
    value = random.randrange(0,65535)
    return value

def erractic_leveling(level:int):
    '''
    Formula for erratic leveling.
    '''
    levels = [level, level + 1]
    caps:list[int] = []
    for level in levels:
        level_to_3rd = (level * level * level)
        if level < 50:
            numerator = (100 - level)
            denominator = 50
        elif 50 <= level < 68:
            numerator = (150 - level)
            denominator = 100
        elif 68 <= level < 98:
            numerator = ((1911 - (10 * level)) / 3)
            denominator = 500
        else:
            numerator = (160 - level)
            denominator = 100
        cap = int((level_to_3rd * numerator) / denominator)
        caps.append(cap)
    current_floor, next_level = caps[0], caps[1]
    return current_floor, next_level

def fast_leveling(level:int):
    '''
    Formula for fast leveling.
    '''
    level_1 = level + 1
    current_floor = int(4 * (level * level * level) / 5)
    next_level = int(4 * (level_1 * level_1 * level_1) / 5)
    return current_floor, next_level

def medium_fast_leveling(level:int):
    '''
    Formula for medium fast leveling.
    '''
    level_1 = level + 1
    current_floor = (level * level * level)
    next_level = (level_1 * level_1 * level_1)
    return current_floor, next_level

def medium_slow_leveling(level:int):
    '''
    Formula for medium slow leveling.
    '''
    level_1 = level + 1
    current_floor = int((6/5 *(level * level * level)) - (15 * level * level) + (100 * level) - 140)
    next_level = int((6/5 *(level_1 * level_1 * level_1)) - (15 * level_1 * level_1) + (100 * level_1) - 140)
    return current_floor, next_level

def slow_leveling(level:int):
    '''
    Formula for slow leveling.
    '''
    level_1 = level + 1
    current_floor = int(5 * (level * level * level) / 4)
    next_level = int(5 * (level_1 * level_1 * level_1) / 4)
    return current_floor, next_level

def fluctuating_leveling(level:int):
    '''
    Formula for fluctuating leveling.
    '''
    levels = [level, level + 1]
    caps:list[int] = []
    for level in levels:
        level_to_3rd = (level * level * level)
        denominator = 50
        if level < 15:
            numerator = (((level + 1) / 3) + 24)
        elif 15 <= level < 36:
            numerator = (level + 14)
        else:
            numerator = ((level / 2) + 32)
        cap = int((level_to_3rd * numerator) / denominator)
        caps.append(cap)
    current_floor, next_level = caps[0], caps[1]
    return current_floor, next_level

def convert_level_to_exp_caps(leveling_speed:str, level:int):
    '''
    Switch function for leveling.
    '''
    leveling_dict = {erratic: erractic_leveling,
                     fast : fast_leveling,
                     medium_fast : medium_fast_leveling,
                     medium_slow : medium_slow_leveling,
                     slow : slow_leveling, 
                     fluctuating : fluctuating_leveling}
    current_floor, next_level = leveling_dict[leveling_speed](level)
    return current_floor, next_level

def get_terminal_confirmation(text):
    ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)
    while True:
        input_value = ui.input.get_player_input()
        if input_value == select:
            return True
        elif input_value == cancel:
            return False

def get_confirmation(text):
    '''
    Takes a question as an input and returns True for yes/y and False for no/n.
    '''
    response = ''
    char = ''
    text = text + '(y/n): '
    while len(response) == 0 or char not in ('y','n'):
        response = input(text).strip().lower()
        try:
            char = response[0]
        except IndexError:
            pass
        if not (len(response) == 0) and (char not in ('y','n')):
            print("Please respond with a yes or no.")
    if char == 'y':
        return True
    else:
        return False
    
def try_again():
    return get_confirmation('Would you like to try again?')