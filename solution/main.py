from container import Container
from container_set import ContainerSet
from container_set_manager import save_set_of_containers, load_set_of_containers


def main():
    # Generate a set of 10 random containers
    container_set = ContainerSet()
    container_set.generate_random_containers(6000)
    
    # Save the containers to a file
    
    # Load the containers from the file
    #container_set = load_set_of_containers("./solution/containers.tsv")
    save_set_of_containers(container_set, "./solution/set_of_6k_containers.tsv")
    print(len(container_set.containers))





    
if __name__ == "__main__":
    main()
