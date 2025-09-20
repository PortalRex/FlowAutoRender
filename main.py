import sys,os
import concurrent.futures
import urllib.parse
from difflib import SequenceMatcher, get_close_matches

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))

from flowlauncher import FlowLauncher
import webbrowser
import requests

s = requests.Session()
_ICON_PATH = os.path.join(parent_folder_path, 'assets', 'app.png')

MAP_INFO = {
    'Advanced Concepts': [
        {'name': 'sp_a3_concepts', 'game_dir': 'portal_stories'},
    ],
    'Advanced Core Access': [
        {'name': 'sp_a4_core_access', 'game_dir': 'portal_stories'},
    ],
    'Advanced Destroyed': [
        {'name': 'sp_a4_destroyed', 'game_dir': 'portal_stories'},
    ],
    'Advanced Destroyed Garden': [
        {'name': 'sp_a2_garden_de', 'game_dir': 'portal_stories'},
    ],
    'Advanced Factory': [
        {'name': 'sp_a4_factory', 'game_dir': 'portal_stories'},
    ],
    'Advanced Faith Plate': [
        {'name': 'sp_a3_faith_plate', 'game_dir': 'portal_stories'},
    ],
    'Advanced Finale': [
        {'name': 'sp_a4_finale', 'game_dir': 'portal_stories'},
    ],
    'Advanced Firestorm': [
        {'name': 'sp_a2_firestorm', 'game_dir': 'portal_stories'},
    ],
    'Advanced Funnel Over Goo': [
        {'name': 'sp_a4_tb_over_goo', 'game_dir': 'portal_stories'},
    ],
    'Advanced Garden': [
        {'name': 'sp_a1_garden', 'game_dir': 'portal_stories'},
    ],
    'Advanced Junkyard': [
        {'name': 'sp_a3_junkyard', 'game_dir': 'portal_stories'},
    ],
    'Advanced Lift': [
        {'name': 'sp_a1_lift', 'game_dir': 'portal_stories'},
    ],
    'Advanced Mel Intro': [
        {'name': 'sp_a1_mel_intro', 'game_dir': 'portal_stories'},
    ],
    'Advanced Once Upon': [
        {'name': 'sp_a2_once_upon', 'game_dir': 'portal_stories'},
    ],
    'Advanced Overgrown': [
        {'name': 'sp_a4_overgrown', 'game_dir': 'portal_stories'},
    ],
    'Advanced Paint Fling': [
        {'name': 'sp_a3_paint_fling', 'game_dir': 'portal_stories'},
    ],
    'Advanced Past Power': [
        {'name': 'sp_a2_past_power', 'game_dir': 'portal_stories'},
    ],
    'Advanced Polarity': [
        {'name': 'mp_coop_tbeam_polarity3', 'game_dir': 'portal2'},
    ],
    'Advanced Ramp': [
        {'name': 'sp_a2_ramp', 'game_dir': 'portal_stories'},
    ],
    'Advanced Tramride': [
        {'name': 'sp_a1_tramride', 'game_dir': 'portal_stories'},
    ],
    'Advanced Transition': [
        {'name': 'sp_a3_transition', 'game_dir': 'portal_stories'},
    ],
    'Advanced Two Of A Kind': [
        {'name': 'sp_a4_two_of_a_kind', 'game_dir': 'portal_stories'},
    ],
    'Advanced Underbounce': [
        {'name': 'sp_a2_underbounce', 'game_dir': 'portal_stories'},
    ],
    'Behind The Scenes': [
        {'name': 'mp_coop_teambts', 'game_dir': 'portal2'},
    ],
    'Bomb Flings': [
        {'name': 'sp_a3_bomb_flings', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a3_bomb_flings', 'game_dir': 'portal2'},
    ],
    'Bridge Catch': [
        {'name': 'mp_coop_bridge_catch', 'game_dir': 'portal2'},
    ],
    'Bridge Fling': [
        {'name': 'mp_coop_catapult_2', 'game_dir': 'portal2'},
    ],
    'Bridge Gels': [
        {'name': 'mp_coop_2paints_1bridge', 'game_dir': 'portal2'},
    ],
    'Bridge Intro': [
        {'name': 'sp_a2_bridge_intro', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_bridge_intro', 'game_dir': 'portal2'},
    ],
    'Bridge Repulsion': [
        {'name': 'mp_coop_paint_bridge', 'game_dir': 'portal2'},
    ],
    'Bridge Swap': [
        {'name': 'mp_coop_wall_2', 'game_dir': 'portal2'},
    ],
    'Bridge Testing': [
        {'name': 'mp_coop_wall_5', 'game_dir': 'portal2'},
    ],
    'Bridge the Gap': [
        {'name': 'sp_a2_bridge_the_gap', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_bridge_the_gap', 'game_dir': 'portal2'},
    ],
    'Buttons': [
        {'name': 'mp_coop_race_2', 'game_dir': 'portal2'},
    ],
    'Catapult Block': [
        {'name': 'mp_coop_wall_block', 'game_dir': 'portal2'},
    ],
    'Catapult Catch': [
        {'name': 'mp_coop_catapult_catch', 'game_dir': 'portal2'},
    ],
    'Catapult Intro': [
        {'name': 'sp_a2_catapult_intro', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_catapult_intro', 'game_dir': 'portal2'},
    ],
    'Catapults': [
        {'name': 'mp_coop_catapult_1', 'game_dir': 'portal2'},
    ],
    'Cave Johnson': [
        {'name': 'sp_a3_03', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a3_03', 'game_dir': 'portal2'},
    ],
    'Ceiling Button': [
        {'name': 'sp_a4_tb_trust_drop', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a4_tb_trust_drop', 'game_dir': 'portal2'},
    ],
    'Ceiling Catapult': [
        {'name': 'sp_a2_sphere_peek', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_sphere_peek', 'game_dir': 'portal2'},
    ],
    'Column Blocker': [
        {'name': 'sp_a2_column_blocker', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_column_blocker', 'game_dir': 'portal2'},
    ],
    'Concepts': [
        {'name': 'st_a3_concepts', 'game_dir': 'portal_stories'},
    ],
    'Container Ride': [
        {'name': 'sp_a1_intro1', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a1_intro1', 'game_dir': 'portal2'},
    ],
    'Conversion Intro': [
        {'name': 'sp_a3_portal_intro', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a3_portal_intro', 'game_dir': 'portal2'},
    ],
    'Cooperative Bridges': [
        {'name': 'mp_coop_wall_intro', 'game_dir': 'portal2'},
    ],
    'Cooperative Funnels': [
        {'name': 'mp_coop_tbeam_redirect', 'game_dir': 'portal2'},
    ],
    'Cooperative Polarity': [
        {'name': 'mp_coop_tbeam_polarity', 'game_dir': 'portal2'},
    ],
    'Core': [
        {'name': 'sp_a2_core', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_core', 'game_dir': 'portal2'},
    ],
    'Core Access': [
        {'name': 'st_a4_core_access', 'game_dir': 'portal_stories'},
    ],
    'Crazier Box': [
        {'name': 'mp_coop_paint_crazy_box', 'game_dir': 'portal2'},
    ],
    'Crazy Box': [
        {'name': 'sp_a3_crazy_box', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a3_crazy_box', 'game_dir': 'portal2'},
    ],
    'Cube Momentum': [
        {'name': 'sp_a1_intro5', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a1_intro5', 'game_dir': 'portal2'},
    ],
    'Destroyed': [
        {'name': 'st_a4_destroyed', 'game_dir': 'portal_stories'},
    ],
    'Destroyed Garden': [
        {'name': 'st_a2_garden_de', 'game_dir': 'portal_stories'},
    ],
    'Doors': [
        {'name': 'mp_coop_doors', 'game_dir': 'portal2'},
    ],
    'Double Bounce': [
        {'name': 'mp_coop_paint_redirect', 'game_dir': 'portal2'},
    ],
    'Double Lift': [
        {'name': 'mp_coop_laser_tbeam', 'game_dir': 'portal2'},
    ],
    'Dual Lasers': [
        {'name': 'sp_a2_dual_lasers', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_dual_lasers', 'game_dir': 'portal2'},
    ],
    'Escape': [
        {'name': 'sp_a2_bts2', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_bts2', 'game_dir': 'portal2'},
    ],
    'Factory': [
        {'name': 'st_a4_factory', 'game_dir': 'portal_stories'},
    ],
    'Faith Plate': [
        {'name': 'st_a3_faith_plate', 'game_dir': 'portal_stories'},
    ],
    'Finale': [
        {'name': 'st_a4_finale', 'game_dir': 'portal_stories'},
    ],
    'Finale 1': [
        {'name': 'sp_a4_finale1', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a4_finale1', 'game_dir': 'portal2'},
    ],
    'Finale 2': [
        {'name': 'sp_a4_finale2', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a4_finale2', 'game_dir': 'portal2'},
    ],
    'Finale 3': [
        {'name': 'sp_a4_finale3', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a4_finale3', 'game_dir': 'portal2'},
    ],
    'Finale 4': [
        {'name': 'sp_a4_finale4', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a4_finale4', 'game_dir': 'portal2'},
    ],
    'Firestorm': [
        {'name': 'st_a2_firestorm', 'game_dir': 'portal_stories'},
    ],
    'Fizzler Intro': [
        {'name': 'sp_a2_fizzler_intro', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_fizzler_intro', 'game_dir': 'portal2'},
    ],
    'Fling Block': [
        {'name': 'mp_coop_catapult_wall_intro', 'game_dir': 'portal2'},
    ],
    'Fling Crushers': [
        {'name': 'mp_coop_fling_crushers', 'game_dir': 'portal2'},
    ],
    'Flings': [
        {'name': 'mp_coop_fling_3', 'game_dir': 'portal2'},
    ],
    'Funnel Catch': [
        {'name': 'sp_a4_tb_catch', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'mp_coop_tbeam_catch_grind_1', 'game_dir': 'portal2'},
        {'name': 'sp_a4_tb_catch', 'game_dir': 'portal2'},
    ],
    'Funnel Drill': [
        {'name': 'mp_coop_tbeam_drill', 'game_dir': 'portal2'},
    ],
    'Funnel Hop': [
        {'name': 'mp_coop_tbeam_polarity2', 'game_dir': 'portal2'},
    ],
    'Funnel Intro': [
        {'name': 'sp_a4_tb_intro', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a4_tb_intro', 'game_dir': 'portal2'},
    ],
    'Funnel Laser': [
        {'name': 'mp_coop_tbeam_laser_1', 'game_dir': 'portal2'},
    ],
    'Funnel Maze': [
        {'name': 'mp_coop_tbeam_maze', 'game_dir': 'portal2'},
    ],
    'Funnel Over Goo': [
        {'name': 'st_a4_tb_over_goo', 'game_dir': 'portal_stories'},
    ],
    'Future Starter': [
        {'name': 'sp_a1_intro6', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a1_intro6', 'game_dir': 'portal2'},
    ],
    'Garden': [
        {'name': 'st_a1_garden', 'game_dir': 'portal_stories'},
    ],
    'Gel Maze': [
        {'name': 'mp_coop_paint_rat_maze', 'game_dir': 'portal2'},
    ],
    'Incinerator': [
        {'name': 'sp_a2_intro', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_intro', 'game_dir': 'portal2'},
    ],
    'Industrial Fan': [
        {'name': 'mp_coop_fan', 'game_dir': 'portal2'},
    ],
    'Infinifling': [
        {'name': 'mp_coop_infinifling_train', 'game_dir': 'portal2'},
    ],
    'Jail Break': [
        {'name': 'sp_a2_bts1', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_bts1', 'game_dir': 'portal2'},
    ],
    'Junkyard': [
        {'name': 'st_a3_junkyard', 'game_dir': 'portal_stories'},
    ],
    'Laser Catapult': [
        {'name': 'sp_a4_laser_catapult', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a4_laser_catapult', 'game_dir': 'portal2'},
    ],
    'Laser Chaining': [
        {'name': 'sp_a2_laser_chaining', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_laser_chaining', 'game_dir': 'portal2'},
    ],
    'Laser Crusher': [
        {'name': 'mp_coop_laser_crusher', 'game_dir': 'portal2'},
    ],
    'Laser Intro': [
        {'name': 'sp_a2_laser_intro', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_laser_intro', 'game_dir': 'portal2'},
    ],
    'Laser Over Goo': [
        {'name': 'sp_a2_laser_over_goo', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_laser_over_goo', 'game_dir': 'portal2'},
    ],
    'Laser Platform': [
        {'name': 'sp_a4_laser_platform', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a4_laser_platform', 'game_dir': 'portal2'},
    ],
    'Laser Relays': [
        {'name': 'sp_a2_laser_relays', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_laser_relays', 'game_dir': 'portal2'},
    ],
    'Laser Stairs': [
        {'name': 'sp_a2_laser_stairs', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_laser_stairs', 'game_dir': 'portal2'},
    ],
    'Laser vs Turret': [
        {'name': 'sp_a2_laser_vs_turret', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_laser_vs_turret', 'game_dir': 'portal2'},
    ],
    'Lasers': [
        {'name': 'mp_coop_laser_2', 'game_dir': 'portal2'},
    ],
    'Lift': [
        {'name': 'st_a1_lift', 'game_dir': 'portal_stories'},
    ],
    'Lobby': [
        {'name': 'mp_coop_lobby_2', 'game_dir': 'portal2'},
        {'name': 'mp_coop_lobby_3', 'game_dir': 'portal2'},
    ],
    'Long Fall': [
        {'name': 'sp_a3_00', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a3_00', 'game_dir': 'portal2'},
    ],
    'Maintenance': [
        {'name': 'mp_coop_paint_conversion', 'game_dir': 'portal2'},
    ],
    'Mel Intro': [
        {'name': 'st_a1_mel_intro', 'game_dir': 'portal_stories'},
    ],
    'Multifling': [
        {'name': 'mp_coop_multifling_1', 'game_dir': 'portal2'},
    ],
    'Neurotoxin Sabotage': [
        {'name': 'sp_a2_bts5', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_bts5', 'game_dir': 'portal2'},
    ],
    'Once Upon': [
        {'name': 'st_a2_once_upon', 'game_dir': 'portal_stories'},
    ],
    'Overgrown': [
        {'name': 'st_a4_overgrown', 'game_dir': 'portal_stories'},
    ],
    'Paint Fling': [
        {'name': 'st_a3_paint_fling', 'game_dir': 'portal_stories'},
    ],
    'Past Power': [
        {'name': 'st_a2_past_power', 'game_dir': 'portal_stories'},
    ],
    'Pit Flings': [
        {'name': 'sp_a2_pit_flings', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_pit_flings', 'game_dir': 'portal2'},
    ],
    'Polarity': [
        {'name': 'sp_a4_tb_polarity', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a4_tb_polarity', 'game_dir': 'portal2'},
    ],
    'Portal Carousel': [
        {'name': 'sp_a1_intro2', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a1_intro2', 'game_dir': 'portal2'},
    ],
    'Portal Gun': [
        {'name': 'sp_a1_intro3', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a1_intro3', 'game_dir': 'portal2'},
    ],
    'PotatOS': [
        {'name': 'sp_a3_transition01', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a3_transition01', 'game_dir': 'portal2'},
    ],
    'Propulsion Catch': [
        {'name': 'sp_a4_speed_tb_catch', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a4_speed_tb_catch', 'game_dir': 'portal2'},
    ],
    'Propulsion Crushers': [
        {'name': 'mp_coop_paint_speed_fling', 'game_dir': 'portal2'},
    ],
    'Propulsion Flings': [
        {'name': 'sp_a3_speed_flings', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a3_speed_flings', 'game_dir': 'portal2'},
    ],
    'Propulsion Intro': [
        {'name': 'sp_a3_speed_ramp', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a3_speed_ramp', 'game_dir': 'portal2'},
    ],
    'Propulsion Retrieval': [
        {'name': 'mp_coop_paint_speed_catch', 'game_dir': 'portal2'},
    ],
    'Pull the Rug': [
        {'name': 'sp_a2_pull_the_rug', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_pull_the_rug', 'game_dir': 'portal2'},
    ],
    'Ramp': [
        {'name': 'st_a2_ramp', 'game_dir': 'portal_stories'},
    ],
    'Rat Maze': [
        {'name': 'mp_coop_rat_maze', 'game_dir': 'portal2'},
    ],
    'Repulsion Intro': [
        {'name': 'sp_a3_jump_intro', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a3_jump_intro', 'game_dir': 'portal2'},
    ],
    'Repulsion Jumps': [
        {'name': 'mp_coop_paint_come_along', 'game_dir': 'portal2'},
    ],
    'Repulsion Polarity': [
        {'name': 'sp_a4_jump_polarity', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a4_jump_polarity', 'game_dir': 'portal2'},
    ],
    'Ricochet': [
        {'name': 'sp_a2_ricochet', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_ricochet', 'game_dir': 'portal2'},
    ],
    'Secret Panel': [
        {'name': 'sp_a1_intro7', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a1_intro7', 'game_dir': 'portal2'},
    ],
    'Separation': [
        {'name': 'mp_coop_separation_1', 'game_dir': 'portal2'},
    ],
    'Smooth Jazz': [
        {'name': 'sp_a1_intro4', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a1_intro4', 'game_dir': 'portal2'},
    ],
    'Start': [
        {'name': 'mp_coop_start', 'game_dir': 'portal2'},
    ],
    'Stop the Box': [
        {'name': 'sp_a4_stop_the_box', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a4_stop_the_box', 'game_dir': 'portal2'},
    ],
    'Team Retrieval': [
        {'name': 'mp_coop_come_along', 'game_dir': 'portal2'},
    ],
    'Test': [
        {'name': 'sp_a4_intro', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a4_intro', 'game_dir': 'portal2'},
    ],
    'Three Gels': [
        {'name': 'sp_a3_end', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a3_end', 'game_dir': 'portal2'},
    ],
    'Tramride': [
        {'name': 'st_a1_tramride', 'game_dir': 'portal_stories'},
    ],
    'Transition': [
        {'name': 'st_a3_transition', 'game_dir': 'portal_stories'},
    ],
    'Triple Axis': [
        {'name': 'mp_coop_tripleaxis', 'game_dir': 'portal2'},
    ],
    'Triple Laser': [
        {'name': 'sp_a2_triple_laser', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_triple_laser', 'game_dir': 'portal2'},
    ],
    'Trust Fling': [
        {'name': 'sp_a2_trust_fling', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_trust_fling', 'game_dir': 'portal2'},
    ],
    'Tube Ride': [
        {'name': 'sp_a2_bts6', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_bts6', 'game_dir': 'portal2'},
    ],
    'Turret Assassin': [
        {'name': 'mp_coop_turret_ball', 'game_dir': 'portal2'},
    ],
    'Turret Blocker': [
        {'name': 'sp_a2_turret_blocker', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_turret_blocker', 'game_dir': 'portal2'},
    ],
    'Turret Factory': [
        {'name': 'sp_a2_bts3', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_bts3', 'game_dir': 'portal2'},
    ],
    'Turret Intro': [
        {'name': 'sp_a2_turret_intro', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_turret_intro', 'game_dir': 'portal2'},
    ],
    'Turret Ninja': [
        {'name': 'mp_coop_paint_red_racer', 'game_dir': 'portal2'},
    ],
    'Turret Sabotage': [
        {'name': 'sp_a2_bts4', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a2_bts4', 'game_dir': 'portal2'},
    ],
    'Turret Walls': [
        {'name': 'mp_coop_turret_walls', 'game_dir': 'portal2'},
    ],
    'Turret Warehouse': [
        {'name': 'mp_coop_tbeam_end', 'game_dir': 'portal2'},
    ],
    'Two Of A Kind': [
        {'name': 'st_a4_two_of_a_kind', 'game_dir': 'portal_stories'},
    ],
    'Underbounce': [
        {'name': 'st_a2_underbounce', 'game_dir': 'portal_stories'},
    ],
    'Underground': [
        {'name': 'sp_a3_01', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a3_01', 'game_dir': 'portal2'},
    ],
    'Vault Entrance': [
        {'name': 'mp_coop_paint_longjump_intro', 'game_dir': 'portal2'},
    ],
    'Vertical Flings': [
        {'name': 'mp_coop_fling_1', 'game_dir': 'portal2'},
    ],
    'Wakeup': [
        {'name': 'sp_a1_wakeup', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a1_wakeup', 'game_dir': 'portal2'},
    ],
    'Wall Button': [
        {'name': 'sp_a4_tb_wall_button', 'game_dir': 'Portal 2 Speedrun Mod'},
        {'name': 'sp_a4_tb_wall_button', 'game_dir': 'portal2'},
    ],
    'Wall Repulsion': [
        {'name': 'mp_coop_paint_walljumps', 'game_dir': 'portal2'},
    ],
}
MAP_ALIASES = list(MAP_INFO.keys())
_MAP_ALIAS_LOOKUP = {alias.lower(): alias for alias in MAP_ALIASES}
_MAP_ALIAS_TERMS = list(_MAP_ALIAS_LOOKUP.keys())
_MAP_ALIAS_NO_SPACE_LOOKUP = {alias.replace(' ', '').lower(): alias for alias in MAP_ALIASES}
_MAP_ALIAS_NO_SPACE_TERMS = list(_MAP_ALIAS_NO_SPACE_LOOKUP.keys())
_FUZZY_IGNORE_TOKENS = {
    'wr',
    'world',
    'record',
    'rank',
    'time',
    'host',
    'latest',
    'sp',
    'coop',
    'mp',
    'blue',
    'orange',
    'player',
    'run',
}
BOARD_DOMAIN_TO_GAME_DIR = {
    'board.portal2.sr': 'portal2',
    'mel.board.portal2.sr': 'portal_stories',
}
PREFERRED_GAME_DIR_ORDER = [
    'portal2',
    'portal_stories',
    'portalreloaded',
    'aperturetag',
    'twtm',
    'portal 2 speedrun mod',
]
_TICKS_PER_SECOND = 60.0

class AutoRenderSearch(FlowLauncher):
  
    def calculate_similarity(self, query, result):
        if not query:
            return 0

        fields = []
        for key in ("map", "user", "comment"):
            value = result.get(key)
            if value:
                fields.append(str(value))

        query_lower = query.lower()
        best_score = 0

        for field in fields:
            field_lower = field.lower()
            if query_lower in field_lower:
                return 1.0

            score = SequenceMatcher(None, query_lower, field_lower).ratio()
            if score > best_score:
                best_score = score

        return best_score

    def request_results(self, query_text):
        search_string = urllib.parse.quote_plus(query_text)
        url = f'https://autorender.p2sr.org/api/v1/search?q={search_string}'
        response = s.get(url, timeout=5)
        response.raise_for_status()

        payload = response.json()
        return payload.get('results', [])

    def suggest_query(self, query):
        normalized_tokens = [token for token in query.lower().split() if token]
        if not normalized_tokens:
            return None

        def token_has_digit(token):
            return any(char.isdigit() for char in token)

        filtered_tokens = []
        modifiers = []
        for token in normalized_tokens:
            if token in _FUZZY_IGNORE_TOKENS or token_has_digit(token):
                modifiers.append(token)
            else:
                filtered_tokens.append(token)

        candidates = []

        def add_candidate(text):
            text = ' '.join(text.split()).strip()
            if text and text not in candidates:
                candidates.append(text)

        add_candidate(' '.join(normalized_tokens))

        if filtered_tokens:
            add_candidate(' '.join(filtered_tokens))
            add_candidate(' '.join(reversed(filtered_tokens)))
            add_candidate(' '.join(sorted(filtered_tokens)))

            for length in range(len(filtered_tokens), 0, -1):
                add_candidate(' '.join(filtered_tokens[:length]))
                add_candidate(' '.join(filtered_tokens[-length:]))

            for token in filtered_tokens:
                add_candidate(token)

        for candidate in candidates:
            match = get_close_matches(candidate, _MAP_ALIAS_TERMS, n=1, cutoff=0.6)
            if match:
                return _MAP_ALIAS_LOOKUP[match[0]], modifiers

            compact = candidate.replace(' ', '')
            match = get_close_matches(compact, _MAP_ALIAS_NO_SPACE_TERMS, n=1, cutoff=0.7)
            if match:
                return _MAP_ALIAS_NO_SPACE_LOOKUP[match[0]], modifiers

        return None

    def resolve_map_entry(self, alias, source_domain=None):
        entries = MAP_INFO.get(alias)
        if not entries:
            return None

        if source_domain:
            preferred = BOARD_DOMAIN_TO_GAME_DIR.get(source_domain.lower())
            if preferred:
                preferred_lower = preferred.lower()
                for entry in entries:
                    game_dir = (entry.get('game_dir') or '').lower()
                    if game_dir == preferred_lower:
                        return entry

        for preferred in PREFERRED_GAME_DIR_ORDER:
            preferred_lower = preferred.lower()
            for entry in entries:
                game_dir = (entry.get('game_dir') or '').lower()
                if game_dir == preferred_lower:
                    return entry

        return entries[0]

    def format_ticks(self, ticks):
        try:
            ticks_int = int(ticks)
        except (TypeError, ValueError):
            return "Unknown"

        seconds_total = ticks_int / _TICKS_PER_SECOND
        minutes = int(seconds_total // 60)
        seconds = seconds_total - (minutes * 60)

        if minutes:
            return f"{minutes}:{seconds:05.2f}"
        return f"{seconds:.2f}s"

    def format_split_summary(self, splits):
        if not splits:
            return "No internal splits"

        parts = []
        for split in splits:
            name = split.get('name') or 'Split'
            ticks = split.get('ticks')
            parts.append(f"{name}: {self.format_ticks(ticks)}")

        return "Splits: " + " | ".join(parts)

    def fetch_mtrigger_stats(self, game_dir, map_name, board_rank, profile_number=None):
        params = {
            'game_dir': game_dir,
            'map_name': map_name,
            'board_rank': board_rank,
        }

        if profile_number:
            params['include_pb_of'] = profile_number

        response = s.get('https://autorender.p2sr.org/api/v1/mtriggers/search', params=params, timeout=5)
        response.raise_for_status()
        return response.json()

    def format_time(self, time_hundredths):
        if time_hundredths is None:
            return "Unknown Time"

        try:
            hundredths_total = int(time_hundredths)
        except (TypeError, ValueError):
            return "Unknown Time"

        minutes, remainder = divmod(hundredths_total, 6000)
        seconds, hundredths = divmod(remainder, 100)

        if minutes:
            return f"{minutes}:{seconds:02}.{hundredths:02}"

        return f"{seconds}.{hundredths:02}"

    def fetch_result(self, query, result):
        share_id = result.get('share_id')
        user = result.get('user', 'Unknown User')
        time_hundredths = result.get('time', 0)
        comment = result.get('comment', '')
        original_rank = result.get('orig_rank')
        map_alias = result.get('map', 'Unknown Map')
        source_domain = result.get('source')
        map_entry = self.resolve_map_entry(map_alias, source_domain)
        default_thumbnail_path = _ICON_PATH
        formatted_time = self.format_time(time_hundredths)
        rank_text = original_rank if original_rank is not None else 'Unknown Rank'
        comment_text = comment if comment else 'No comment'
        subtitle_parts = [
            f"User: {user}",
            f"Rank: {rank_text}",
            f"Comment: {comment_text}",
        ]

        if source_domain:
            subtitle_parts.append(f"Source: {source_domain}")

        subtitle = " | ".join(subtitle_parts)

        item = {
            "Title": f"{map_alias} - {formatted_time}",
            "SubTitle": subtitle,
            "IcoPath": default_thumbnail_path,
        }

        if share_id:
            autorender_url = f'https://autorender.p2sr.org/videos/{share_id}'
            item["JsonRPCAction"] = {
                "method": "open_url",
                "parameters": [autorender_url]
            }

        context_data = {
            "share_id": share_id,
            "map_alias": map_alias,
            "map_name": map_entry['name'] if map_entry else None,
            "game_dir": map_entry['game_dir'] if map_entry else None,
            "rank": original_rank,
            "profile_number": result.get('user_id'),
            "source_domain": source_domain,
        }

        changelog_id = result.get('id') or result.get('board_changelog_id')
        if changelog_id is not None:
            context_data['board_changelog_id'] = changelog_id

        item["ContextData"] = context_data

        return item

    def query(self, query):
        sanitized_query = ' '.join(query.strip().split())
        if not sanitized_query:
            return [
                {
                    "Title": "Enter a search term",
                    "SubTitle": "Type a map or runner name to search autorender",
                    "IcoPath": _ICON_PATH,
                }
            ]

        try:
            active_query = sanitized_query
            results = self.request_results(active_query)

            def build_items(result_set, query_text):
                query_for_similarity = query_text.lower()
                sorted_results = sorted(
                    result_set,
                    key=lambda result: self.calculate_similarity(query_for_similarity, result),
                    reverse=True,
                )

                with concurrent.futures.ThreadPoolExecutor() as executor:
                    return [
                        item
                        for item in executor.map(lambda result: self.fetch_result(query_text, result), sorted_results)
                        if item
                    ]

            base_items = build_items(results, active_query) if results else []
            if base_items:
                return base_items

            suggestion = self.suggest_query(sanitized_query)
            subtitle = "Try a different search term"

            if suggestion:
                suggested_term, modifiers = suggestion
                suggestion_query_parts = [suggested_term, *modifiers]
                suggestion_query = ' '.join(part for part in suggestion_query_parts if part).strip()

                if suggestion_query.lower() != sanitized_query.lower():
                    suggestion_results = self.request_results(suggestion_query)
                    suggestion_items = build_items(suggestion_results, suggestion_query) if suggestion_results else []
                    if suggestion_items:
                        return suggestion_items

                    subtitle = f"No videos found for '{sanitized_query}' or suggested term '{suggestion_query}'"
                else:
                    subtitle = f"No videos found for '{sanitized_query}'"

            return [
                {
                    "Title": "No results found",
                    "SubTitle": subtitle,
                    "IcoPath": _ICON_PATH,
                }
            ]
        except requests.exceptions.RequestException as exc:
            print(f"Network error in query: {exc}")
            return [
                {
                    "Title": "Network error",
                    "SubTitle": "Check your connection and try again",
                    "IcoPath": _ICON_PATH,
                }
            ]
        except ValueError as exc:
            print(f"Error parsing response: {exc}")
            return [
                {
                    "Title": "Unexpected response",
                    "SubTitle": "The autorender API returned data in an unexpected format",
                    "IcoPath": _ICON_PATH,
                }
            ]

    def context_menu(self, data):
        if not isinstance(data, dict):
            return [{
                "Title": "MTrigger data unavailable",
                "SubTitle": "No context information provided.",
                "IcoPath": _ICON_PATH,
            }]

        map_alias = data.get('map_alias')
        map_name = data.get('map_name')
        game_dir = data.get('game_dir')
        source_domain = data.get('source_domain')

        rank_value = data.get('rank')
        try:
            rank = int(rank_value)
        except (TypeError, ValueError):
            rank = None

        profile_number = data.get('profile_number')

        if (map_name is None or game_dir is None) and map_alias:
            resolved = self.resolve_map_entry(map_alias, source_domain)
            if resolved:
                map_name = map_name or resolved.get('name')
                game_dir = game_dir or resolved.get('game_dir')

        if map_name is None or game_dir is None or rank is None:
            return [{
                "Title": "MTrigger data unavailable",
                "SubTitle": "Missing map metadata or rank to query autorender.",
                "IcoPath": _ICON_PATH,
            }]

        try:
            payload = self.fetch_mtrigger_stats(game_dir, map_name, rank, profile_number)
        except requests.exceptions.RequestException as exc:
            return [{
                "Title": "MTrigger request failed",
                "SubTitle": f"{exc}",
                "IcoPath": _ICON_PATH,
            }]
        except ValueError as exc:
            return [{
                "Title": "MTrigger response error",
                "SubTitle": f"{exc}",
                "IcoPath": _ICON_PATH,
            }]

        entries = []
        if isinstance(payload, dict):
            entries = payload.get('data') or []

        if not entries:
            return [{
                "Title": "No mtrigger segments",
                "SubTitle": "Autorender did not return SAR mtrigger data for this run.",
                "IcoPath": _ICON_PATH,
            }]

        items = []
        for entry in entries:
            entry_rank = entry.get('board_rank', rank)
            entry_profile = entry.get('board_profile_number')
            entry_changelog = entry.get('board_changelog_id')

            header_parts = [f"Rank #{entry_rank}"]
            if entry_profile:
                header_parts.append(f"Profile {entry_profile}")
            header_title = " – ".join(header_parts)
            header_subtitle_parts = []
            if entry_changelog is not None:
                header_subtitle_parts.append(f"Changelog ID: {entry_changelog}")
            if map_alias:
                header_subtitle_parts.append(f"Map: {map_alias}")
            header_subtitle = " | ".join(header_subtitle_parts) if header_subtitle_parts else "Segment breakdown"

            items.append({
                "Title": header_title,
                "SubTitle": header_subtitle,
                "IcoPath": _ICON_PATH,
            })

            metadata = entry.get('demo_metadata')
            segments = metadata.get('segments') if isinstance(metadata, dict) else None
            if not segments:
                items.append({
                    "Title": "No segments recorded",
                    "SubTitle": "SAR did not provide segment data for this run.",
                    "IcoPath": _ICON_PATH,
                })
                continue

            for index, segment in enumerate(segments, start=1):
                segment_name = segment.get('name') or f"Segment {index}"
                segment_ticks = segment.get('ticks')
                segment_title = f"{segment_name} — {self.format_ticks(segment_ticks)}"
                splits = segment.get('splits') or []
                subtitle_parts = [f"Ticks: {segment_ticks if segment_ticks is not None else 'Unknown'}"]
                if splits:
                    subtitle_parts.append(self.format_split_summary(splits))
                else:
                    subtitle_parts.append("Splits: none")

                items.append({
                    "Title": segment_title,
                    "SubTitle": " | ".join(subtitle_parts),
                    "IcoPath": _ICON_PATH,
                })

        return items

    def open_url(self, url):
        if url:
            webbrowser.open(url)

if __name__ == "__main__":
    AutoRenderSearch()
