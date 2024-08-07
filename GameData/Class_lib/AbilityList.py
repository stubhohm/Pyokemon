from ..Constants import name, description, type, modifier, is_active

class AbilityList ():
    def __init__(self) -> None:
        pass

full_ability_dict = {}

# Format for making ability
ability  = {name: 'name',
            description: 'Abilitity Description',
            type: 'unsure of the categories right now', 
            modifier:'stat it impacts',
            is_active: 'True if always on, or False if it needs to be activated'}

#Ability names as variables
air_lock = 'Air Lock'
ab_air_lock = {name: air_lock, 
            description: 'While this Pokemon is in battle, all weather effects are negated', 
            type: '?combat ability?', 
            modifier: None,
            is_active: True}
full_ability_dict[air_lock] = ab_air_lock



