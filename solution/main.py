from container import Container
from container_set import ContainerSet, generate_random_containers
from container_manager import save_set_of_containers, load_set_of_containers


def main():
    container_set = load_set_of_containers("containers.tsv", ContainerSet(), Container)
    for container in container_set.containers:
        print(container)
    print(len(container_set.containers))
    
    
    
    
if __name__ == "__main__":
    main()
