from container import *

class ContainerSet:
    def __init__(self):
        self.containers = []
    
    def get_containers(self):
        return self.containers

    def get_nth_container(self, n):
        if n >= len(self.containers):
            return f"Container with index {n} not found"
        return self.containers[n]
        
    def add_container_to_set(self, container):
        self.containers.append(container)
        
    def remove_container_from_set(self, container):
        self.containers.remove(container)
    
    def find_container(self, code):
        for container in self.containers:
            if container.code == code:
                return container
        return f"Container with code {code} not found"

    def flush(self):
        self.containers = []
            

    # Generate a list of random containers using add_container and remove_container functions
    # Task 2.1.3
    def generate_random_containers(self, set_size):
        for i in range(set_size):
            container = generate_random_container()
            self.add_container_to_set(container)
        
    # Generate empty containers for later use
    def generate_n_empty_containers(self, set_size):
        for i in range(set_size):
            container = generate_random_container()
            container.set_cargo(0)
            self.add_container_to_set(container)
    
    # Generate list of 20 foot containers
    def generate_n_20_foot_containers(self, set_size, cargo):
        for i in range(set_size):
            container = Container(create_container_code(), 20, 2, 0, 20)
            container.set_cargo(cargo)
            self.add_container_to_set(container)
    
    # Generate list of 40 foot containers
    def generate_n_40_foot_containers(self, set_size, cargo):
        for i in range(set_size):
            container = Container(create_container_code(), 40, 4, 0, 22)
            container.set_cargo(cargo)
            self.add_container_to_set(container)
            
    

def standard_demo():
    container_set = ContainerSet()
    container_set.generate_random_containers(10)
    print(container_set.containers)
    container_to_remove = container_set.get_nth_container(0)
    print("We are removing container with code: ", container_to_remove.code)
    container_set.remove_container_from_set(container_to_remove)
    container_to_look_for = "01"
    print("We are looking for container with code: ", container_to_look_for, " and we found: ", container_set.find_container(container_to_look_for))
    container_to_look_for = "02"
    print("We are looking for container with code: ", container_to_look_for, " and we found a contaier with following information: ", container_set.find_container(container_to_look_for))
            
def advanced_demo():
    container_set = ContainerSet()
    container_set.generate_n_empty_containers(10)
    container_to_remove = container_set.get_nth_container(1)
    print("We are removing container with code: ", container_to_remove.code)
    container_set.remove_container_from_set(container_to_remove)
    container_to_look_for = "01"
    print("Looking for container with code: ", container_to_look_for, " -> ", container_set.find_container(container_to_look_for))
    container_to_look_for = "02"
    print("Looking for container with code: ", container_to_look_for, " -> ", container_set.find_container(container_to_look_for))
    
    container_set.flush()
    container_set.generate_n_20_foot_containers(10, 0)
    print(container_set.containers)
    container_set.generate_n_40_foot_containers(10, 0)
    print(container_set.containers)

def main():
    advanced_demo()

if __name__ == "__main__":
    main()
        


