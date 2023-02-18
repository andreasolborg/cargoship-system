# Author: Andreas Olborg - Group 47

from Container import *

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
            
    # Generate a list of random containers (size and cargo are optional)
    def generate_random_containers(self, set_size, size=None, cargo=None):
        for i in range(set_size):
            container = generate_random_container(size)
            cargo = random.randint(0, container.weight_capacity)
            container.set_cargo(cargo)
            self.add_container_to_set(container)
        
    # Generate empty containers for later use
    def generate_n_empty_containers(self, set_size, size=None):
        for i in range(set_size):
            container = generate_random_container(size)
            container.set_cargo(0)
            self.add_container_to_set(container)
            
    
# Look for a container that is in the list, and remove it, then look for a container that is not in the list
def standard_demo():
    container_set = ContainerSet()
    container_set.generate_random_containers(100)
    print(container_set.containers)
    container_to_remove = container_set.get_nth_container(0)
    print("We are removing container with code: ", container_to_remove.get_code())
    container_set.remove_container_from_set(container_to_remove)
    container_to_look_for = "0000"
    print("We are looking for container with code: ", container_to_look_for, container_set.find_container(container_to_look_for))
    container_to_look_for = "0002"
    print("We are looking for container with code: ", container_to_look_for, " and we found a contaier with following ID: ", container_set.find_container(container_to_look_for).get_code())
            
# Look for a container that is not in the list
def advanced_demo():
    container_set = ContainerSet()
    container_set.generate_n_empty_containers(10)
    print(container_set.containers)
    container_to_remove = container_set.get_nth_container(1)
    print("We are removing container with code: ", container_to_remove.code)
    container_set.remove_container_from_set(container_to_remove)
    container_to_look_for = "01"
    print("Looking for container with code: ", container_to_look_for, " -> ", container_set.find_container(container_to_look_for))
    container_to_look_for = "02"
    print("Looking for container with code: ", container_to_look_for, " -> ", container_set.find_container(container_to_look_for))
    
    container_set.flush()
    print(container_set.containers)

def main():
    print("----- Standard demo -----\n")

    standard_demo()

    print("\n\n----- Advanced demo -----\n")

    advanced_demo()

if __name__ == "__main__":
    main()
        


