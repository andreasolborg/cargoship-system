from random import randint
from container import generate_random_container

class ContainerSet:
    def __init__(self):
        self.containers = []
        

    def add_container(self, container):
        if self.find_container(container.code) == None: # We need this, because two objects with the same code will be considered equal
            self.containers.append(container)

    def remove_container(self, container):
        self.containers.remove(container)

    def find_container(self, code):
        for container in self.containers:
            if container.code == code:
                return container
        return None
    
    # Generate a list of random containers using add_container and remove_container functions
    # Task 2.1.3
    def generate_random_containers(self, set_size):
        for i in range(set_size):
            container = generate_random_container()
            self.add_container(container)
        


