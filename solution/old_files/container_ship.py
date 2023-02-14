from container import *
from ContainerSet import *
from ContainerSetManager import *
from ContainerShipManager import *
from ContainerSection import *
import time
import numpy as np
start_time = time.time()


class ContainerShip:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.containers = [[[None for z in range(self.length)] for y in range(self.width)] for x in range(self.height)]
        self.empty_places = []
        for height in range(self.height):
            for width in range(self.width):
                for length in range(self.length):
                    self.empty_places.append((height, width, length))
        self.sections = []
        self.section_width = width // 2 
        self.section_length = length // 3

        

    def __str__(self):
        ship_str = ""
        for h in range(self.height):
            ship_str += "Floor " + str(h) + "\n"
            for l in range(self.length):
                for w in range(self.width):
                    container = self.containers[h][w][l]
                    if container is None:
                        ship_str += " XX-XX"
                    else:
                        ship_str += " " + str(container.get_code()) + " " +str(container.get_total_weight()) +" "+ str(container.get_length()) + " - "
                ship_str += "\n"
            ship_str += "\n"
        return ship_str

    
def initialize_ship():
    ship = ContainerShip(12, 8, 3) # dimensions of the ship (length, width, height)
    container_set = load_set_of_containers("./solution/set_of_containers/set_of_6k_containers.tsv")
    #sorted_container_set = ship.sort_containers_in_set_by_weight(container_set)
    #ship.load_container_from_set_of_containers(container_set.containers)
    #save_ship_with_containers_to_file(ship, "./solution/set_of_containers/ship_load.tsv")
    return ship

def main():
    ship = initialize_ship()
    
    #ship = load_ship_with_containers_from_file("./solution/ship_load.tsv")
    #make the sections of the ship from the section.py file
    for i in range(ship.section_length*ship.section_width):
        ship.sections.append(ShipSection(ship, ship.section_length, ship.section_width))

    for section in ship.sections:
        print(section.stacks)

    

    print("--- %s seconds ---" % (time.time() - start_time))

    #Remove a container from the ship
    

if __name__ == "__main__":
    main()

