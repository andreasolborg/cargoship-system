import time
from Container import *
from ContainerSet import *
from ContainerSetManager import *
from ContainerShipManager import *
from ContainerStack import *
from ContainerSection import *

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

        self.list_of_containers = []  # List of containers that are not in the ship

    def get_ship_length(self):
        return self.length

    def get_ship_width(self):
        return self.width

    def get_ship_height(self):
        return self.height

    def get_sections(self):
        return self.available_sections + self.full_sections

    def get_section(self, sectionID):
        return self.get_sections()[sectionID]
    
    def get_number_of_operations(self):
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



    # ----------------- UNTESTED METHODS ----------------- #

    def calculate_total_weight(self):
        total_weight = 0
        for section in self.get_sections():
            total_weight += section.get_section_weight()
        return total_weight
    
    def calculate_starboard_weight(self):
        starboard_weight = 0
        for section in self.get_sections():
            if section.get_sectionID() % 2 == 0:
                starboard_weight += section.get_section_weight()
        return starboard_weight

    def calculate_port_weight(self):
        port_weight = 0
        for section in self.get_sections():
            if section.get_sectionID() % 2 == 1:
                port_weight += section.get_section_weight()
        return port_weight
    
    def calculate_front_weight(self):
        front_weight = 0
        for section in self.get_sections():
            if section.get_sectionID() < 2:
                front_weight += section.get_section_weight()
        return front_weight

    def calculate_middle_weight(self):
        middle_weight = 0
        for section in self.get_sections():
            if section.get_sectionID() > 2 and section.get_sectionID() < 5:
                middle_weight += section.get_section_weight()
        return middle_weight
    
    def calculate_back_weight(self):
        back_weight = 0
        for section in self.get_sections():
            if section.get_sectionID() > 4:
                back_weight += section.get_section_weight()
        return back_weight

    # Ship is balanced if The weight on starboard does not exceed the weight on port side by more that x%, e.g. x = 5
    def is_ship_balanced_portside_and_starboard(self, x, y):
        starboard_weight = self.calculate_starboard_weight()
        port_weight = self.calculate_port_weight()
        if starboard_weight > port_weight:
            if (starboard_weight - port_weight) / starboard_weight * 100 > x:
                return False
        else:
            if (port_weight - starboard_weight) / port_weight * 100 > x:
                return False
        return True
    
    # Ship is balanced if The weight of a section does not exceed the weight of another section by more that x%, e.g. x = 10
    def is_ship_balanced_section(self, x, y):
        for section in self.get_sections():
            for section2 in self.get_sections():
                if section.get_section_weight() > section2.get_section_weight():
                    if (section.get_section_weight() - section2.get_section_weight()) / section.get_section_weight() * 100 > x:
                        return False
                else:
                    if (section2.get_section_weight() - section.get_section_weight()) / section2.get_section_weight() * 100 > x:
                        return False
        return True

    def is_ship_balanced(self, x, y):
        if self.is_ship_balanced_portside_and_starboard(x, y) == True and self.is_ship_balanced_section(x, y) == True:
            return True
        return False

    
    # -------------------- END OF UNTESTED METHODS --------------------


    
    def get_number_of_containers_on_ship(self):
        containers_on_ship = 0
        for section in self.get_sections():
            for stack in section.get_container_stacks():
                containers_on_ship += stack.get_number_of_containers()
        return containers_on_ship

    def get_stacks_that_are_not_full(self):
        stacks_that_are_not_full = []
        for section in self.get_sections():
            for stack in section.get_container_stacks():
                if stack.container_stack_is_full() == False:
                    stacks_that_are_not_full.append(stack)
        return stacks_that_are_not_full
        

    def add_container(self, container):
        if len(self.available_sections) == 0:                   # if there is no available section
            raise Exception("Ship is full, no available section(s). Could not add container with ID: " + container.get_code(), "Stop adding containers.")                            
        else:
            lightest_section = self.get_lightest_section()      # get the lightest section
            #print("Adding container: " + container.get_code(), "total weight: " + str(container.get_total_weight()), "to section " + str(lightest_section.get_sectionID()))
            if lightest_section.is_section_full() == True:
                self.available_sections.remove(lightest_section)
                self.full_sections.append(lightest_section)
                print("Section " + str(lightest_section.get_sectionID()) + " is full, moving to full sections. Could not add container with ID: " + container.get_code())
                self.add_container(container)                   # Try to add container again to the lightest section (which is now full)
            else:
                lightest_section.add_container_to_section(container)


