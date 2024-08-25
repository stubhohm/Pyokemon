from ..Constants import screen_size, terminal_font_size
from ..Colors import black, grey, red, white, brown
from ..Modules.External_Modules import pygame, Surface, Rect, time
from .SpriteTools import SpriteTools
from ..Keys import up, down, left, right, directional_inputs
from ..Keys import fight, run, swap, item, combat_inputs
from ..Keys import select, cancel
from ..Keys import default, moves, output_info
from .Text import Text
from .Input import Input


valid_inputs = [up, down, left, right, select, cancel]

class BattleTerminal():
    def __init__(self) -> None:
        self.scale:tuple[int,int] = (0,0)
        self.text:Text = Text()
        self.current_selection = None
        self.active_grid:list = None
        self.margin = 3
        self.sprite:Surface = None
        self.name:str = ''
        self.sprite_tools = SpriteTools()
        self.mode:str = default
        self.input:Input = Input()

    def create_terminal(self, parent_surface:Surface):
        width = screen_size[0]
        height = screen_size[1]
        self.width = width
        self.height = height * 5 / 16
        self.scale = (self.width, self.height)
        self.set_corner()
        self.sprite = Surface((self.width, self.height))
        self.parent_surface = parent_surface
    
    def set_active_name(self, active_name:str):
        self.name = active_name

    def set_corner(self):
        self.x = 0
        self.y = screen_size[1] - self.height

    def define_grid(self, input_list:list, columns):
        grid = []
        row = []
        for i, item in enumerate(input_list):
            row.append(item)
            if (i + 1) % columns == 0:
                grid.append(row)
                row = []
        if len(row) > 0:
            grid.append(row)
        return grid

    def get_position(self):
        for i, row in enumerate(self.active_grid):
            for j, column in enumerate(row):
                entry = self.active_grid[i][j]
                if entry != self.current_selection:
                    continue
                else:
                    return i , j
        return None, None

    def get_selection(self):
        i, j = self.get_position()
        return self.active_grid[i][j]

    def change_cursor_location(self, input_value:str):
        column_len = len(self.active_grid)
        row_len = len(self.active_grid[0])
        column, row = self.get_position()
        if type(row) != int:
            return 0, 0
        if type(column) != int:
            return 0, 0
        if input_value == up:
            row = (row - 1) % row_len
        elif input_value == down:
            row = (row + 1) % row_len
        elif input_value == left:
            column = (column - 1) % column_len
        elif input_value == right:
            column = (column + 1) % column_len
        return column, row
        
    def select_item(self, input_value:str):
        grid = self.active_grid
        if not self.current_selection:
            self.current_selection = grid[0][0]
        if input_value in directional_inputs:
            row, column = self.change_cursor_location(input_value)
            if not row:
                return None
            if not column:
                return None
            self.current_selection = grid[row][column]
        elif input_value == select:
            self.current_selection = select
        elif input_value == cancel:
            self.current_selection = cancel

    def handle_direction(self, input_value:str):
        print(self.get_selection())
        i, j = self.change_cursor_location(input_value)
        self.current_selection = self.active_grid[i][j]
        print(self.get_selection())

    def handle_select(self):
        if self.current_selection:
            return self.current_selection
        if self.active_grid:
            self.current_selection = self.active_grid[0][0]
            return self.current_selection
        else:
            return cancel

    def define_list(self, input_list:list, columns:int):
        self.active_list = input_list
        self.columns = columns
        self.active_grid = self.define_grid(input_list, columns)
        self.current_selection = self.active_grid[0][0]
        if self.current_selection == fight:
            self.mode = default

    def use_combat_terminal(self, input_value):
        if input_value not in valid_inputs:
            return
        if input_value in directional_inputs:
            self.handle_direction(input_value)
        elif input_value == select:
            return self.handle_select()
        elif input_value == cancel:
            return cancel
        
    def get_action_selection_window_dimensions(self):
        top_pad = self.height * 3 / 16
        width_pad = self.width / 16
        width = self.width * 31 / 64
        height = self.height * 28 / 32
        return {'top pad': top_pad, 'width pad': width_pad, 
                'width': width, 'height': height}
    
    def get_moves_selection_window_dimensions(self):
        top_pad = self.height * 3 / 16
        width_pad = self.width / 16
        width = self.width * 62 / 64
        height = self.height* 28 / 32
        return {'top pad': top_pad, 'width pad': width_pad, 
                'width': width, 'height': height}

    def make_selection_window(self):
        text = self.text.draw_text('fight', terminal_font_size, black)
        h = text.get_height()
        w = text.get_width()
        if self.mode in [moves, output_info]:
            values = self.get_moves_selection_window_dimensions()
            w = values['width'] * 3 / 8
        else:
            values = self.get_action_selection_window_dimensions()
        top_pad = values['top pad']
        width_pad = values['width pad']
        width = values['width']
        height = values['height']
        selection_window = Surface((width, height))
        selection_window.fill(grey)
        if self.mode == output_info:
            return selection_window
        for i, row in enumerate(self.active_grid):
            for j, column in enumerate(row):
                item = self.active_grid[i][j]
                text = self.text.draw_text(item, terminal_font_size, black)
                x = (w * i) + width_pad * (i + 1)
                y = (h * j) + top_pad * (j + 1) 
                position = (x , y)
                selection_window.blit(text, position)     
        point = self.get_position()
        if type(point[0]) == int:
            b = text.get_height() * 9 / 8
            i ,j = point[0], point[1]
            x = (w * i) + (width_pad * (i + 1)) - (width_pad / 8)
            y = (h * j) + (top_pad * (j + 1)) + (h / 4)
            h = width_pad * 3 / 8
            headpoint = (x,y)
            self.sprite_tools.draw_triangle(selection_window, headpoint, right, black, b, h)
        return selection_window

    def slow_print(self, text:str, size:int, color):
        self.mode = output_info
        self.draw_terminal()
        max_length = self.width * 28 / 32
        heigh_padding = self.height / 16
        lines = self.text.wrap_text(text, size, max_length)
        x = self.width * 2 / 32
        text_height = self.text.draw_text('TEST', size, black).get_height()
        y = text_height + heigh_padding + self.y
        for line in lines:
            self.text.slow_write_text(self.parent_surface, line, size, (x,y), color)
            y += (heigh_padding + text_height)
        time.sleep(0.5)
        self.draw_terminal()

    def draw_terminal(self):
        self.sprite.fill(grey)
        selection_window = self.make_selection_window()
        x, y = self.width, self.height
        selection_window_pos = (x * 65 / 128, y * 1 / 16)
        if self.mode == moves:
            selection_window_pos = (x * 1 / 64, y * 1 / 16)
        elif self.mode == output_info:
            selection_window_pos = (x * 1 / 64, y * 1 / 16)
        else: 
            top_line = self.text.draw_text('What should', terminal_font_size * (10 / 12), black)
            self.sprite.blit(top_line, (x / 32, y / 4))
            bottom_line = self.text.draw_text(f'{self.name} to do?', terminal_font_size * (10 / 12), black)
            self.sprite.blit(bottom_line, (x / 32, y / 2))
        self.sprite.blit(selection_window, selection_window_pos)
        self.parent_surface.blit(self.sprite, (self.x, self.y + 1))
        self.sprite_tools.add_border(self.parent_surface, self.sprite, (self.x, self.y), black)
        self.sprite_tools.add_interior_border(self.parent_surface, self.sprite, (self.x, self.y), red, 4)
        selection_window_pos = (self.x + selection_window_pos[0], self.y + selection_window_pos[1])
        self.sprite_tools.add_exterior_border(self.parent_surface, selection_window, selection_window_pos, black, 3)
        self.sprite_tools.add_interior_border(self.parent_surface, selection_window, selection_window_pos, brown, 3)
        self.sprite_tools.add_border(self.parent_surface, selection_window, selection_window_pos, red, 2)
