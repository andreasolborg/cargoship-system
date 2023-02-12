# Task 4
# Class for saving and loading the container data from a file
# We are using TSV Values (Tab Separated Values) for this
from container import Container
from container_set import ContainerSet

def save_set_of_containers(container_set, filename):
    with open(filename, "a") as file:
        for container in container_set.containers:
            file.write(container.get_code() + "\t")
            file.write(str(container.get_length()) + "\t")
            file.write(str(container.get_weight()) + "\t")
            file.write(str(container.get_cargo()) + "\t")
            file.write(str(container.get_weight_capacity()))
            file.write("\n")
        file.close()

def load_set_of_containers(file_name):
    container_set = ContainerSet()
    with open(file_name, 'r') as file:
        for line in file:
            values = line.split("\t")
            container = Container(values[0], int(values[1]), int(values[2]), int(values[3]), int(values[4]))
            container_set.add_container(container)
    return container_set
