import random

class Container:
# The constructor of the class Container
# Kan eventuelt gjøre om length, width og height til size?
    def __init__(self, code, length, width, height, weight, loaded_weight, weight_capacity):
        self.code = code
        self.length = length
        self.width = width
        self.height = height
        self.loaded_weight = loaded_weight
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

    def get_loaded_weight(self):
        return self.loaded_weight

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

    def set_loaded_weight(self, loaded_weight):
        self.loaded_weight = loaded_weight

    def set_weight(self, weight):
        self.weight = weight
    
    def set_weight_capacity(self, weight_capacity):
        self.weight_capacity = weight_capacity

    # tostring
    def __str__(self) -> str:
        return f"Container: {self.code}, {self.length}x{self.width}x{self.height}, {self.weight} tons, {self.loaded_weight} tons loaded, {self.weight_capacity} tons capacity"


# Generate a random container with a random code, length, width, height and weight
# The loaded weight should be 0. The weight should be 2 tons for a 20 foot container and 4 tons for a 40 foot container.

def generate_random_container():
    possible_containers = [[20, 2, 20], [40, 2, 22]]
    random_container_ = random.choice(possible_containers)

    random_code = random.randint(100000, 999999)
    length = random_container_[0]
    weight = random_container_[1]
    weight_capacity = random_container_[2]

    random_container = Container(random_code, length, 8, 8, weight, 0, weight_capacity) # The loaded weight should be 0
    return random_container


print(generate_random_container())








