#Import container
from Container import Container, generate_container
import random

class ContainerSet:
    def __init__(self):
        self.containers = []
    
    def add_container(self, container):
        self.containers.append(container)

    def remove_container(self, container):
        self.containers.remove(container)

    def find_container(self, code):
        for container in self.containers:
            if container.code == code:
                return container
        return None

def generate_container_set(num_containers, code_length, load_range, length_range):
    container_set = ContainerSet()
    for i in range(num_containers):
        container = generate_container(code_length, load_range, length_range)
        container_set.add_container(container)
    return container_set


def main():
    container_set = ContainerSet()
    container_set = generate_container_set(10, 5, (0, 20), (20, 40))
    print(container_set.containers)  # prints [<__main__.Container object at 0x...>, <__main__.Container object at 0x...>, ...]
    for container in container_set.containers:
        print(container)


main()

