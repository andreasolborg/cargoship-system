import time

import numpy as np
from container import *
from container_set import *
from container_set_manager import *
from container_ship_manager import *
from container_stack import *
from section import *


class ContainerShip:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.available_sections = []
        self.full_sections = []
        self.number_of_operations = 0
        for i in range(0, 6):
            # 3x2 sections
            self.available_sections.append(ShipSection(
                i, self.length//6, self.width//2, self.height)) # must divide by 6 because we assume each container as 40 feet long and each cell is 20 feet long
            
        self.holding_spot = []  # Holding spot for 20ft containers

    def get_ship_length(self):
        return self.length

    def get_ship_width(self):
        return self.width

    def get_ship_height(self):
        return self.height

    def get_sections(self):
        return self.available_sections + self.full_sections

    def get_section(self, sectionID):
        return self.sections[sectionID]
    
    def get_number_of_operations(self):
        for section in self.available_sections:
            self.number_of_operations += section.get_number_of_operations_in_section()
        return self.number_of_operations
        

    def get_lightest_section(self):
        lightest_section = self.available_sections[0]
        for section in self.available_sections:
            if section.get_section_weight() <= lightest_section.get_section_weight():
                lightest_section = section
        return lightest_section

    def add_container(self, container):
        if len(self.available_sections) == 0:                   # if there is no available section
            raise Exception("Ship is full")                               
        else:
            lightest_section = self.get_lightest_section()      # get the lightest section
            if lightest_section.is_section_full() == True:
                self.available_sections.remove(lightest_section)
                self.full_sections.append(lightest_section)
                self.add_container(container)
            else:
                lightest_section.add_container_to_section(container)
            
                   

        
    def __str__(self) -> str:
        pass


def main():
    random.seed(10)
    container_set = ContainerSet()
    container_set.generate_random_containers(10)
    #ship = ContainerShip(12, 10, 9)
    ship = ContainerShip(24, 22, 18)
    
    
    for section in ship.get_sections():
        print(section)
        


def main2():
    #START TIME
    start_time = time.time()
    
    ship_dimensions = [24, 22, 18]
    ship = ContainerShip(
        ship_dimensions[0], ship_dimensions[1], ship_dimensions[2])
    #loaded_container_set = load_set_of_containers("./solution/set_of_containers/set_of_6k_containers.tsv")
    #random.seed(42069)
    container_set = ContainerSet()
    container_set.generate_random_containers(10000)

    # Load up sections
    try :
        for container in container_set.containers:
            ship.add_container(container)
    except Exception as e:
        print(e)
    

    # Print sections
    # for i in range(0, 6):
    #     print("Section " + str(i+1) + " weight: " + str(ship.sections[i].get_section_weight()),
    #           "containers: " + str(ship.sections[i].get_number_of_containers()) + "\n" + str(ship.sections[i]), "size of available stack: " + str(len(ship.sections[i].get_available_container_stacks())))


    
    # Pretty print the ships sections
    # for i in range(0, 6):
    #     print("Section " + str(i+1) + " weight: " + str(ship.full_sections[i].get_section_weight()), "containers: " + str(ship.full_sections[i].get_number_of_containers()) + "\n" + str(ship.full_sections[i]), "size of available stack: " + str(len(ship.full_sections[i].get_available_container_stacks())))
    
    print(ship.full_sections[0], "\t", ship.full_sections[2], "\t", ship.full_sections[4])
    print(ship.full_sections[1], "\t", ship.full_sections[3], "\t", ship.full_sections[5])
    
            
        

    #END TIME
    end_time = time.time()
    print("Time: " + str(end_time - start_time))
    


if __name__ == "__main__":
    main2()
