from container import Container

class ShipSection:
    def __init__(self, container_ship, length, width, height):
        self.width = container_ship.width
        self.length = container_ship.length
        self.height = container_ship.height
        self.stacks = [[[] for j in range(self.width)] for i in range(self.length)]
        self.empty_places = []
        for i in range(self.length):
            for j in range(self.width):
                self.empty_places.append((i, j))



        self.holder_for_20feet_containers = []
    
    def get_height(self):
        return self.height


        
    ##find the stack in the section 
    ## Fill up one stack with container from the container_set until the stack is full. A cell consist of 2 20feet containers or 1 40feet container
    def add_container(self, container):
        #if the container is a 20feet container
        if container.length == 20:
            #if the holder is empty
            if not self.holder_for_20feet_containers:
                #add the container to the holder
                self.holder_for_20feet_containers.append(container)
            #if the holder is not empty
            else:
                #add the container to the holder
                self.holder_for_20feet_containers.append(container)
                #find the first empty place in the section
                first_empty_place = self.empty_places[0]
                #add the holder to the stack
                self.stacks[first_empty_place[0]][first_empty_place[1]].append(self.holder_for_20feet_containers)
                #remove the first empty place from the list of empty places
                self.empty_places.remove(first_empty_place)
                #empty the holder
                self.holder_for_20feet_containers = []
        #if the container is a 40feet container
        else:
            #find the first empty place in the section
            first_empty_place = self.empty_places[0]
            #add the container to the stack
            self.stacks[first_empty_place[0]][first_empty_place[1]].append(container)
            #remove the first empty place from the list of empty places
            self.empty_places.remove(first_empty_place)

    
    def get_stacks(self):
        return self.stacks
    
    def get_stack(self, length, width):
        return self.stacks[length][width]

    def get_weight(self):
        weight = 0
        for stack in self.stacks:
            for container in stack:
                weight += container.weight
        return weight

    def get_amount_of_containers(self):
        amount = 0
        for stack in self.stacks:
            amount += len(stack)
        return amount
    
    def get_amount_of_stacks(self):
        return len(self.stacks)
