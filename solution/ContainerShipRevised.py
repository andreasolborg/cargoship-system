import time

import numpy as np
from Container import *
from ContainerSet import *
from ContainerSetManager import *
from ContainerShipManager import *
from ContainerStack import *
from ContainerSection import *

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
        for section in self.get_sections():
            self.number_of_operations += section.get_number_of_operations_in_section()
        return self.number_of_operations

        
    def get_lightest_section(self):
        lightest_section = self.available_sections[0]
        for section in self.available_sections:
            if section.get_section_weight() < lightest_section.get_section_weight():
                lightest_section = section
        return lightest_section

    def add_container(self, container):
        if len(self.available_sections) == 0:                   # if there is no available section
            raise Exception("Ship is full, no available section(s). Could not add container with ID: " + container.get_code(), "Stop adding containers.")                            
        else:
            lightest_section = self.get_lightest_section()      # get the lightest section
            #print("Adding container: " + container.get_code(), "total weight: " + str(container.get_total_weight()), "to section " + str(lightest_section.get_sectionID()))
            if lightest_section.is_section_full() == True:
                self.available_sections.remove(lightest_section)
                self.full_sections.append(lightest_section)
                print("Section " + str(lightest_section.get_sectionID()) + " is full, moving to full sections.")
                self.add_container(container)                   # Try to add container again to the lightest section
            else:
                lightest_section.add_container_to_section(container)

    def find_container(self, container_code):
        holding_container = []
        for section in self.get_sections():
                for stacks in section.get_container_stacks():
                    for containers in stacks.get_containers():
                        for container in containers:
                            if container.get_code() == container_code:
                                print("Container "+ container.get_code() + " found in section " + str(section.get_sectionID()) + " stack " + str(stacks.get_location_in_section()) + " container " + str(containers.index(container)+1), "(means the container is the " + str(containers.index(container)+1) + "th container in the stack)")
                                return container
        return None

    
        

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
    random.seed(42069)
    container_set = ContainerSet()
    set_size = 10000
    container_set.generate_random_containers(set_size)
    print("Number of containers: " + str(len(container_set.containers)))
    for container in container_set.containers:
        if container.get_code() == "6346":
            print(container.get_code(), container.get_total_weight(), container.get_length())

    # Load up sections
    try :
        for container in container_set.containers:
            # print("Adding container: " + container.get_code(), "total weight: " + str(container.get_total_weight()))
            ship.add_container(container)
    except Exception as e:
        print(e)
    
    ship.find_container("0001")
    ship.find_container("0865")
    ship.find_container("6344")
    

    
    # Pretty print the ships sections
    # for i in range(0, 6):
    #     print("Section " + str(i+1) + " weight: " + str(ship.full_sections[i].get_section_weight()), "containers: " + str(ship.full_sections[i].get_number_of_containers()) + "\n" + str(ship.full_sections[i]), "size of available stack: " + str(len(ship.full_sections[i].get_available_container_stacks())))
    
    # print(ship.full_sections[0], "\t", ship.full_sections[2], "\t", ship.full_sections[4])
    # print(ship.full_sections[1], "\t", ship.full_sections[3], "\t", ship.full_sections[5])
    
    
    save_ship_with_containers_to_file(ship, "./saved_ships/set_of_{set_size}_containers.tsv".format(set_size=set_size))

            
        

    #END TIME
    end_time = time.time()
    print("Time: " + str(end_time - start_time))
    


if __name__ == "__main__":
    main2()