#### UNLOADING CONTAINERS ####

    def remove_container(self, container_code):
        container, section, stack,  = self.find_container(container_code)
        stack.remove_container_from_stack(container)
        if stack.container_stack_is_empty() == True:
            section.remove_container_stack(stack)
        if section.is_section_empty() == True:
            self.full_sections.remove(section)
            self.available_sections.append(section)
            print("Section " + str(section.get_sectionID()) + " is empty, moving to available sections.")
        return container
    
    def remove_container_from_heaviest_section(self):
        heaviest_section = self.get_heaviest_section()
        popped_container = heaviest_section.pop_container_from_heaviest_stack()
        if heaviest_section.is_section_empty() == True:
            self.full_sections.remove(heaviest_section)
            self.available_sections.append(heaviest_section)
            print("Section " + str(heaviest_section.get_sectionID()) + " is empty, moving to available sections.")
        return popped_container


    #Unload all containers. Always unload from the heaviest section
    def unload_all_containers(self):
        print("#### UNLOADING CONTAINERS ####")
        i = self.get_number_of_containers_on_ship()
        while i > 0:
            container = self.remove_container_from_heaviest_section()
            self.list_of_containers.append(container)
            for c in container:
                i -= 1
        print("#### UNLOADING CONTAINERS FINISHED ####")
        return self.list_of_containers

            
#### UNLOADING CONTAINERS FINISHED #### 

    def find_container(self, container_code):
        holding_container = []
        for section in self.get_sections():
                for stack in section.get_container_stacks():
                    for containers in stack.get_containers():
                        for container in containers:
                            if container.get_code() == container_code:
                                # z_level = str(stack.get_index_of_container(container))
                                # Keep this print statement for debugging
                                # print("Container "+ container.get_code() + " found in section " + str(section.get_sectionID()) + " stack " + str(stack.get_location_in_section()) +" at height: " + z_level + ". The container " + str(containers.index(container)+1), "(means the container is the " + str(containers.index(container)+1) + "th container in the stack)")
                                return container, section, stack
                            
        return "Container with id {} not found in the ship.".format(container_code)

    
    def __str__(self):
        ship_string = ""
        sections_sorted = sorted(self.get_sections(), key=lambda section: section.get_sectionID())
        for section in sections_sorted:
            ship_string += str(section) + "\t"  
        return ship_string




def main():
    
    ship_dimensions = [24, 22, 18]
    ship = ContainerShip(
        ship_dimensions[0], ship_dimensions[1], ship_dimensions[2])
    #loaded_container_set = load_set_of_containers("./solution/set_of_containers/set_of_6k_containers.tsv")
    container_set = ContainerSet()
    set_size = 6500
    random.seed(10)
    # container_set.generate_random_containers(set_size)
    container_set.generate_random_containers(set_size)
    print("Number of containers to load: " + str(len(container_set.containers)))

    
    #START TIME
    start_time = time.time()
    # Load up sections
    for container in container_set.containers:
        # print("Adding container: " + container.get_code(), "total weight: " + str(container.get_total_weight()))
        try:
            ship.add_container(container)
        except Exception as e:
                print(e)


    end_time = time.time()

    print("time to load: " + str(end_time - start_time))
    print("Number of operations after loading and then unloading: ",ship.get_number_of_operations())
    print(ship.find_container("6288"))
    ship.remove_container("6288")
    print(ship.find_container("6288"))
    # print(ship)

    #END TIME
    save_ship_with_containers_to_file(ship, "./solution/saved_ships/set_of_{set_size}_containers.tsv".format(set_size=set_size))
    
    # print("Number of operations in the ship is: ",ship.get_number_of_operations())
    # Unload ship
    try:
        ship.unload_all_containers()
    except Exception as e:
        print(e)
    
    increment = 0
    for container in ship.list_of_containers:
        for c in container:
            increment += 1
    print(increment)
    
    
    print(len(ship.list_of_containers))

    

    time2 = time.time()
    print("time to load and unload: " + str(time2 - start_time))
    print("Number of operations after loading and then unloading: ",ship.get_number_of_operations())
        
    
    #save_ship_with_containers_to_file(ship, "./solution/saved_ships/set_of_{set_size}_containers.tsv".format(set_size=set_size))

    #ship2 = load_ship_with_containers_from_file("./solution/saved_ships/set_of_2900_containers.tsv")

    
    

def main2():
    start_time = time.time()
    ship2 = load_ship_with_containers_from_file("./solution/saved_ships/set_of_6500_containers.tsv")
    end_time = time.time()
    print("Time: " + str(end_time - start_time))

if __name__ == "__main__":
    main()
