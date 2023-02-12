from container import *

class ContainerStack:
    def __init__(self, sectionID, location_in_section, max_stack_height):
        self.sectionID = sectionID
        self.max_stack_height = max_stack_height
        self.location_in_section = location_in_section
        self.x_location, self.y_location = location_in_section
        self.temporary_containers = [] # List for temporary storage of containers outside of the stack, may be removed
        self.number_of_containers = 0
        self.stack_weight = 0
        self.top_weight = 0
        self.containers = [] # List of containers in the stack
        self.operationCounter = 0
    
    # Get functions 
    def get_sectionID(self):
        return self.sectionID

    def get_max_stack_height(self):
        return self.max_stack_height

    def get_location_in_section(self):
        return self.location_in_section

    def get_temporary_containers(self):
        return self.temporary_containers

    def get_stack_weight(self):
        return self.stack_weight

    def get_number_of_containers(self):
        for container in self.containers:
            if len(container) == 1:
                self.number_of_containers += 1
            elif len(container) == 2:
                self.number_of_containers += 2
        return self.number_of_containers

    def get_number_of_operations(self):
        return self.operationCounter

    def get_stack_height(self):
        return len(self.containers)

    def container_stack_is_full(self):
        if len(self.containers) == self.max_stack_height:
            return True
        else:
            return False


    # Set functions
    def set_sectionID(self, sectionID):
        self.sectionID = sectionID

    def set_max_stack_height(self, max_stack_height):
        self.max_stack_height = max_stack_height

    def set_location_in_section(self, location_in_section):
        if len(location_in_section) != 2:
            raise Exception("Location in section must be a tuple of length 2") #Trying out Exceptions
        self.location_in_section = location_in_section

    def set_containers(self, containers):
        self.containers = containers


    def set_weight(self, weight):
        self.weight = weight

    # tostring
    def __str__(self) -> str:
        return f"Container stack in section {self.sectionID} at location {self.location_in_section} with a stack weight of {self.stack_weight} tons"
    
    # Updating top weight so that sorting is easier
    def update_top_weight(self):
        if len(self.containers) == 0:
            self.top_weight = 0
        else: # If there are containers in the stack check if the top container is a single container or a list of two containers
            if len(self.containers[-1]) == 1:   ## Method for getting the top weight of the stack
                containers = self.containers[-1]
                self.top_weight = containers[0].get_total_weight()
            elif len(self.containers[-1]) == 2:
                containers = self.containers[-1]
                self.top_weight = containers[0].get_total_weight() + containers[1].get_total_weight()
                      
        
    def push_container_to_stack(self, container): # Dont check for length of container, just check if it is a list or not and then add it to the stack
        if len(self.containers) == self.max_stack_height:
            raise Exception("Container stack is full")
        else:
            if len(container) == 1: # If container is a single container
                self.containers.append(container)
                self.stack_weight += container[0].get_total_weight()
                self.operationCounter += 1
                #print(self.operationCounter, "Operation counter")
            else:
                if len(container) == 2: # If container is a list of two containers
                    self.containers.append(container)
                    container_weight = container[0].get_total_weight() + container[1].get_total_weight()
                    self.stack_weight += container_weight
                    self.operationCounter += 2
                    #print(self.operationCounter, "Operation counter")
                else:
                    raise Exception("Container must be a single container or a list of two containers")
            self.update_top_weight()
        

    # Add container to stack using push and pop functions such that the stack is always sorted by weight. 
    # If the container is 20-feet it must be placed in a temporary list to ensure 20-feet containers always get loaded as a pair later
    def add_container_to_stack(self, container):
        if type(container) is Container:                            # If container is a single container and not a list of containers
            if container.get_length() == 20:                        # If container is a 20-feet container 
                raise Exception(                                    # Raise an exception
                    'A single 20 foot container cannot be loaded to a containerStack') 
            else:
                container_weight = container.get_total_weight()
                container = [container]                             # Make container a list of one container to make it easier to handle later
        else:
            if len(container) == 1: 
                container_weight = container[0].get_total_weight() 
            else:
                if container[0].get_length() == 40:
                    raise Exception(
                        "You cannot load two 40-feet containers at the same time")
                else:
                    container_weight = container[0].get_total_weight() + container[1].get_total_weight()
        ### Stack-Sorting algorithm ###
        temporary_storing_stack = [] 
        while container_weight > self.top_weight and self.top_weight != 0:
            temporary_storing_stack.append(self.pop_container_from_stack())
        temporary_storing_stack.append(container)
        while len(temporary_storing_stack) > 0:
            temp_stack_pop = temporary_storing_stack.pop()
            self.push_container_to_stack(temp_stack_pop)

                
    def pop_container_from_stack(self):
        if len(self.containers) == 0:
            raise Exception("Stack is empty")
        else:
            container = self.containers.pop()
            if type(container) == Container:                            #This may be removed
                self.stack_weight -= container.get_total_weight()        #This may be removed
                self.operationCounter += 1                                  #This may be removed
            else:
                for c in container:
                    self.stack_weight -= c.get_total_weight()
                    self.operationCounter += 1
            self.update_top_weight()
            return container


    def get_temporary_containers_total_weight(self):
        total_weight = 0
        for container in self.temporary_containers:
            total_weight += container.get_total_weight()
        return total_weight
        
    # print the stack as a nested list, where each element is a list of containers shown as a string (e.g. [first container code, second container code])
    def print_stack_as_nested_list(self):
        print("Printing stack as nested list")
        print(self.containers)

    # Tostring function
    def __str__(self) -> str:
        return f"Container stack at location {self.location_in_section}, has an operation counter of {self.operationCounter} and a stack weight of {self.stack_weight} tons"

# Main function that creates a container stack and adds 10 containers to it
def main():
    


    stack = ContainerStack("A", (0, 0), 18)
    c1 = Container(1, 40, 4, 0, 22) # Container(id, length, width, weight, max_weight)
    c2 = Container(2, 40, 4, 0, 22)
    c3 = Container(3, 40, 4, 0, 22)
    c4 = Container(4, 40, 4, 0, 22)
    c5 = Container(5, 40, 4, 0, 22)
    c6 = Container(6, 40, 4, 0, 22)
    c7 = Container(7, 40, 4, 0, 22)
    c8 = Container(8, 40, 4, 0, 22)
    c9 = Container(9, 40, 4, 0, 22)
    c10 = Container(10, 40, 4, 22, 22)
    c11 = Container(11, 40, 4, 22, 22)
    c12 = Container(12, 40, 4, 22, 22)
    c13 = Container(13, 40, 4, 22, 22)
    c14 = Container(14, 40, 4, 22, 22)
    c15 = Container(15, 40, 4, 22, 22)
    c16 = Container(16, 40, 4, 22, 22)
    c17 = Container(17, 40, 4, 22, 22)
    c18 = Container(18, 20, 2, 20, 20)
    c19 = Container(19, 20, 2, 20, 20)

    ## Add all the containers to the container set
    container_set = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, [c18, c19]]
    for container in container_set:
        stack.add_container_to_stack(container)
    

    print(stack)

    stack.print_stack_as_nested_list()
    



        
if __name__ == "__main__":
    main()
