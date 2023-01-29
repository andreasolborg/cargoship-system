from container import Container
from container_ship import ContainerShip

# TASK 6
# Save the ship to a file with the containers on it as well as the ship dimensions and the container information (code, length, weight, cargo, cargo capacity)
def save_ship_with_containers_to_file(ship, file_path):
    with open(file_path, "w") as file:
        # Write the ship dimensions to the file
        file.write("{}\t{}\t{}\n".format(ship.get_ship_length(), ship.get_ship_width(), ship.get_ship_height()))
        # Write the container information to the file
        file.write("y\tx\tz\tContainerCode\tContainer Length\tWeight\tCargo\tCargo Capacity\n")  
        # Iterate through the containers on the ship
        for h in range(ship.get_ship_height()):
            for w in range(ship.get_ship_width()):
                for l in range(ship.get_ship_length()):
                    container = ship.get_nth_container(h, w, l)
                    if container is not None:
                        # Write the container information to the file
                        file.write(f"{l}\t{w}\t{h}\t{container.get_code()}\t{container.get_length()}\t{container.get_weight()}\t{container.get_cargo()}\t{container.get_weight_capacity()}\n")
    

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
            

