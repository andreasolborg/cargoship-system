from Container import Container
from ContainerStack import ContainerStack
from ContainerSetManager import *
from ContainerSet import *

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
        self.number_of_operations = 0
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

    def get_number_of_operations(self):
        return self.number_of_operations

    def get_holding_containers(self):
        return self.holding_containers
    
    def get_available_container_stacks(self):
        return self.available_container_stacks

    def get_full_container_stacks(self):
        return self.full_container_stacks

    def get_container_stacks(self):
        return self.available_container_stacks + self.full_container_stacks
    

    # Get section weight by adding up the weight of all stacks in full and available stacks
    def get_section_weight(self):
        section_weight = 0
        for stack in self.get_container_stacks():
            section_weight += stack.get_stack_weight()
        return section_weight
        
        
    def get_lightest_container_stack(self):
        if len(self.available_container_stacks) == 0:
            return "No stacks in section"
        lightest_stack = self.available_container_stacks[0]
        for stack in self.available_container_stacks:
            if stack.get_stack_weight() < lightest_stack.get_stack_weight():
                lightest_stack = stack
        return lightest_stack

    def get_heaviest_container_stack(self):
        heaviest_stack = self.get_container_stacks()[0]
        for stack in self.get_container_stacks():
            if stack.get_stack_weight() > heaviest_stack.get_stack_weight():
                heaviest_stack = stack
        return heaviest_stack
    
    def get_number_of_containers(self):
        number_of_containers = 0
        for stack in self.get_container_stacks():
            number_of_containers += stack.get_number_of_containers()
        return number_of_containers

    
    def get_stack(self, stack_location: tuple):
        for stack in self.get_container_stacks():
            if stack.location_in_section == stack_location:
                return stack
        return None

    def get_weight_per_height_level_in_section(self):
        weight_per_height_level = []
        for height_level in range(0, self.max_stack_height):
            weight_per_height_level.append(0)
        for stack in self.get_container_stacks():
            for height_level in range(0, self.max_stack_height):
                weight_per_height_level[height_level] += stack.get_weight_at_height_level(height_level)
        return weight_per_height_level


    # Functionalities
    def is_section_full(self):
        if len(self.available_container_stacks) == 0:
            return True
        else:
            return False

    def is_section_empty(self):
        if len(self.get_container_stacks()) == 0:
            return True
        else:
            return False

    def add_holding_container(self, container):
        self.holding_containers.append(container)


    def add_container_to_section(self, container):
        if self.is_section_full() == True:
            return
            raise Exception("Container stack is full, cannot add container, with ID: " + container.get_code())
        else:    
            container_stack = self.get_lightest_container_stack()
            if container_stack.container_stack_is_full() == True:
                self.full_container_stacks.append(container_stack)
                self.available_container_stacks.remove(container_stack)
                self.add_container_to_section(container)
            else:
                if container.get_length() == 20 and self.holding_containers == []:
                    self.holding_containers.append(container)
                elif container.get_length() == 20 and self.holding_containers != []:
                    self.holding_containers.append(container)
                    container_stack.add_container_to_stack([self.holding_containers[0], self.holding_containers[1]])
                    self.holding_containers = []
                elif container.get_length() == 40:
                    container_stack.add_container_to_stack(container)
                self.section_weight += container.get_weight()


    def pop_container_from_heaviest_stack(self):
        heaviest_stack = self.get_heaviest_container_stack()
        if heaviest_stack.container_stack_is_empty() == True:
            raise Exception("Heaviest stack is empty, cannot pop container")
        else:               
            container = heaviest_stack.pop_container_from_stack()
            for c in container:
                self.section_weight -= c.get_total_weight()
            return container

                
        
    def get_number_of_operations_in_section(self):
        counter = 0
        for stack in self.get_container_stacks():
            counter += stack.get_number_of_operations()
        return counter


    def insert_stack_at_location(self, stack, location):
        stack.location_in_section = location
        self.available_container_stacks.append(stack)
        self.full_container_stacks.remove(stack)
        self.section_weight += stack.get_stack_weight()



            
    # tostring to print the section as a 2d grid of the length of each stack in both available and full stacks
    def __str__(self) -> str:
        return_string =  "Section ID: " + str(self.sectionID) + "\n#OPERATIONS:[height]-[WEIGHT]\n"
        total = 0
        for y in range(0, self.section_width):
            for x in range(0, self.section_length):
                for stacks in self.get_container_stacks():
                    if stacks.location_in_section == (x, y):
                        return_string += str(stacks.get_number_of_operations()) + "--" + str(stacks.get_stack_height()) + "--" + str(stacks.get_stack_weight()) + "\t"
                        total += stacks.get_stack_weight()
            return_string += "\n"
            
        return_string += "Total section weight: " + str(total) + "\n"
        return_string += "Total number of operations: " + str(self.get_number_of_operations_in_section()) + "\n"
        return return_string
    

