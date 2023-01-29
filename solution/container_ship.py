from container import *
from container_set import *
from container_manager import *

class ContainerShip:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.containers = [[[None for z in range(self.length)] for y in range(self.width)] for x in range(self.height)]

    def get_ship_length(self):
        return self.length 
    
    def get_ship_width(self):
        return self.width
    
    def get_ship_height(self):
        return self.height
    
    def get_containers(self):
        return self.containers
    
    def get_number_of_containers(self):
        return len(self.containers)
    
    def get_nth_container(self, n):
        return self.containers[n]

    def get_top_container(self):
        if len(self.containers) == 0:
            return None
        return self.containers[-1]
    
    # Functionalities

    def append_container(self, container):
        self.containers.append(container)

    def push_container(self, container): # Pushes container to the end of the list
        self.containers.append(container)    

    def insert_container(self, container, n):
        self.containers.insert(n, container)
    
    def remove_nth_container(self, n):
        self.containers.pop(n)
    
    def pop_container(self):
        if len(self.containers) == 0:
            return None
        self.containers.pop()


    def load_container(self, container):
        length = container.get_length()
        if length == 20:
            for height in range(self.height):
                for width in range(self.width):
                    for length in range(self.length):
                        if self.get_containers()[height][width][length] is None:
                            self.get_containers()[height][width][length] = container
                            return
        elif length == 40:
            for height in range(self.height):
                for width in range(self.width):
                    for length in range(self.length - 1):
                        if self.get_containers()[height][width][length] is None and self.get_containers()[height][width][length + 1] is None:
                            self.get_containers()[height][width][length] = container
                            self.get_containers()[height][width][length + 1] = container
                            return


    def __str__(self):
        ship_str = ""
        for h in range(self.height):
            for w in range(self.width):
                for l in range(self.length):
                    container = self.containers[h][w][l]
                    if container is None:
                        ship_str += "[ooooooo]"
                    else:
                        ship_str += str(container.get_code() + " ")
                ship_str += "\n"
            ship_str += "\n"
        return ship_str



def main():
    ship = ContainerShip(7, 5, 3) # dimensions of the ship (length, width, height)
    #load containers from file
    container_set = load_set_of_containers("containers.tsv")
    #container_set.containers = sorted(container_set.containers, key=lambda x: x.get_weight(), reverse=True)
    
    #load containers on ship
    for container in container_set.containers:
        ship.load_container(container)

    print(ship)


if __name__ == "__main__":
    main()



# bredde : 