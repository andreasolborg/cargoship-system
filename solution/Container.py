## Ikke ha mange kommentarer. Koden skal være lesbar uten kommentarer
import random
import time

class Container:
    # The constructor of the class Container   
    def __init__(self, code, length, weight, cargo, weight_capacity):
        self.code = code
        self.length = length
        self.weight = weight
        self.cargo = cargo
        self.weight_capacity = weight_capacity

    # Get functions
    def get_code(self):
        return self.code

    def get_length(self):
        return self.length

    def get_cargo(self):
        return self.cargo

    def get_weight(self):
        return self.weight

    def get_weight_capacity(self):
        return self.weight_capacity

    def get_total_weight(self):
        return self.weight + self.cargo
      
    # Set functions
    def set_code(self, code):
        self.code = code

    def set_length(self, length):
        self.length = length

    def set_cargo(self, cargo):
        self.cargo = cargo

    def set_weight(self, weight):
        self.weight = weight

    def set_weight_capacity(self, weight_capacity):
        self.weight_capacity = weight_capacity

    # tostring
    def __str__(self) -> str:
        return f"Container: {self.code}, length: {self.length}, total container weight {self.weight + self.cargo}, {self.weight_capacity} tons capacity"

    # tostring for list of containers
    def __repr__(self) -> str:
        return f"C: {self.code} W: {self.weight + self.cargo}, L: {self.length}"


def createContainerCode():
    if not hasattr(createContainerCode, "counter"):
        createContainerCode.counter = 1
    id = str(createContainerCode.counter).zfill(2)
    createContainerCode.counter += 1
    return id


# Task 2.1.2
# Generate a random container with a random code, length, width, height and weight
# The loaded weight should be 0. The weight should be 2 tons for a 20 foot container and 4 tons for a 40 foot container.

def generate_random_container():
    possible_containers = [[20, 2, 20], [40, 4, 22]]
    random_container_ = random.choice(possible_containers)

    random_code = createContainerCode()
    length = random_container_[0]
    weight = random_container_[1]
    weight_capacity = random_container_[2]

    # The loaded weight should be 0
    random_container = Container(random_code, length, weight, random.randint(0, weight_capacity), weight_capacity) ## random.randint(0, weight_capacity) is the cargo weight (loaded weight) make it a function
    return random_container

def generate_list_of_random_containers(n):
    list_of_containers = []
    for _ in range(n):
        list_of_containers.append(generate_random_container())
    return list_of_containers

def main():
    # Task 2.1.1
    # Create a container with the code "ABO1234567", length 20, width 2, height 2 and weight 2
    # The loaded weight should be 0. The weight should be 2 tons for a 20 foot container and 4 tons for a 40 foot container.
    container1 = Container("ABO1234567", 20, 2, 0, 20)
    print(container1)

    start = time.time()
    
    # Task 2.1.2
    # Generate a random container with a random code, length, width, height and weight
    # The loaded weight should be a random number between 0 and capacity. The weight should be 2 tons for a 20 foot container and 4 tons for a 40 foot container.
    container2 = generate_random_container()
    # print(container2)

    # Task 2.1.3
    # Create a list of 10 random containers
    # Print the list
    list_of_containers = []
    for _ in range(20000):
        list_of_containers.append(generate_random_container())
    # print(list_of_containers)


    print(time.time() - start)

if __name__ == "__main__":
    main()