# Author: Andreas Olborg - Group 47
from Container import Container
from ContainerShip import ContainerShip
from ContainerSetManager import *
from ContainerSet import ContainerSet

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
                    file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(section.get_section_id(), container.get_code(), container.get_length(), container.get_weight(), container.get_cargo(), container.get_total_weight(), container.get_weight_capacity()))
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
                                file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(section.get_section_id(),x, y, z, c.get_code(), c.get_length(), c.get_weight(), c.get_cargo(), c.get_total_weight(), c.get_weight_capacity()))
                        except IndexError:
                            pass
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
    except FileNotFoundError as e:
        print("The file {} does not exist. Creating a set with given size, and making a new ship".format(ship_file_path))
        container_set = ContainerSet()
        container_set.generate_random_containers(set_size)
        save_set_of_containers(container_set, container_file_path)
        ship = ContainerShip(24, 22, 18)
        ship.load_ship(container_set)
        save_ship_with_containers_to_file(ship, ship_file_path)
        print("Ship saved to file: {}".format(ship_file_path))
        return ship



