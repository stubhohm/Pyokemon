from ..Creatures.Torchic_Line.Full import instance_combusken, instance_torchic
from ..Creatures.Wurmple_Line.Full import instance_wurmple
from ..Class_lib.ActorBattleInfo import ActorBattleInfo
from ..Keys import battle, player
from ..Keys import up, down, left, right, directional_inputs
from ..Keys import fight, run, swap, item, combat_inputs
from ..Keys import select, cancel
from ..Keys import moves, default
from ..Keys import hp
from ..Class_lib.UI import ui
from ..Colors import *
from ..Modules.External_Modules import time, key_input, pygame

wurmple = instance_wurmple(6)
torchic = instance_torchic(8)
combusken = instance_combusken(20)
roster = [wurmple, torchic, combusken]
ab_player = ActorBattleInfo()
ab_player.define_battle_info(roster, None, player)

def display_battle_player(creature):
    active_stats = creature.stats
    ui.display.active.player_stat_block.update_info(creature)
    current_hp = active_stats.active_value[hp]
    max_hp = active_stats.active_max[hp]

def display_battle_npc(creature):
    active_stats = creature.stats
    ui.display.active.npc_stat_blocks[0].update_info(creature)
    current_hp = active_stats.active_value[hp]
    max_hp = active_stats.active_max[hp]

def mainfx():
    wurmple = instance_wurmple(6)
    combusken = instance_combusken(20)

    playing = True
    ui.display.set_screen_state(battle)
    ui.display.active.init_battle_screen(white, 1)
    battle_screen = ui.display.active
    terminal = battle_screen.battle_terminal
    ui.display.active.player_stat_block.define(combusken)
    ui.display.active.npc_stat_blocks[0].define(wurmple)
    terminal.set_active_name(combusken.name)
    terminal.define_list(combat_inputs, 2)
    terminal_state = None
    while playing:
        if not ui.input.is_playing:
            playing = False
            continue
        ui.display.active.update()
        name = ui.input.get_player_input()
        if name in directional_inputs:
            print(name)
        if name == 'return':
            print(name)
            name = select
        if name == 'b':
            terminal_state = None
            terminal.define_list(combat_inputs, 2)
        output = terminal.use_combat_terminal(name)
        if type(output) == str:
            print(output)
            if output == fight:
                moves_list = combusken.moves.get_moves_list()
                terminal.mode = moves
                terminal.define_list(moves_list, 2)
        ui.display.active.update()
        
    pygame.quit()



