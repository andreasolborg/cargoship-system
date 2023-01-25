from container import Container
from container_set import ContainerSet, generate_random_containers
from container_manager import save_set_of_containers, load_set_of_containers


def main():
    container_set = generate_random_containers(10) # Generate a set of 10 random containers
    save_set_of_containers(container_set, "containers.tsv") # Save the containers to a file
    
    container_set = load_set_of_containers("containers.tsv", ContainerSet(), Container) # Load the containers from the file
    for container in container_set.containers:
        print(container)
    print(len(container_set.containers))
    
    
    
    
if __name__ == "__main__":
    main()
