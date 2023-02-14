# Author: Andreas Olborg


# Import the classes from the other files

from Container import *
from ContainerSet import *
from ContainerSetManager import *
from ContainerShipManager import *
from ContainerStack import *
from ContainerSection import *

def main():
    # Generate a set of 10 random containers
    container_set = ContainerSet()
    container_set.generate_random_containers(6000) # Generate 6000 random containers and add them to the container set (list)
    
    # Save the containers to a file
    
    # Load the containers from the file
    #container_set = load_set_of_containers("./solution/set_of_containers/containers.tsv")
    save_set_of_containers(container_set, "./solution/set_of_containers/set_of_6k_containers.tsv")
    print(len(container_set.containers))





    
if __name__ == "__main__":
    main()
