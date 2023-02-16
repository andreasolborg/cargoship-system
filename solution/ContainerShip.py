import time
from Container import *
from ContainerSet import *
from ContainerSetManager import *
from ContainerShipManager import *
from ContainerStack import *
from ShipSection import *

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

        self.list_of_unloaded_containers = []  # List of containers that are not in the ship

    # ------------------ Get functions ------------------
    def get_ship_length(self):
        return self.length

    def get_ship_width(self):
        return self.width

    def get_ship_height(self):
        return self.height

    def get_sections(self):
        return self.available_sections + self.full_sections
    
    def     get_number_of_operations(self):
        self.number_of_operations = 0
        for section in self.get_sections():
            self.number_of_operations += section.get_number_of_operations_in_section()
        return self.number_of_operations
   
    def get_lightest_section(self):
        lightest_section = self.available_sections[0]
        for section in self.available_sections:
            if section.get_section_weight() < lightest_section.get_section_weight():
                lightest_section = section
        return lightest_section

    def get_heaviest_section(self):
        heaviest_section = self.get_sections()[0]
        for section in self.get_sections():
            if section.get_section_weight() > heaviest_section.get_section_weight():
                heaviest_section = section
        if heaviest_section.is_section_empty() == True:
            return "No containers on ship."
        return heaviest_section

    def get_weight_per_height_level(self):
        weight_per_height_level = []
        for i in range(self.height):
            weight_per_height_level.append(0)
        for section in self.get_sections():
            for i in range(self.height):
                weight_per_height_level[i] += section.get_weight_per_height_level_in_section()[i]
        return weight_per_height_level
    
    def get_number_of_containers_on_ship(self):
        number_of_containers = 0
        for section in self.get_sections():
            number_of_containers += section.get_number_of_containers()
        return number_of_containers

    def get_stacks_that_are_not_full(self):
        stacks_that_are_not_full = []
        for section in self.get_sections():
            for stack in section.get_container_stacks():
                if stack.container_stack_is_full() == False:
                    stacks_that_are_not_full.append(stack)
        return stacks_that_are_not_full

    def get_amount_of_unloaded_containers(self):
        amount_of_unloaded_containers = 0
        for container_list in self.list_of_unloaded_containers:
            for container in container_list:
                amount_of_unloaded_containers += 1
        return amount_of_unloaded_containers

    def get_single_crane_loading_operation_counter(self):
        return self.get_number_of_operations()

    # We always remove the container from the top of the stack, so the number of operations is equal to the number of containers on the ship
    def get_single_crane_unloading_operation_counter(self): 
        return self.get_number_of_containers_on_ship()

    def get_max_triple_crane_loading_operation_counter(self):
        sections = self.get_sections()
        front_crane_loading_operation_count = sections[0].get_number_of_operations_in_section() + sections[1].get_number_of_operations_in_section()
        middle_crane_loading_operation_count = sections[2].get_number_of_operations_in_section() + sections[3].get_number_of_operations_in_section()            
        back_crane_loading_operation_count = sections[4].get_number_of_operations_in_section() + sections[5].get_number_of_operations_in_section()
        return max(front_crane_loading_operation_count, middle_crane_loading_operation_count, back_crane_loading_operation_count)
    
    def get_max_triple_crane_unloading_operation_counter(self):
        sections = self.get_sections()
        front_section_container_count = sections[0].get_number_of_containers() + sections[1].get_number_of_containers()
        middle_section_container_count = sections[2].get_number_of_containers() + sections[3].get_number_of_containers()
        back_section_container_count = sections[4].get_number_of_containers() + sections[5].get_number_of_containers()

        # Get the amount of operations needed to unload the section with the most containers
        max_section_container_count = max(front_section_container_count, middle_section_container_count, back_section_container_count)
        return int(max_section_container_count)

    def get_time_to_load_ship(self, operations):
        time = int(operations) * 4 / 60 / 24
        time = round(time, 2)
        return "It takes:  " + str(time) + " days to load the ship"

    def get_time_to_unload_ship(self, operations):
        time = int(operations) * 4 / 60 / 24
        time = round(time, 2)
        return "It takes:  " + str(time) + " days to unload the ship"
        
    # ----------------- CALCULATIONS ----------------- #

    def calculate_total_weight(self):
        total_weight = 0
        for section in self.get_sections():
            total_weight += section.get_section_weight()
        return total_weight

    
    def calculate_starboard_weight(self):
        starboard_weight = 0
        for section in self.get_sections():
            if section.get_section_id() % 2 == 0:
                starboard_weight += section.get_section_weight()
        return starboard_weight

    def calculate_port_weight(self):
        port_weight = 0
        for section in self.get_sections():
            if section.get_section_id() % 2 == 1:
                port_weight += section.get_section_weight()
        return port_weight
    
    def calculate_front_weight(self):
        front_weight = 0
        for section in self.get_sections():
            if section.get_section_id() < 2:
                front_weight += section.get_section_weight()
        return front_weight

    def calculate_middle_weight(self):
        middle_weight = 0
        for section in self.get_sections():
            if section.get_section_id() > 1 and section.get_section_id() < 4:
                middle_weight += section.get_section_weight()
        return middle_weight
    
    def calculate_back_weight(self):
        back_weight = 0
        for section in self.get_sections():
            if section.get_section_id() > 3:
                back_weight += section.get_section_weight()
        return back_weight

    
    # ----------------- BALANCE CHECKS ----------------- #

    # Ship is balanced if The weight on starboard does not exceed the weight on port side by more that x%, e.g. x = 5
    def is_ship_balanced_portside_and_starboard(self, x):
        starboard_weight = self.calculate_starboard_weight()
        port_weight = self.calculate_port_weight()
        if starboard_weight > port_weight:
            if (starboard_weight - port_weight) / starboard_weight * 100 > x:
                return False
        else:
            if (port_weight - starboard_weight) / port_weight * 100 > x:
                return False
        return True

    # Ship is balanced if the weight of each section does not exceed the weight of the middle section by more than y%, e.g. y = 5
    def is_ship_balanced_section(self, y):
        front_weight = self.calculate_front_weight()
        middle_weight = self.calculate_middle_weight()
        back_weight = self.calculate_back_weight()

        # Calculate the percentage difference between the weights of each section
        front_middle_diff = abs((middle_weight - front_weight) / middle_weight) * 100
        middle_back_diff = abs((middle_weight - back_weight) / middle_weight) * 100
        front_back_diff = abs((front_weight - back_weight) / front_weight) * 100

        # Check if any section exceeds the weight difference limit
        if front_middle_diff > y or middle_back_diff > y or front_back_diff > y:
            return False
        return True

    def are_containers_placed_in_descending_order(self):
        if self.get_weight_per_height_level() == sorted(self.get_weight_per_height_level(), reverse=True):
            return True

    def is_ship_balanced(self, x, y):
        if self.is_ship_balanced_portside_and_starboard(x) == True and self.is_ship_balanced_section(y) == True and self.are_containers_placed_in_descending_order() == True:
            return True
        return False
    
    def is_ship_full(self):
        for section in self.get_sections():
            if section.is_section_full() == False:
                return False
        return True

   # ----------------- LOADING FUNCTIONALITES ----------------- #
    
    def add_container(self, container):
        if len(self.available_sections) == 0:                   # if there is no available section
            raise Exception("No available sections to add container with ID: " + container.get_code() + " ship is full")
        else:
            lightest_section = self.get_lightest_section()      # get the lightest section
            #print("Adding container: " + container.get_code(), "total weight: " + str(container.get_total_weight()), "to section " + str(lightest_section.get_section_id()))
            if lightest_section.is_section_full() == True:
                self.available_sections.remove(lightest_section)
                self.full_sections.append(lightest_section)
                print("Section " + str(lightest_section.get_section_id()) + " is full, moving to full sections. Could not add container with ID: " + container.get_code())
                self.add_container(container)                   # Try to add container again to the lightest section (which is now full)
            else:
                lightest_section.add_container_to_section(container)

    def load_ship(self, container_set):
        print("Loading ship....")
        for container in container_set.containers:
            try:
                self.add_container(container)
            except Exception as e:
                pass
        print("Ship loaded successfully!")
        print("Ship is full: " + str(self.is_ship_full()))

    
    # ----------------- UNLOADING FUNCTIONALITES ----------------- #

    # Remove specific container from ship
    def remove_container(self, container_code):
        container, section, stack,  = self.find_container(container_code)
        stack.remove_container_from_stack(container)
        if stack.container_stack_is_empty() == True:
            section.remove_container_stack(stack)
        if section.is_section_empty() == True:
            self.full_sections.remove(section)
            self.available_sections.append(section)
            print("Section " + str(section.get_section_id()) + " is empty, moving to available sections.")
        return container
    
    # Remove the a container from the heaviest section
    def remove_container_from_heaviest_section(self):
        heaviest_section = self.get_heaviest_section()
        popped_container = heaviest_section.pop_container_from_heaviest_stack()
        if heaviest_section.is_section_empty() == True:
            self.full_sections.remove(heaviest_section)
            self.available_sections.append(heaviest_section)
            print("Section " + str(heaviest_section.get_section_id()) + " is empty, moving to available sections.")
        return popped_container


    #Unload all containers, and creates the corresponding list. Always unload from the heaviest section
    def unload_all_containers(self):
        print("#### UNLOADING CONTAINERS ####")
        i = self.get_number_of_containers_on_ship()
        while i > 0:
            container = self.remove_container_from_heaviest_section()
            self.list_of_unloaded_containers.append(container)
            for c in container:
                i -= 1
        print("#### UNLOADING CONTAINERS FINISHED ####")
        return self.list_of_unloaded_containers

    # ----------------- FINDING FUNCTIONALITES ----------------- #

    def find_container(self, container_code):
        for section in self.get_sections():
                for stack in section.get_container_stacks():
                    for containers in stack.get_containers():
                        for container in containers:
                            if container.get_code() == container_code:
                                return container, section, stack
                            
        return "Container with id {} not found in the ship.".format(container_code)



    
    def __str__(self):
        ship_string = ""
        sections_sorted = sorted(self.get_sections(), key=lambda section: section.get_section_id())
        for section in sections_sorted:
            ship_string += str(section) + "\t"  
        return ship_string




