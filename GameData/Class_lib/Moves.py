from ..Modules.External_Modules import call_flip
from ..Constants import terminal_font_size
from ..Colors import black
from ..Keys import moves as moves_str, cancel, select
from .Attack import Attack
from ..Function_Lib.General_Functions import get_confirmation, try_again, get_terminal_confirmation
from .UI import ui


class Moves ():
    def __init__(self) -> None:
        self.instance_moves()

    def end_battle(self):
        for move in self.move_list:
            if not move:
                continue
            move.reset_accuracy()
            move.reset_bp()
            move.consecutive_success = 0

    def print_moves(self):
        for i, move in enumerate(self.move_list):
            if not move:
                continue
            print(f'{i + 1}: {move.name}')
            print(f'  PP: {move.attributes.points}\n  Type: {move.attributes.element}')

    def get_moves_list(self):
        move_names = []
        for moves in self.move_list:
            if not moves:
                continue
            else:
                move_names.append(moves.name)
        return move_names

    def full_restore_pp(self):
        for move in self.move_list:
            if not move:
                continue
            move.attributes.points = move.attributes.pp_max

    def print_to_terminal(self, text:str):
        ui.display.active.battle_terminal.slow_print(text, terminal_font_size, black)

    def instance_moves(self):
        self.move_1:Attack = None
        self.move_2:Attack = None
        self.move_3:Attack = None
        self.move_4:Attack = None
        self.move_list = [self.move_1, self.move_2, self.move_3, self.move_4]

    def evolve_moves(self, evolution):
        moves:Moves = evolution.moves
        moves.set_moves(self.move_list)
        return moves

    def replace_move(self, index:int, new_move:Attack):
        if index == 0:
            self.move_1 = new_move
        elif index == 1:
            self.move_2 = new_move
        elif index == 2:
            self.move_3 = new_move
        else:
            self.move_4 = new_move
        self.print_moves()
        self.update_known_moves()
        self.print_moves()

    def update_known_moves(self):
        self.move_list = [self.move_1, self.move_2, self.move_3, self.move_4]

    def set_moves(self, move_list:list[Attack]):
        self.move_1 = move_list[0]
        self.move_2 = move_list[1]
        self.move_3 = move_list[2]
        self.move_4 = move_list[3]
        self.move_list = [self.move_1, self.move_2, self.move_3, self.move_4]

    def define_moves(self, breeding:list, training:list, level_up:list[list]):
        self.define_breeding_moves(breeding)
        self.define_levelup_moves(level_up)
        self.define_training_moves(training)

    def define_breeding_moves(self, breeding_moves:list):
        self.breeding_moves = breeding_moves
    
    def define_training_moves(self, training_moves:list):
        self.training_moves = training_moves

    def define_levelup_moves(self, levelup_moves:list[list]):
        self.levelup_moves = levelup_moves

    def select_move(self):
        selected_move = None
        terminal = ui.display.active.battle_terminal
        moves_list = self.get_moves_list()
        terminal.define_list(moves_list, 2)
        terminal.mode = moves_str
        while True:
            ui.display.active.update()
            input_value = ui.input.get_player_input()
            output = terminal.use_combat_terminal(input_value)
            if output == cancel:
                return output
            if not output:
                continue
            for move_item in self.move_list:
                if not move_item:
                    continue
                if move_item.name == output:
                    selected_move = move_item
            if not selected_move:
                return cancel 
            return selected_move

    def try_learn(self, new_move:Attack, name:str):
        print('Known moves:')
        for move in self.move_list:
            print(move.name)
            if not move:
                continue
        terminal = ui.display.active.battle_terminal
        text = f'Which move would you like to replace with {new_move.name}?'
        self.print_to_terminal(text)
        terminal.define_list(self.get_moves_list(), 2)
        terminal.mode = moves_str
        while True:
            output = self.select_move()
            if output == cancel:
                text = f'Stop trying to learn {new_move.name}?'
                if get_terminal_confirmation(text):
                    break
                text = f'Which move would you like to replace with {new_move.name}?'
                self.print_to_terminal(text)
                continue
            if not output:
                continue
            if output == select:
                continue
            text = f'Replace {output.name} with {new_move.name}?'
            if not get_terminal_confirmation(text):
                text = f'Which move would you like to replace with {new_move.name}?'
                self.print_to_terminal(text)
                continue
            text = f'{name} forgot {output.name} and learned {new_move.name}!'
            self.print_to_terminal(text)
            print(text)
            for i, moves in enumerate(self.move_list):
                if output == moves.name:
                    break
            self.replace_move(i, new_move)
            return True
        return False

    def determine_if_move_is_new(self, move:Attack):
        if not move:
            print('not move')
            return False
        new_move:Attack = move()
        for moves in self.move_list:
            if not moves:
                print('not move')
                break
            if new_move.name == moves.name:
                print('already known')
                return False
        return new_move

    def learn_via_levelup(self, start_level:int, current_level:int, name:str):
        learn_list = self.levelup_moves[start_level + 1:current_level + 1]
        for level_learned_list in learn_list:
            print('')
            if not level_learned_list:
                continue
            for move in level_learned_list:
                learned = False
                new_move = self.determine_if_move_is_new(move)
                if not new_move:
                    continue
                text = f'{name} is trying to learn {new_move.name}!'
                self.print_to_terminal(text)
                print(text)
                for i, viable_move in enumerate(self.move_list):
                    if not viable_move:
                        text = f'{name} learned {new_move.name}!'
                        self.print_to_terminal(text)
                        print(text)
                        print(i, new_move.name)
                        self.replace_move(i, new_move)
                        self.print_moves()
                        learned = True
                        break  
                if learned:
                    continue
                text = f'Would you like to replace an existing move with {new_move.name}?'
                self.print_to_terminal(text)
                if not get_terminal_confirmation(text):
                    continue
                learned = self.try_learn(new_move, name)

    def rotate_in_new_move(self, new_move:Attack):
        self.move_4 = self.move_3
        self.move_3 = self.move_2
        self.move_2 = self.move_1
        self.move_1 = new_move
        self.update_known_moves()

    def learn_on_instance(self, level:int):
        '''
        Learns moves from levelup without prompting player up to current level.
        '''
        learned_level_list = self.levelup_moves
        for level in range(level):
            level_moves = learned_level_list[level]
            if not level_moves:
                continue
            for move in level_moves:
                if not move:
                    continue
                new_move = move()
                self.rotate_in_new_move(new_move)
