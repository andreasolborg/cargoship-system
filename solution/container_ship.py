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
    def get_first_empty_place_to_place_a_20_feet_container(self):
        for height in range(self.height):
            for width in range(self.width):
                for length in range(self.length):
                    if self.get_nth_container(height, width, length) is None:
                        return height, width, length
        return None
            

    def get_first_empty_place_to_place_a_40_feet_container(self):
        for height in range(self.height):
            for width in range(self.width):
                for length in range(self.length - 1): # The container is 2 cells long, so we need to check if the next cell is empty as well
                    if self.get_nth_container(height, width, length) is None and self.get_nth_container(height, width, length + 1) is None:
                        return height, width, length
        return None
    
    # Insert ("load") a container in the ship
    def insert_container(self, container, x, y, z):
        self.containers[x][y][z] = container
    
    # Remove ("unload") a container from the ship [WORKS WELL] (if it is a 40 feet container, it will remove the 2 cells)
    def remove_container(self, container):
        for height in range(self.height):
            for width in range(self.width):
                for length in range(self.length):
                    if self.get_nth_container(height, width, length) is container:
                        self.insert_container(None, height, width, length)
                        # If the container is 40 feet long, then we need to remove the 2 cells
                        if container.get_length() == 40:
                            self.insert_container(None, height, width, length + 1)
    
         
    def get_container_above(self, container):
        for height in range(self.height - 1, -1, -1):
            for width in range(self.width):
                for length in range(self.length):
                    if self.get_nth_container(height, width, length) is container:
                        return self.get_nth_container(height + 1, width, length)
        return None
       
    def remove_container_if_nothing_is_ontop_of_container(self, container):
        if self.get_container_above(container) is None:
            self.remove_container(container)
        else:
            print("There is a container on top of the container you want to remove")
        
        

    # Function to get the last element in the 3d list
    def get_highest_level_of_container(self):
        for height in range(self.height - 1, -1, -1):
            for width in range(self.width):
                for length in range(self.length):
                    if self.get_nth_container(height, width, length) is not None:
                        return height, width, length, self.get_nth_container(height, width, length).get_length()
        return None
    
    
    ##### MAY BE REMOVED LATER ########
    # Remove a container from the ship using get_highest_level_of_container function
    def remove_container_at_highest_level(self):
        if(self.get_highest_level_of_container()[3] == 20):
            self.remove_container_at_position(self.get_highest_level_of_container()[0], self.get_highest_level_of_container()[1], self.get_highest_level_of_container()[2])
        elif(self.get_highest_level_of_container()[3] == 40):
            self.remove_container_at_position(self.get_highest_level_of_container()[0], self.get_highest_level_of_container()[1], self.get_highest_level_of_container()[2])
            self.remove_container_at_position(self.get_highest_level_of_container()[0], self.get_highest_level_of_container()[1], self.get_highest_level_of_container()[2])
        
        

     
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

    # Get the total weight of containers loaded on the ship
    def get_total_weight_of_containers_loaded_on_ship(self):
        total_weight = 0
        for height in range(self.height):
            for width in range(self.width):
                for length in range(self.length):
                    if self.get_nth_container(height, width, length) is not None:
                        total_weight += self.get_nth_container(height, width, length).get_weight() + self.get_nth_container(height, width, length).get_cargo()
        return total_weight
  
  ############################################################################################################
    
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
    def get_all_containers_in_nth_floor_from_top(self, n):
        top_containers = []
        for height in range(self.height):
            for width in range(self.width):
                for length in range(self.length):
                    if self.get_nth_container(height, width, length) is not None and height == self.height - n:
                        top_containers.append(self.get_nth_container(height, width, length))
        return top_containers
    
    # Get the top containers in the ship (the ones that are not None in the uppermost layer)
    def get_all_top_containers(self):
        return self.get_all_containers_in_nth_floor_from_top(1)
    
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
    
    # load containers using get_first_empty_place_to_place_a_20_feet_container function, get_first_empty_place_to_place_a_40_feet_container function, and insert_container function
    def load_container(self, container):
        container_length = container.get_length()
        if container_length == 20:
            if self.get_first_empty_place_to_place_a_20_feet_container() is not None:
                h, w, l = self.get_first_empty_place_to_place_a_20_feet_container()
                self.insert_container(container, h, w, l)
        elif container_length == 40:
            if self.get_first_empty_place_to_place_a_40_feet_container() is not None:
                h, w, l = self.get_first_empty_place_to_place_a_40_feet_container()
                self.insert_container(container, h, w, l)
                self.insert_container(container, h, w, l + 1)
            
        

    def load_container1(self, container):
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
                        ship_str += " XX-XX"
                    else:
                        ship_str += " " + str(container.get_code()) +"-"+ str(container.get_length())
                ship_str += "\n"
            ship_str += "\n"
        return ship_str



def sort_containers_in_set_by_weight(ship, container_set):  
    container_set.containers = sorted(container_set.containers, key=lambda x: x.get_weight(), reverse=True)
    
    
def initialize_ship():
    ship = ContainerShip(3, 5, 3) # dimensions of the ship (length, width, height)
    container_set = load_set_of_containers("./solution/containers.tsv")
    #container_set.containers = sorted(container_set.containers, key=lambda x: x.get_weight(), reverse=True)
    ship.load_container_from_set_of_containers(container_set)
    save_ship_with_containers_to_file(ship, "./solution/small_ship_load.tsv")

def main():
    #initialize_ship()
    
    small_ship = load_ship_with_containers_from_file("./solution/small_ship_load_3x5x3.tsv")
    print(small_ship)
    
    # Remove the containers from the ship
    top_containers = small_ship.get_all_top_containers()
    for i in top_containers:
        small_ship.remove_container(i)


    print(small_ship)
    
    container = small_ship.get_nth_container(1, 0, 0)
    print(container)
    small_ship.remove_container_if_nothing_is_ontop_of_container(container)
    
    container = small_ship.get_nth_container(1, 1, 1)
    small_ship.remove_container_if_nothing_is_ontop_of_container(container)

    
    container = small_ship.get_nth_container(0, 0, 0)
    small_ship.remove_container_if_nothing_is_ontop_of_container(container)
    print(small_ship)
    
    
    container_set = load_set_of_containers("./solution/small_container_set.tsv")
    for container in container_set.containers:
        small_ship.load_container(container)
    
    
    print(small_ship)
    
    
if __name__ == "__main__":
    main()



# bredde : 