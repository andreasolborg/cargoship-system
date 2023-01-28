## Ikke ha mange kommentarer. Koden skal være lesbar uten kommentarer
import random


class Container:
    # The constructor of the class Container
    # Kan eventuelt gjøre om length, width og height til size?
    
    def __init__(self, code, length, width, height, weight, cargo, weight_capacity):
        self.code = code
        self.length = length
        self.width = width
        self.height = height
        self.cargo = cargo
        self.weight = weight
        self.weight_capacity = weight_capacity

    # Get functions
    def get_code(self):
        return self.code

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_cargo(self):
        return self.cargo

    def get_weight(self):
        return self.weight

    def get_weight_capacity(self):
        return self.weight_capacity

    # Set functions
    def set_code(self, code):
        self.code = code

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_cargo(self, cargo):
        self.cargo = cargo

    def set_weight(self, weight):
        self.weight = weight

    def set_weight_capacity(self, weight_capacity):
        self.weight_capacity = weight_capacity


    # tostring
    def __str__(self) -> str:
        return f"Container: {self.code}, {self.length}x{self.width}x{self.height}, {self.weight} tons, {self.loaded_weight} tons loaded, {self.weight_capacity} tons capacity"


def createContainerCode():
    id = "GAF"
    for _ in range(5):
        id += str(random.randint(0, 9))
    return id


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
    random_container = Container(
        random_code, length, 8, 8, weight, 0, weight_capacity)
    return random_container

