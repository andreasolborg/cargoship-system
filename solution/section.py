from container import Container
from container_stack import ContainerStack
from container_set_manager import *
from container_set import *

import random


# Standard ship dimensions as defined in the assignment
SHIP_LENGTH = 24
SHIP_WIDTH = 22
SHIP_HEIGHT = 18
ship_dimensions = (SHIP_LENGTH, SHIP_WIDTH, SHIP_HEIGHT)
max_stack_height = 5


class ShipSection:

    def __init__(self, sectionID, section_length, section_width, max_stack_height):
        self.sectionID = sectionID
        self.section_length = section_length
        self.section_width = section_width
        self.max_stack_height = max_stack_height
        self.operationCounter = 0
        self.available_container_stacks = []
        self.full_container_stacks = []

        self.holding_containers = [] # Containers that are being held for a 20ft container
    
        self.section_weight = 0

        # Create container stacks
        for x in range(0, self.section_length):
            for y in range(0, self.section_width):
                self.available_container_stacks.append(ContainerStack(self.sectionID, (x, y), self.max_stack_height))
            
    # Get functions
    def get_sectionID(self):
        return self.sectionID

    def get_section_length(self):
        return self.section_length

    def get_section_width(self):
        return self.section_width

    def get_max_stack_height(self):
        return self.max_stack_height

    def get_available_container_stacks(self):
        return self.available_container_stacks

    def get_full_container_stacks(self):
        return self.full_container_stacks

    def get_operationCounter(self):
        return self.operationCounter

    # Get section weight by adding up the weight of all stacks in full and available stacks
    def get_section_weight(self):
        section_weight = 0
        for stack in self.available_container_stacks:
            section_weight += stack.get_stack_weight()
        for stack in self.full_container_stacks:
            section_weight += stack.get_stack_weight()
        return section_weight
        
        
    def get_lightest_container_stack(self):
        lightest_stack = self.available_container_stacks[0]
        for stack in self.available_container_stacks:
            if stack.get_stack_weight() < lightest_stack.get_stack_weight():
                lightest_stack = stack
        return lightest_stack
    
    def get_number_of_containers(self):
        number_of_containers = 0
        for stack in self.available_container_stacks:
            number_of_containers += stack.get_number_of_containers()
        for stack in self.full_container_stacks:
            number_of_containers += stack.get_number_of_containers()
        return number_of_containers

    # Set functions
    def set_sectionID(self, sectionID):
        self.sectionID = sectionID

    def set_section_length(self, section_length):
        self.section_length = section_length

    def set_section_width(self, section_width):
        self.section_width = section_width

    def set_max_stack_height(self, max_stack_height):
        self.max_stack_height = max_stack_height

    def set_container_stacks(self, container_stacks):
        self.container_stacks = container_stacks

    def set_operationCounter(self, operationCounter):
        self.operationCounter = operationCounter

    def add_container(self, container):
        container_stack = self.get_lightest_container_stack()
        if container_stack.container_stack_is_full() == True:
            self.full_container_stacks.append(container_stack)
            self.available_container_stacks.remove(container_stack)
        else:
            if container.get_length() == 20 and self.holding_containers == []:
                self.holding_containers.append(container)
                #print("Holding 1 20 footer for now" , self.holding_containers)
            elif container.get_length() == 20 and self.holding_containers != []:
                self.holding_containers.append(container)
                #print("adding 2 20 footers", self.holding_containers)
                container_stack.add_container_to_stack([self.holding_containers[0], self.holding_containers[1]])
                self.holding_containers = []
            elif container.get_length() == 40:
                container_stack.add_container_to_stack(container)
            self.section_weight += container.get_weight()

            
            
        
    def get_number_of_operations_in_section(self):
        counter = 0
        for stack in self.available_container_stacks + self.full_container_stacks:
            counter += stack.get_number_of_operations()
        return counter
            
    # tostring to print the section as a 2d grid of the length of each stack in both available and full stacks
    def __str__(self) -> str:
        return_string = ""
        for y in range(0, self.section_width):
            for x in range(0, self.section_length):
                for stack in self.available_container_stacks:
                    if stack.location_in_section == (x, y):
                        return_string += str(stack.operationCounter) + " "
                for stack in self.full_container_stacks:
                    if stack.location_in_section == (x, y):
                        return_string += str(stack.operationCounter) + " "
            return_string += "\n"
        return return_string
    

def main():
    # Create a ship section
    section = ShipSection(1, ship_dimensions[0]//6, ship_dimensions[1]//2, ship_dimensions[2])
    lightest_stack = section.get_lightest_container_stack()
    print(lightest_stack, "is the lightest stack")
    # Create a container
    container_set = ContainerSet()
    random.seed(42069)
    #container_set.generate_random_containers(696)




    # Print all the stacks in the section in as a 2d grid 
    for container in container_set.containers:
        section.add_container(container)


    print(section.get_number_of_operations_in_section(), "is the number of operations in the section")

        
    
    print(section.get_section_weight(), "is the section weight")
    print(section.get_lightest_container_stack(), "is the lightest stack")

    

    

    

if __name__ == "__main__":
    main()