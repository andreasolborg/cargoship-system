# Author: Andreas Olborg - Group 47
from Container import *

class ContainerStack:
    def __init__(self, section_id, location_in_section, max_stack_height):
        self.section_id = section_id
        self.max_stack_height = max_stack_height
        self.location_in_section = location_in_section
        self.number_of_containers = 0
        self.stack_weight = 0
        self.top_weight = 0
        self.containers = [] # List of containers in the stack
        self.operationCounter = 0
    
    # Get functions 
    def get_section_id(self):
        return self.section_id

    def get_max_stack_height(self):
        return self.max_stack_height

    def get_location_in_section(self):
        return self.location_in_section

    def get_stack_weight(self):
        return self.stack_weight

    def get_number_of_containers(self):
        return self.number_of_containers
        
    def get_container(self, index):
        return self.containers[index]
    
    def get_containers(self):
        return self.containers

    def get_number_of_operations(self):
        return self.operationCounter

    def get_stack_height(self):
        return len(self.containers)

    def get_weight_at_height_level(self, height_level):
        weight_at_height_level = 0
        if height_level >= len(self.containers):
            return 0
        else:
            for container in self.get_container(height_level):
                weight_at_height_level += container.get_total_weight()
            return weight_at_height_level

    def container_stack_is_full(self):
        if len(self.containers) == self.max_stack_height:
            return True
        else:
            return False
    
    def container_stack_is_empty(self):
        if len(self.containers) == 0:
            return True
        else:
            return False
        

    # tostring
    def __str__(self) -> str:
        return f"Container stack in section {self.section_id} at location {self.location_in_section} stackweight:{self.stack_weight} #containers:{self.get_number_of_containers()}"
    
    # Updating top weight so that sorting is easier
    def update_top_weight(self):
        if len(self.containers) == 0:
            self.top_weight = 0
        else:                                   # If there are containers in the stack check if the top container is a single container or a list of two containers
            if len(self.containers[-1]) == 1:   # Method for getting the top weight of the stack
                containers = self.containers[-1]
                self.top_weight = containers[0].get_total_weight()
            elif len(self.containers[-1]) == 2:
                containers = self.containers[-1]
                self.top_weight = containers[0].get_total_weight() + containers[1].get_total_weight()
            else:
                raise Exception("Container must be a single container or a list of two containers")
                              
    def push_container_to_stack(self, container):
        if not self.container_stack_is_full():
            if type(container) is not list:
                container = [container]
            if len(container) == 1:
                self.containers.append(container)
                self.stack_weight += container[0].get_total_weight()
                self.number_of_containers += 1
            elif len(container) == 2:
                self.containers.append(container)
                self.stack_weight += (container[0].get_total_weight() + container[1].get_total_weight())
                self.number_of_containers += 2
            else:
                raise Exception("Container must be a single container or a list of two containers")
            self.operationCounter += len(container)
            self.update_top_weight()
        else:
            raise Exception("Container stack is full")
        
    # Add container to stack using push and pop functions such that the stack is always sorted by weight. 
    # If the container is 20-feet it must be placed in a temporary list to ensure 20-feet containers always get loaded as a pair later
    def add_container_to_stack(self, container):
        if type(container) is Container:
            if container.get_length() == 20:
                raise Exception("A single 20-foot container cannot be loaded to a container stack")
            container_weight = container.get_total_weight()
            container = [container]
        else:
            if len(container) == 1:
                container_weight = container[0].get_total_weight()
            else:
                if container[0].get_length() == 40:
                    raise Exception("You cannot load two 40-feet containers at the same time")
                container_weight = sum(c.get_total_weight() for c in container)
        temporary_storing_stack = []
        while container_weight > self.top_weight and self.top_weight != 0:
            temporary_storing_stack.append(self.pop_container_from_stack())
        temporary_storing_stack.append(container)
        for temp_stack_pop in reversed(temporary_storing_stack):
            self.push_container_to_stack(temp_stack_pop)
        
    def pop_container_from_stack(self):
        if len(self.containers) == 0:
            raise Exception("Stack is empty")
        else:
            container = self.containers.pop()
            for c in container:
                self.stack_weight -= c.get_total_weight()
                self.operationCounter += 1
            self.number_of_containers -= len(container)
            self.update_top_weight()
            return container

    # Remove container from stack using pop and push functions such that the stack is always sorted by weight. We use a temporary list to store the containers that are popped from the stack and then push them back to the stack after the container is removed
    def remove_container_from_stack(self, container):
        if len(self.containers) == 0:
            raise Exception("Stack is empty")
        else:
            temporary_storing_stack = []
            while container not in self.containers[-1]:
                temporary_storing_stack.append(self.pop_container_from_stack())
            self.pop_container_from_stack()
            for temp_stack_pop in reversed(temporary_storing_stack):
                self.push_container_to_stack(temp_stack_pop)
            
        
    # Tostring function
    def __str__(self) -> str:
        return f"Container stack at location {self.location_in_section}, has an operation counter of {self.operationCounter} and a stack weight of {self.stack_weight} tons"

    def print_stack_as_list(self):
        for container in self.containers:
            for c in container:
                print(c)


def main():
    
    # Create a new stack for testing purposes
    stack = ContainerStack("A", (0, 0), 18)

    # Create 4 empty containers
    c1 = Container(1, 40, 4, 0, 22) # Container(id, length, width, weight, max_weight)
    c2 = Container(2, 40, 4, 0, 22)
    c3 = Container(3, 40, 4, 0, 22)
    c4 = Container(4, 40, 4, 0, 22)
    
    # Create containers with 20 tons of cargo
    c5 = Container(5, 40, 4, 20, 22)
    c6 = Container(6, 40, 4, 20, 22)
    c7 = Container(7, 40, 4, 20, 22)
    
    #Create a full 40-feet container
    c8 = Container(8, 40, 4, 22, 22)
    
    # Create 2 Full 20-feet containers
    c9 = Container(9, 20, 2, 18, 20)
    c10 = Container(10, 20, 2, 18, 20)
    
    c11 = Container(11, 20, 2, 20, 20)
    c12 = Container(12, 20, 2, 20, 20)

    ## Add every 40-feet container to the set of containers, and then add them to the stack
    container_set = [c1, c2, c3, c4, c5, c6, c7, c8]
    for container in container_set:
        stack.add_container_to_stack(container)
    
    # Print the stack, and the operation counter. Should be 46
    print("printing container at index 0", stack.get_container(0))
    print("printing weights at each level in the stack", stack.get_weight_at_height_level(0))


    # Create a new stack for testing purposes
    stack2 = ContainerStack("B", (1, 0), 18)
    

    container_set.clear()
    container_set = [c1, c2, c3, c4, c5, c6, c7, [c9, c10], [c11, c12]]
    
    for container in container_set:
        stack2.add_container_to_stack(container)
    
    # Print the stack, and the operation counter. Should be 67
    print(stack2)
    stack2.print_stack_as_list()
    print(stack2.get_number_of_containers(), "containers in stack")

    # Remove a container from the stack
    stack2.remove_container_from_stack(c12)

    print("\n------------------ After removing container 12 ------------------")
    stack2.print_stack_as_list()

    print(stack2.get_number_of_containers(), "containers in stack")
    print("printing weights at each level in the stack", stack2.get_weight_at_height_level(0))


        
    
        
if __name__ == "__main__":
    main()
