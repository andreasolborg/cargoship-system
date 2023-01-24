from ContainerSet import ContainerSet
from Container import Container

class ContainerShip:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.container_set = ContainerSet()

    def add_container(self, container):
        if self.container_set.find_container(container.code) is None:
            self.container_set.add_container(container)
        else:
            print("Container already exists")

    def remove_container(self, container):
        self.container_set.remove_container(container)

    def find_container(self, code):
        return self.container_set.find_container(code)

    def __str__(self):
        return f"Name: {self.name}, Capacity: {self.capacity}, Containers: {self.container_set.containers}"

def main():
    ship = ContainerShip("Titanic", 1000)
    c1 = Container("C1", 20, 2, 20)
    ship.add_container(c1)
    c2 = Container("C2", 40, 4, 22)
    ship.add_container(c2)
    print(ship.find_container("C1").__str__())  # prints Container: C1, length: 20, empty weight: 2, max load: 20, current load: 0
    ship.remove_container(c1)
    print(ship.find_container("C1"))  # prints None
    print(ship.__str__())  # prints Name: Titanic, Capacity: 1000, Containers: [<Container.Container object at 0x...>, <Container.Container object at 0x...>]

main()