from ..Keys import attack, sp_attack, defense, sp_defense, speed
from ..Keys import name
from ..Keys import increase, decrease
from ..Function_Lib.General_Functions import random

hardy  = {increase : None,       decrease : None,       name : 'hardy'}
lonely  = {increase : attack,     decrease : defense,    name: 'lonely'}
brave   = {increase : attack,     decrease : speed,      name : 'brave'}
adamant = {increase : attack,     decrease : sp_attack,  name : 'adamant'}
naugty  = {increase : attack,     decrease : sp_defense, name : 'naughty'}
bold    = {increase : defense,    decrease : attack,     name : 'bold'}
docile  = {increase : None,       decrease : None,       name : 'docile'}
relaxed = {increase : defense,    decrease : speed,      name : 'relaxed'}
impish  = {increase : defense,    decrease : sp_attack,  name : 'impish'}
lax     = {increase : defense,    decrease : sp_defense, name : 'lax'}
timid   = {increase : speed,      decrease : attack,     name : 'timid'}
hasty   = {increase : speed,      decrease : defense,    name : 'hasty'}
serious = {increase : None,       decrease : None,       name : 'serious'}
jolly   = {increase : speed,      decrease : sp_attack,  name : 'jolly'}
naive   = {increase : speed,      decrease : sp_defense, name : 'naive'}
modest  = {increase : sp_attack,  decrease : attack,     name : 'modest'}
mild    = {increase : sp_attack,  decrease : defense,    name : 'mild'}
quiet   = {increase : sp_attack,  decrease : speed,      name : 'quiet'}
bashful = {increase : None,       decrease : None,       name : 'bashful'}
rash    = {increase : sp_attack,  decrease : sp_defense, name : 'rash'}
calm    = {increase : sp_defense, decrease : attack,     name : 'calm'}
gentile = {increase : sp_defense, decrease : defense,    name : 'gentile'}
sassy   = {increase : sp_defense, decrease : speed,      name : 'sassy'}
careful = {increase : sp_defense, decrease : sp_attack,  name : 'careful'}
quirky  = {increase : None,       decrease : None,       name : 'quirky'}

natures = [hardy, lonely, brave, adamant, naugty, 
           bold, docile, relaxed, impish, lax,
           timid, hasty, serious, jolly, naive, 
           modest, mild, quiet, bashful, rash,
           calm, gentile, sassy, careful, quirky]
natures_count = len(natures)

def pick_random_nature():
    rand_int = random.randrange(0, natures_count - 1)
    rand_nature = natures[rand_int]
    return rand_nature