def main():
    start_time = time.time()

    ship_dimensions = [24, 22, 18]
    ship = ContainerShip(
        ship_dimensions[0], ship_dimensions[1], ship_dimensions[2])
    #loaded_container_set = load_set_of_containers("./solution/set_of_containers/set_of_6k_containers.tsv")
    container_set = ContainerSet()
    set_size = 6500
    # random.seed(10)
    container_set.generate_random_containers(set_size)
    save_set_of_containers(container_set, "./solution/set_of_containers/set_of_6500_containers.tsv")
    print("Number of containers to load: " + str(len(container_set.containers)))

    #START TIME
    # Load up sections
    ship.load_ship(container_set)


    print("Number of operations after loading and then unloading: ",ship.get_number_of_operations())
    print(ship.find_container("6288"))
    ship.remove_container("6288")
    print(ship.find_container("6288"))
    # print(ship)

    #END TIME
    save_ship_with_containers_to_file(ship, "./solution/saved_ships/ship_of_{set_size}_containers.tsv".format(set_size=set_size))
    
    # print("Number of operations in the ship is: ",ship.get_number_of_operations())
    # Unload ship
    ship.unload_all_containers()
    print("Containers that was loaded off the ship: ", ship.get_amount_of_unloaded_containers())
    
    

    

    time2 = time.time()
    print("Number of operations after loading and then unloading: ",ship.get_number_of_operations())
        
    print("Compile time " + str(time2 - start_time))
    
    #save_ship_with_containers_to_file(ship, "./solution/saved_ships/set_of_{set_size}_containers.tsv".format(set_size=set_size))

    #ship2 = load_ship_with_containers_from_file("./solution/saved_ships/set_of_2900_containers.tsv")


def main2():
    start_time = time.time()
    # ship2 = load_ship_with_containers_from_file(6500)

    ship = ContainerShip(24, 22, 18)
    container_set = ContainerSet()
    # random.seed(10)
    set_size = 6330
    container_set.generate_random_containers(set_size)

    ship.load_ship(container_set)
    
    print(ship)
    
    print(ship.is_ship_balanced_portside_and_starboard(5))
    print(ship.is_ship_balanced_section(10))
    print(ship.get_weight_per_height_level())
    print(ship.are_containers_placed_in_descending_order())

    print(ship.is_ship_balanced(5, 10), "ship is balanced")

    end_time = time.time()
    print("Time: " + str(end_time - start_time))



if __name__ == "__main__":
    main()
