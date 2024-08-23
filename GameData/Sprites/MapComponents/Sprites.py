from ...Class_lib.Sprite import Sprite
from ...Modules.External_Modules import os
from ...Keys import town, route, building

directory_path = os.path.join('GameData', 'Sprites', 'MapComponents', 'Maps')

def generate_petalbug_wood_map():
    petalburg_img_path = os.path.join(directory_path, route, 'Petalburg_Woods.png')
    petalburg_woods_map = Sprite('Petalburg Woods', 2)
    petalburg_woods_map.import_image(petalburg_img_path)
    petalburg_woods_map.cap_both()
    petalburg_woods_map.invert_movement()
    return petalburg_woods_map


def generate_littleroot_town_map():
    img_path = os.path.join(directory_path, town, 'Littleroot_Town.png')
    map = Sprite('Littlerot Town', 2)
    map.import_image(img_path)
    map.cap_both()
    map.invert_movement()
    return map

def generate_oldale_town_map():
    img_path = os.path.join(directory_path, town, 'Oldale_Town.png')
    map = Sprite('Oldale Town', 2)
    map.import_image(img_path)
    map.cap_both()
    map.invert_movement()
    return map

def generate_route_101_map():
    img_path = os.path.join(directory_path, route, 'Route_101_Map.png')
    map = Sprite('Route 101', 2)
    map.import_image(img_path)
    map.cap_both()
    map.invert_movement()
    return map

def generate_route_102_map():
    img_path = os.path.join(directory_path, route, 'Route_102_Map.png')
    map = Sprite('Route 102', 2)
    map.import_image(img_path)
    map.cap_both()
    map.invert_movement()
    return map

def generate_route_103_map():
    img_path = os.path.join(directory_path, route, 'Route_103_Map.png')
    map = Sprite('Route 103', 2)
    map.import_image(img_path)
    map.cap_both()
    map.invert_movement()
    return map

def generate_route_104_South_map():
    img_path = os.path.join(directory_path, route, 'Route_104_South_Map.png')
    map = Sprite('Route 104', 2)
    map.import_image(img_path)
    map.cap_both()
    map.invert_movement()
    return map

def generate_route_104_North_map():
    img_path = os.path.join(directory_path, route, 'Route_104_North_Map.png')
    map = Sprite('Route 104', 2)
    map.import_image(img_path)
    map.cap_both()
    map.invert_movement()
    return map