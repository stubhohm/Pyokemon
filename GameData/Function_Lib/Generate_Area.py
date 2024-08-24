from ..Class_lib.Area import Area
from ..Maps.Littleroot_Town.area import generate_town as generate_littleroot_town
from ..Maps.Oldale_Town.area import generate_town as generate_oldale_town
from ..Maps.Petalburg_City.area import generate_town as generate_petalburg_city
from ..Maps.Route_101.area import generate_route as generate_route_101
from ..Maps.Route_102.area import generate_route as generate_route_102
from ..Maps.Route_103.area import generate_route as generate_route_103
from ..Maps.Route_104_South.area import generate_route as generate_route_104_south
from ..Maps.Route_104_North.area import generate_route as generate_route_104_north
from ..Maps.Petalburg_Woods.area import generate_route as generate_petalburg_woods

def generate_area():
    start_area = Area('Starting Area')
    littleroot_town = generate_littleroot_town()
    oldale_town = generate_oldale_town()
    petalburg_city = generate_petalburg_city()

    petalburg_woods = generate_petalburg_woods()

    route_101 = generate_route_101()
    route_102 = generate_route_102()
    route_103 = generate_route_103()
    route_104_s = generate_route_104_south()
    route_104_n = generate_route_104_north()
    
    
    # Add Routes to the towns
    littleroot_town.add_route(route_101)
    
    oldale_town.add_route(route_101)
    oldale_town.add_route(route_102)
    oldale_town.add_route(route_103)

    petalburg_city.add_route(route_102)
    petalburg_city.add_route(route_104_s)

    # Add Towns to Routes
    route_101.add_adjacent_area(littleroot_town)
    route_101.add_adjacent_area(oldale_town)

    route_102.add_adjacent_area(oldale_town)
    route_102.add_adjacent_area(petalburg_city)

    route_104_s.add_adjacent_area(petalburg_city)
    route_104_s.add_adjacent_area(petalburg_woods)
    
    petalburg_woods.add_adjacent_area(route_104_s)
    petalburg_woods.add_adjacent_area(route_104_n)

    route_104_n.add_adjacent_area(petalburg_woods)



    route_103.add_adjacent_area(oldale_town)
    

    start_area.set_active_area(littleroot_town)
    start_area.active.navigation.starting_position = (14, 7)

    return start_area

