from Container import Container
from ContainerShipRevised import ContainerShip

# TASK 6
# Save the ship to a file with the containers on it as well as the ship dimensions and the container information (code, length, weight, cargo, cargo capacity)
def save_ship_with_containers_to_file(ship, file_path):
    with open(file_path, "w") as file:
        file.write("10 This file contains information about the containers on an already loaded ship.\nThe sorting is already done when loading the containers.\n")
        file.write("Ship dimensions: {}x{}x{}\n".format(ship.get_ship_length(), ship.get_ship_width(), ship.get_ship_height()))
        # Write the ship dimensions to the file
        # file.write("{}\t{}\t{}\n".format(ship.get_ship_length(), ship.get_ship_width(), ship.get_ship_height()))
        file.write("Dimensions for each section: {}x{}\n".format(ship.get_sections()[0].get_section_width(), ship.get_sections()[0].get_section_length()))
        # Write the container information to the file
        # Iterate through the containers on the ship
        for section in ship.get_sections():
            file.write("Section {}\n".format(section.get_sectionID()))

            holding_container = section.get_holding_container()
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
                        container = stack.get_container(z)
                        for c in container:
                            file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(x, y, z, c.get_code(), c.get_length(), c.get_weight(), c.get_cargo(), c.get_total_weight(), c.get_weight_capacity()))
                            
    file.close()

# We dont need to check for the length of the container, because the ship_load.tsv file is already correct
def load_ship_with_containers_from_file(file_path):
    with open(file_path, "r") as file:
        # Skip the 2 first lines
        values = file.readline().split("\t")
        ship = ContainerShip(int(values[0]), int(values[1]), int(values[2]))
        file.readline()
        values = []
        # Iterate through the rest of the file
        for line in file:
            values = line.split("\t")
            container = Container(values[3], int(values[4]), int(values[5]), int(values[6]), int(values[7]))
            ship.insert_container(container, int(values[2]), int(values[1]), int(values[0]))
    return ship
            