def main():
    # Create a ship section
    section = ShipSection(1, ship_dimensions[0]//6, ship_dimensions[1]//2, ship_dimensions[2])
    lightest_stack = section.get_lightest_container_stack()
    #print(lightest_stack, "is the lightest stack, ")
    # Create a container
    container_set = ContainerSet()
    random.seed(420)
    container_set.generate_random_containers(1500)

    # Print all the stacks in the section in as a 2d grid 
    for container in container_set.containers:
        try:
            section.add_container_to_section(container)
        except Exception as e:
            print(e)
            break
    print(section)
    stack_to_inspect = section.get_stack((0, 0))
    print(stack_to_inspect.get_location_in_section(),"List:", stack_to_inspect.get_containers(),
          "Weight", stack_to_inspect.get_stack_weight(),
          "Height", stack_to_inspect.get_stack_height(),
          "#operations:", stack_to_inspect.get_number_of_operations(),
          "#containers:", stack_to_inspect.get_number_of_containers()
          )
    stack_to_inspect = section.get_stack((0, 1))
    print(stack_to_inspect.get_location_in_section(),"List:", stack_to_inspect.get_containers(),
          "Weight", stack_to_inspect.get_stack_weight(),
          "Height", stack_to_inspect.get_stack_height(),
          "#operations:", stack_to_inspect.get_number_of_operations(),
          "#containers:", stack_to_inspect.get_number_of_containers()
          )
    stack_to_inspect = section.get_stack((0, 2))
    print(stack_to_inspect.get_location_in_section(),"List:", stack_to_inspect.get_containers(),
          "Weight", stack_to_inspect.get_stack_weight(),
          "Height", stack_to_inspect.get_stack_height(),
          "#operations:", stack_to_inspect.get_number_of_operations(),
          "#containers:", stack_to_inspect.get_number_of_containers()
          )
    stack_to_inspect = section.get_stack((0, 3))
    print(stack_to_inspect.get_location_in_section(),"List:", stack_to_inspect.get_containers(),
          "Weight", stack_to_inspect.get_stack_weight(),
          "Height", stack_to_inspect.get_stack_height(),
          "#operations:", stack_to_inspect.get_number_of_operations(),
          "#containers:", stack_to_inspect.get_number_of_containers()
          )
    
    # print(section, "is the section")
    # print(section.get_number_of_operations_in_section(), "is the number of operations in the section")
    # print(section.get_section_weight(), "is the section weight")
    print(section.get_lightest_container_stack(), "is the lightest stack")
    print(section.get_number_of_operations_in_section(), "is the number of operations in the section")


    popped_container = section.pop_container_from_heaviest_stack()
    print(popped_container, "is the popped container")
    popped_container = section.pop_container_from_heaviest_stack()
    print(popped_container, "is the popped container")

    weightlist = section.get_weight_per_height_level_in_section()
    print(weightlist, "is the weightlist")

if __name__ == "__main__":
    main()