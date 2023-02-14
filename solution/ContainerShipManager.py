from Container import Container
from ContainerStack import ContainerStack
from ContainerSection import ShipSection
from ContainerShipRevised import ContainerShip

# TASK 6
# Save the ship to a file with the containers on it as well as the ship dimensions and the container information (code, length, weight, cargo, cargo capacity)
def save_ship_with_containers_to_file(ship, file_path):
    with open(file_path, "w") as file:
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

