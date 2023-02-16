from Container import Container
from ContainerStack import ContainerStack
from ContainerSection import ShipSection
from ContainerShipRevised import ContainerShip
from ContainerSetManager import load_set_of_containers

# TASK 6
# Save the ship to a file with the containers on it as well as the ship dimensions and the container information (code, length, weight, cargo, cargo capacity)
def save_ship_with_containers_to_file(ship, file_path):
    with open(file_path, "w") as file:
        file.write("{}\t{}\t{}\n".format(ship.get_ship_length(), ship.get_ship_width(), ship.get_ship_height()))
        # Iterate through the holding containers 
        file.write("HOLDING CONTAINERS\n")
        file.write("SectionID\tcode\tlength\tweight\tcargo\tTW\tcargo capacity\n")
        for section in ship.get_sections():
            holding_container = section.get_holding_containers()
            if len(holding_container) > 0:
                for container in holding_container:
                    file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(section.get_sectionID(), container.get_code(), container.get_length(), container.get_weight(), container.get_cargo(), container.get_total_weight(), container.get_weight_capacity()))
        # Iterate through the containers on the ship
        file.write("SectionID\tx\ty\tz\tcode\tlength\tweight\tcargo\tTW\tcargo capacity\n")
        file.write("--------------------\n")
        for section in ship.get_sections():
            x_max = section.get_section_length()
            y_max = section.get_section_width()
            z_max = section.get_max_stack_height()
            # file.write("--------------------\n")
            for x in range(x_max):
                for y in range(y_max):
                    stack = section.get_stack((x,y))
                    for z in range(z_max):
                        try:
                            container = stack.get_container(z)
                            for c in container:
                                file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(section.get_sectionID(),x, y, z, c.get_code(), c.get_length(), c.get_weight(), c.get_cargo(), c.get_total_weight(), c.get_weight_capacity()))
                        except IndexError:
                            pass
    file.close()

def save_ship_with_containers_to_file_basic(ship, file_path):
    with open(file_path, "w") as file:
        popped_containers = ship.unload_all_containers() # Get all the containers on the ship, unloading them by weight
        popped_containers.reverse() # Reverse the list so that the containers are in the same order as they were loaded
        file.write("{}\t{}\t{}\n".format(ship.get_ship_length(), ship.get_ship_width(), ship.get_ship_height()))
        # Iterate through the holding containers
        file.write("HOLDING CONTAINERS\n")
        file.write("Section\tcode\tlength\tweight\tcargo\tTW\tcargo capacity\n")
        for section in ship.get_sections():
            holding_container = section.get_holding_containers()
            if len(holding_container) > 0:
                for container in holding_container:
                    file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(section.get_sectionID(), container.get_code(), container.get_length(), container.get_weight(), container.get_cargo(), container.get_total_weight(), container.get_weight_capacity()))
        file.write("--------------------\n")
        # Iterate through the containers on the ship
        for container in popped_containers:
            for c in container:
                file.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(c.get_code(), c.get_length(), c.get_weight(), c.get_cargo(), c.get_total_weight(), c.get_weight_capacity()))
    file.close()


def load_ship_with_containers_from_file(set_size):
    ship_file_path = "./solution/saved_ships/ship_of_{}_containers.tsv".format(set_size)
    container_file_path = "./solution/set_of_containers/set_of_{}_containers.tsv".format(set_size)
    try:
        with open(ship_file_path, "r") as file:
            line = file.readline()
            line = line.strip().split("\t")
            ship_length = int(line[0])
            ship_width = int(line[1])
            ship_height = int(line[2])
            ship = ContainerShip(ship_length, ship_width, ship_height)
            # Iterate through the containers in the set of containers file
            set_of_containers = load_set_of_containers(container_file_path)
            ship.load_ship(set_of_containers)

        return ship
    except FileNotFoundError:
        print("The file {} does not exist.".format(ship_file_path))

        


