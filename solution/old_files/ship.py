from container import *
from ContainerSet import *
from ContainerSetManager import *
from ContainerShipManager import *
from ContainerSection import *
from ContainerStack import *
import time
import numpy as np
start_time = time.time()


class ContainerShip:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.sections = []
        self.section_width = width // 2 
        self.section_length = length // 3
        self.section_height = height


    def get_ship_length(self):
        return self.length 
    
    def get_ship_width(self):
        return self.width
    
    def get_ship_height(self):
        return self.height
    
    def get_containers(self):
        return self.containers
    
    def get_sections(self):
        return self.sections
    


    
    
    ################################ Functions for task 5 ###########################################
    
    # Get nth container in a section
    def get_nth_container_in_section(self, section, height, width, length):
        if height >= self.height or width >= self.width or length >= self.length:
            return None
        return section.get_stack(length, width)[height]
    
    # Get the weight of a section
    def get_weight_of_section(self, section):
        return section.get_weight()
    
    # Pop the top container from a section
    def pop_top_container_from_section(self, section):
        return section.remove_container()

     
    ################################    Task 5 finished         ######################################
    ################################    Functions for task 7    ######################################
    

    
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
        ship.sections.append(ShipSection(ship, ship.section_length, ship.section_width, ship.section_height))

    
    container_set = load_set_of_containers("./solution/set_of_containers/small_container_set.tsv")
    print(ship.sections[0].empty_places)
    for stack in ship.sections[0].get_stacks():
        print(stack)
        print("   ")

    #add 20 containers to the ship from the container_set
    for i in range(40):
        ship.sections[0].add_container(container_set.containers[i])

    

    stacks = ship.sections[0].get_stacks()
    section = ship.sections
    #print(stacks)
    def print_stacks(stacks):
        for stack in stacks:
            # if the stack is not empty
            if stack:
                for stack_element in stack:
                    if stack_element:
                        for container in stack_element:
                            # if the stack_element is not a list
                            if not isinstance(container, list):
                                print(container)
                            else:
                                for container in container:
                                    print(container)
 


    
    print_stacks(stacks)
    
    #print the height of the section
    print(ship.sections[0].get_height())
    

    print("--- %s seconds ---" % (time.time() - start_time))

    #Remove a container from the ship
    

if __name__ == "__main__":
    main()

