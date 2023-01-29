from container import *
from container_set import *
from container_set_manager import *
from container_ship_manager import *

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
    
    # Get number of containers in the 3d list
    def get_number_of_containers(self):
        set_of_container_codes = set()
        for height in range(self.height):
            for width in range(self.width):
                for length in range(self.length):
                    if self.get_nth_container(height, width, length) is not None:
                        set_of_container_codes.add(self.get_nth_container(height, width, length).get_code())  
        return len(set_of_container_codes)
    
    def get_nth_container(self, x, y, z):
        return self.containers[x][y][z]
    

    def get_top_container(self):
        if len(self.containers) == 0:
            return None
        return self.containers[-1]
    
    # Functionalities
    
    # Pushes container to the end of the 3d-list
    def push_container(self, container):
        for height in range(self.height):
            for width in range(self.width):
                for length in range(self.length):
                    if self.get_nth_container(height, width, length) is None:
                        self.insert_container(container, height, width, length)
                        return
        print("No room for the container")
        

    def insert_container(self, container, x, y, z):
        self.containers[x][y][z] = container
        
    
    def remove_nth_container(self, n):
        self.containers.pop(n)
    
    def pop_container(self):
        if len(self.containers) == 0:
            return None
        self.containers.pop()


    def load_container(self, container):
        container_length = container.get_length()
        if container_length == 20:
            for height in range(self.height):
                for width in range(self.width):
                    for length in range(self.length):
                        if self.get_nth_container(height, width, length) is None:
                            self.insert_container(container, height, width, length)
                            return
        elif container_length == 40:
            for height in range(self.height):
                for width in range(self.width):
                    for length in range(self.length - 1): # -1 because of the 40 foot container can't be placed at the end of the ship
                        if self.get_nth_container(height, width, length) is None and self.get_nth_container(height, width, length + 1) is None:
                            self.insert_container(container, height, width, length)
                            self.insert_container(container, height, width, length + 1)
                            return


    def __str__(self):
        ship_str = ""
        for h in range(self.height):
            ship_str += "Floor " + str(h) + "\n"
            for l in range(self.length):
                for w in range(self.width):
                    container = self.containers[h][w][l]
                    if container is None:
                        ship_str += " XX"
                    else:
                        ship_str += " " + str(container.get_code())
                ship_str += "\n"
            ship_str += "\n"
        return ship_str



def load_containers_on_ship(ship, container_set):  
    #container_set.containers = sorted(container_set.containers, key=lambda x: x.get_weight(), reverse=True)
    for container in container_set.containers:
        ship.load_container(container)
    

def main():
    #ship = ContainerShip(7, 13, 5) # dimensions of the ship (length, width, height)
    #container_set = load_set_of_containers("containers.tsv")
    #container_set.containers = sorted(container_set.containers, key=lambda x: x.get_weight(), reverse=True)
    #load_containers_on_ship(ship, container_set)
    ship = load_ship_with_containers_from_file("./solution/ship_load.tsv")
    
    
    #print(ship)
    #save_ship_with_containers_to_file(ship, "./solution/ship_load.tsv")
    
    print(ship.get_nth_container(1, 0, 1))
      


if __name__ == "__main__":
    main()



# bredde : 