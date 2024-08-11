from ..Constants import trianer_battles_off, gymleader_battles_off
from ..Keys import no_weather, hp
from ..Function_Lib.General_Functions import try_again, get_confirmation
from .ActorBattleInfo import ActorBattleInfo
from .Battle import Battle



class LocalTrainers():
    def __init__(self) -> None:
        self.trainers:list[ActorBattleInfo] = []
        self.gym_leader:ActorBattleInfo = None
        self.is_gym = False

    def add_trainer(self, trainer:ActorBattleInfo):
        self.trainers.append(trainer)
    
    def set_gym_leader(self, gym_leader:ActorBattleInfo):
        self.gym_leader = gym_leader
        self.is_gym = True

    def get_viable_trainers(self):
        viable_trainers:list[ActorBattleInfo] = []
        for trainer in self.trainers:
            white_out = True
            for creature in trainer.roster:
                if creature.stats.active_value[hp] > 0:
                    white_out = False
            trainer.white_out = white_out
            if trainer.white_out:
                continue
            else:
                viable_trainers.append(trainer)
        return viable_trainers

    def print_viable_trainers(self, viable_trainers:list[ActorBattleInfo]):
        print('\n Available Trainers:')
        for i, trainer in enumerate(viable_trainers):
            print(f'{i+1}: {trainer.name}')
        print('')

    def engage_leader(self, player:ActorBattleInfo):
        if gymleader_battles_off:
            print('gym leader battles are toggled off')
            return
        print('')
        if self.gym_leader.white_out:
            print('You have defeated the leader already.')
        elif len(self.get_viable_trainers()) == 0:
            text = f'Would you like to battle {self.gym_leader.name}?'
            if get_confirmation(text):
                self.conduct_battle(self.gym_leader, player)
        else:
            print('You need to defeat all the trainers before taking on the leader.')
            if get_confirmation('Would you like to battle a trainer instead?'):
                self.engage_trainer(player)

    def engage_trainer(self, player:ActorBattleInfo):
        if trianer_battles_off:
            print('trainer battles are toggled off')
            return
        if self.is_gym and self.gym_leader.white_out:
            print('\nYou have defeated everyone in the area already.')
            return None
        viable_trainers = self.get_viable_trainers()
        if len(viable_trainers) == 0:
            print('\nYou have beaten all trainers in the area.')
            if self.is_gym and get_confirmation('Would you like to challenge the leader?'):
                self.engage_leader(player)
        target_trainer = self.search_for_trainer()
        if target_trainer:
            self.conduct_battle(target_trainer, player)

    def conduct_battle(self, trainer:ActorBattleInfo, player:ActorBattleInfo):
        print('')
        battle = Battle()
        battle.define_battle_start(player, [trainer], no_weather)
        battle.battle_loop()

    def get_matching_trainer(self, response:str, viable_trainers:list[ActorBattleInfo]):
        '''
        Returns a matching trainer by name or number or none if not found.
        '''
        selected_trainer = None
        for i, trainer in enumerate(viable_trainers):
            i_str = str(i+1)
            trainer_name = trainer.name.strip().lower()
            if response in trainer_name or i_str == response:
                selected_trainer = trainer
                break
        return selected_trainer

    def search_for_trainer(self):
        '''
        Gets viable trainers, prints, viable trainers, gets player input, and finds a match.
        '''
        viable_trainers = self.get_viable_trainers()
        if len(viable_trainers) == 0:
            text = 'There are no trainers that can battle here.'
            return None
        pending_response = True
        while pending_response:
            self.print_viable_trainers(viable_trainers)
            response = input('Who would you like to battle?: ').strip().lower()
            trainer = self.get_matching_trainer(response, viable_trainers)
            if not trainer:
                print(f'Your input of: {response} did not match an available trainer.')
                if try_again():
                    continue
                else:
                    return None
            text = f'You have selected to battle {trainer.name}. Is this correct?'
            if get_confirmation(text):
                return trainer
            else:
                if try_again():
                    continue
                else:
                    return None