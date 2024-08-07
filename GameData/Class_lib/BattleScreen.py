from ..Constants import screen_size
from ..Colors import black, white, brown, grey
from ..Keys import hp
from .Text import Text
from .SpriteTools import SpriteTools
from .BattleInfoDisplay import BattleInfoDisplay
from .BattleTerminal import BattleTerminal
from .RosterSelection import RosterSelection
from .ItemSelection import ItemSelection
from ..Modules.External_Modules import pygame, Surface, Rect

class BattleScreen():
    def __init__(self) -> None:
        self.text = Text()
        self.window:Surface = None
        self.sprite_tools = SpriteTools()
        self.battle_terminal:BattleTerminal = BattleTerminal()
        self.roster_selection = RosterSelection()
        
        #self.item_selection = ItemSelection()
    def set_window(self, surface:Surface):
        print('setting battle screen')
        self.window = surface
        self.battle_terminal.create_terminal(self.window)
        self.roster_selection.teriminal.create_terminal(self.window)

    def set_background(self, color:tuple[int,int,int]):
        self.window.fill(color)

    def init_stat_block(self, is_player:bool):
        stat_block = BattleInfoDisplay()
        x = int(screen_size[0] * 3 / 8)
        if is_player:
            y = int(screen_size[1] / 6)
            stat_block.init_player((x,y))
        else:
            y = int(screen_size[1] / 6)
            stat_block.init_npc((x,y))
        return stat_block
        
    def init_player_stat_block(self):
        self.player_stat_block = self.init_stat_block(True)  
        
    def init_enemy_stat_block(self, npc_count:int):
        self.npc_stat_blocks:list[BattleInfoDisplay] = []
        for npc in range(npc_count):
            stat_block = self.init_stat_block(False)
            self.npc_stat_blocks.append(stat_block)

    def init_battle_terminal(self):
        self.battle_terminal.create_terminal(self.window)

    def init_battle_screen(self, color:tuple[int,int,int], npc_count):
        self.set_background(color)
        self.init_enemy_stat_block(npc_count)
        self.init_player_stat_block()
        self.init_battle_terminal()

    def clear_battle_screen(self):
        self.player_stat_block = None
        self.npc_stat_blocks = [None]
        self.battle_terminal = None
            
    def print_to_battle_terminal(self, text:str):
        self.text.active = self.battle_terminal
        text_obj = self.print(text)
        self.window.blit(text_obj, self.text.active)
        pygame.display.flip()

    def print(self, text:str):
        text_obj = self.text.draw_text(text)
        return text_obj

    def display_battle_player(self, creature):
        active_stats = creature.stats
        self.player_stat_block.update_info(creature)
        current_hp = active_stats.active_value[hp]
        max_hp = active_stats.active_max[hp]
        print(f"{creature.name}'s current hp is {current_hp}/{max_hp}.")

    def display_battle_npc(self, creature):
        active_stats = creature.stats
        self.npc_stat_blocks[0].update_info(creature)
        current_hp = active_stats.active_value[hp]
        max_hp = active_stats.active_max[hp]
        print(f"{creature.name}'s current hp is {current_hp}/{max_hp}.")

    def update(self):
        self.window.fill(grey)
        self.player_stat_block.hp_bar.define_surfs()
        self.player_stat_block.xp_bar.define_surfs()
        self.player_stat_block.sprite.fill(brown)
        self.player_stat_block.draw(self.window)
        self.sprite_tools.add_border(self.window, self.player_stat_block.sprite, self.player_stat_block.position, black)
        for stat_block in self.npc_stat_blocks:
            stat_block.hp_bar.define_surfs()
            stat_block.sprite.fill(brown)
            stat_block.draw(self.window)
            self.sprite_tools.add_border(self.window, stat_block.sprite, stat_block.position, black)
        self.battle_terminal.draw_terminal()
        pygame.display.flip()