def save_ship_with_containers_to_file_pretty(ship, file_path):
    with open(file_path, "w") as file:
        # Write the header to the file
        file.write("This file contains information about the containers on an already loaded ship.\nThe sorting is already done when loading the containers.\n")
        file.write("Ship dimensions (length, width, height): \n")
        file.write("{}\t{}\t{}\n".format(ship.get_ship_length(), ship.get_ship_width(), ship.get_ship_height()))
        # Write the ship dimensions to the file
        file.write("Dimensions for each section (length, width, max_height): \n")
        file.write("{}\t{}\t{}\n".format(ship.get_section(0).get_section_length(), ship.get_section(0).get_section_width(), ship.get_section(0).get_max_stack_height()))
        file.write("--------------------\n")
        # Write the container information to the file
        # Iterate through the containers on the ship
        for section in ship.get_sections():
            file.write("{}\n".format(section.get_sectionID()))

            holding_container = section.get_holding_containers()
            if len(holding_container) > 0:
                file.write("This section has a holding container with the following information:\n")
                file.write("code\tlength\tweight\tcargo\tTW\tcargo capacity\n")
                for container in holding_container:
                    file.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(container.get_code(), container.get_length(), container.get_weight(), container.get_cargo(), container.get_total_weight(), container.get_weight_capacity()))
            else:
                file.write("This section has no holding container\n")
                
            x_max = section.get_section_length()
            y_max = section.get_section_width()
            z_max = section.get_max_stack_height()
            file.write("--------------------\n")
            for x in range(x_max):
                for y in range(y_max):
                    stack = section.get_stack((x,y))
                    file.write("Stack at ({}, {}), in section: {}\n".format(x, y, section.get_sectionID()))
                    file.write("(x,\t y,\t z)\tcode\tlength\tweight\tcargo\tTW\tcargo capacity\n")
                    for z in range(z_max):
                        try:
                            container = stack.get_container(z)
                            for c in container:
                                file.write("({},\t {},\t {})\t{}\t{}\t{}\t{}\t{}\t{}\n".format(x, y, z, c.get_code(), c.get_length(), c.get_weight(), c.get_cargo(), c.get_total_weight(), c.get_weight_capacity()))
                        except IndexError:
                            file.write("({},\t {},\t {})\t{}\t{}\t{}\t{}\t{}\t{}\n".format(x, y, z, "None", "None", "None", "None", "None", "None"))

            file.write("--------------------\n")
        file.close()
                       
    file.close()




def load_ship_with_containers_from_file1(file_path):
    with open(file_path, "r") as file:
        # Read the first line of the file to get the ship dimensions
        line = file.readline()
        print(line)
        line = line.strip().split("\t")
        ship_length = int(line[0])
        ship_width = int(line[1])
        ship_height = int(line[2])
        # Create a new ship with the dimensions from the file
        ship = ContainerShip(ship_length, ship_width, ship_height)
        # Read the next line to get the holding containers
        line = file.readline()
        print(line)
        line = file.readline()
        print(line)
        while line != "--------------------\n" and line != "":
            line = file.readline()
            if line.startswith("HOLDING CONTAINERS"):
                line = file.readline()
                line = file.readline()
                while line != "--------------------\n":
                    print(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                    line = line.strip().split("\t")
                    sectionID = int(line[0])
                    code = line[1]
                    length = int(line[2])
                    weight = int(line[3])
                    cargo = line[4]
                    cargo_capacity = int(line[6])
                    container = Container(code, length, weight, cargo, TW, cargo_capacity)
                    ship.get_section(sectionID).add_holding_container(container)
                    print(container)
                    line = file.readline()
            # Read the next line to get the containers on the ship
            if line == "--------------------\n":
                line = file.readline()
                line = file.readline()
                while line != "": 
                    line = line.split("\t")
                    code = line[4]
                    length = int(line[5])
                    weight = int(line[6])
                    cargo = int(line[7])
                    cargo_capacity = int(line[9])
                    container = Container(code, length, weight, cargo, cargo_capacity)
                    ship.add_container(container)
                    line = file.readline()
        file.close()
    return ship

                
def main():

    return 


if "__name__" == "__main__":
    main()