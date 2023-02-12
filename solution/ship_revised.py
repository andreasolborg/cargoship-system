from container import *
from container_set import *
from container_set_manager import *
from container_ship_manager import *
from section import *
from container_stack import *
from container_set_manager import *
import time
import numpy as np

class ContainerShip:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.sections = []
        self.operationCounter = 0
        

    def get_ship_length(self):
        return self.length 
        
    def get_ship_width(self):
        return self.width
        
    def get_ship_height(self):
        return self.height
             
    def get_sections(self):
        return self.sections
        
    def get_section(self, sectionID):
        return self.sections[sectionID]
    
    def get_lightest_section(self):
        lightest_section = self.sections[0]
        for section in self.sections:
            if section.get_section_weight() < lightest_section.get_section_weight():
                lightest_section = section
        return lightest_section


    def add_container(self, container):
        section = self.get_lightest_section()
        if section == None:
            raise Exception("No section found")
        else:
            section.add_container(container)
            return section

def main():
    ship_dimensions = [24, 22, 18]
    ship = ContainerShip(ship_dimensions[0], ship_dimensions[1], ship_dimensions[2])
    #loaded_container_set = load_set_of_containers("./solution/set_of_containers/set_of_6k_containers.tsv")
    random.seed(42069)
    container_set = generate_list_of_random_containers(6330)

    # Create sections
    for i in range(0, 6):
        # 3x2 sections
        ship.sections.append(ShipSection(i, ship_dimensions[0]//6, ship_dimensions[1]//2, ship_dimensions[2]))
    
    # Load up sections
    for container in container_set:
        ship.add_container(container)

        
    # Print sections
    for i in range(0, len(ship.sections)):
        ship.operationCounter += ship.sections[i].get_number_of_operations_in_section()
        print("Section " + str(i+1) + " weight: " + str(ship.sections[i].get_section_weight()), "containers: " + str(ship.sections[i].get_number_of_containers()) + "\n" + str(ship.sections[i]))
        
    print("Total operations: " + str(ship.operationCounter))

if __name__ == "__main__":
    main()
