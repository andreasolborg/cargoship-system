from container import Container
from container_set import ContainerSet
from container_set_manager import save_set_of_containers, load_set_of_containers


def main():
    # Generate a set of 10 random containers
    container_set = ContainerSet()
    container_set.generate_random_containers(10000)
    
    # Save the containers to a file
    save_set_of_containers(container_set, "./solution/set_of_10k_containers.tsv")
    # Load the containers from the file
    #container_set = load_set_of_containers("./solution/set_of_25k_containers.tsv")
    #save_set_of_containers(container_set, "./solution/containers.tsv")





    
if __name__ == "__main__":
    main()
