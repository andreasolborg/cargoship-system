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
    
    ################################ Functions for task 5 ###########################################
    
    # Look for a container in the ship
    def get_nth_container(self, x, y, z):
        return self.containers[x][y][z]
    
    # Look for the first empty place in the ship where the container can be placed
    def get_first_empty_place_to_place_container(self):
        for height in range(self.height):
            for width in range(self.width):
                for length in range(self.length):
                    if self.get_nth_container(height, width, length) is None:
                        return height, width, length
        return None
    
    # Insert ("load") a container in the ship
    def insert_container(self, container, x, y, z):
        self.containers[x][y][z] = container
    
    # Remove ("unload") a container from the ship, and make sure it is on the uppermost layer. You cannot remove a container from the middle of the ship
    def remove_container(self, x, y, z):
        if x == self.height - 1:
            self.containers[x][y][z] = None
        else:
            print("You cannot remove a container from the middle of the ship")
     
    ################################    Task 5 finished         ######################################
    ################################    Functions for task 7    ######################################
    
    
    ################################    Functions for task 9 (these need further testing)        ######################################
    # The total weight of containers loaded the first, middle and last section of a ship (from the bow to the stern).
    def get_total_weight_of_containers_loaded_in_first_middle_and_last_section(self):
        first_section_weight = 0
        middle_section_weight = 0
        last_section_weight = 0
        for height in range(self.height):
            for width in range(self.width):
                for length in range(self.length):
                    if self.get_nth_container(height, width, length) is not None:
                        if length < self.length // 3:
                            first_section_weight += self.get_nth_container(height, width, length).get_weight() + self.get_nth_container(height, width, length).get_cargo()
                        elif length < self.length // 3 * 2:
                            middle_section_weight += self.get_nth_container(height, width, length).get_weight() + self.get_nth_container(height, width, length).get_cargo()
                        else:
                            last_section_weight += self.get_nth_container(height, width, length).get_weight() + self.get_nth_container(height, width, length).get_cargo()
        return first_section_weight, middle_section_weight, last_section_weight
    
    # Get The total weight of containers loaded on starboard and on portside of ship.
    def get_total_weight_of_containers_loaded_on_starboard_and_portside(self):
        starboard_weight = 0
        portside_weight = 0
        for length in range(self.length):
            for height in range(self.height):
                for width in range(self.width):
                    if self.get_nth_container(height, width, length) is not None:
                        if length < self.length // 2:
                            starboard_weight += (self.get_nth_container(height, width, length).get_weight() + self.get_nth_container(height, width, length).get_cargo())
                        else:
                            portside_weight += (self.get_nth_container(height, width, length).get_weight() + self.get_nth_container(height, width, length).get_cargo())
        return starboard_weight, portside_weight

    
    
    # Get number of containers in the 3d list
    def get_number_of_containers(self):
        set_of_container_codes = set()
        for height in range(self.height):
            for width in range(self.width):
                for length in range(self.length):
                    if self.get_nth_container(height, width, length) is not None:
                        set_of_container_codes.add(self.get_nth_container(height, width, length).get_code())  
        return len(set_of_container_codes)


    # Get all the containers that occur in the nth floor
    def get_all_containers_in_nth_floor(self, n):
        top_containers = []
        for height in range(self.height):
            for width in range(self.width):
                for length in range(self.length):
                    if self.get_nth_container(height, width, length) is not None and height == self.height - n:
                        top_containers.append(self.get_nth_container(height, width, length))
        return top_containers
    
    # Get the top containers in the ship (the ones that are not None in the uppermost layer)
    def get_all_top_containers(self):
        return self.get_all_containers_in_nth_floor(1)
    
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
                        
    def load_container_from_set_of_containers(self, container_set):
        for container in container_set.containers:
            self.load_container(container)
    
                        

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



def sort_containers_in_set_by_weight(ship, container_set):  
    container_set.containers = sorted(container_set.containers, key=lambda x: x.get_weight(), reverse=True)
    
    
def initialize_ship():
    ship = ContainerShip(23, 22, 18) # dimensions of the ship (length, width, height)
    container_set = load_set_of_containers("./solution/containers.tsv")
    container_set.containers = sorted(container_set.containers, key=lambda x: x.get_weight(), reverse=True)
    ship.load_container_from_set_of_containers(container_set)
    save_ship_with_containers_to_file(ship, "./solution/ship_load.tsv")

def main():
    #initialize_ship()
    ship = load_ship_with_containers_from_file("./solution/ship_load.tsv")
    
    

    
    
    
    
    #save_ship_with_containers_to_file(ship, "./solution/ship_load.tsv")
    
    # Print total weight of containers loaded on starboard and portside formatted as a string
    starboard_weight, portside_weight = ship.get_total_weight_of_containers_loaded_on_starboard_and_portside()
    print("Total weight of containers loaded on starboard: " + str(starboard_weight))
    print("Total weight of containers loaded on portside: " + str(portside_weight))
    
    # Print total weight in the front middle and back of the ship formatted as a string
    front_weight, middle_weight, back_weight = ship.get_total_weight_of_containers_loaded_in_first_middle_and_last_section()
    print("Total weight of containers loaded in front: " + str(front_weight))
    print("Total weight of containers loaded in middle: " + str(middle_weight))
    print("Total weight of containers loaded in back: " + str(back_weight))

    

    

if __name__ == "__main__":
    main()



# bredde : 