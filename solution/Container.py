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
        
    
    def set_cargo(self, cargo):
        if cargo > self.weight_capacity:
            raise Exception("Cargo is too heavy")
        self.cargo = cargo

    # tostring
    def __str__(self) -> str:
        return f"ContainerID:{self.code}\tlength:{self.length}\tTotal weight= {self.weight} + {self.cargo} = {self.weight+self.cargo}"

    # tostring for list of containers
    def __repr__(self) -> str:
        return f"C:{self.get_code()} L:{self.get_length()} W:{self.get_cargo()} TW:{self.get_total_weight()}"


def create_container_code():
    if not hasattr(create_container_code, "counter"):
        create_container_code.counter = 0
    id = "{:04d}".format(create_container_code.counter)
    create_container_code.counter += 1
    return id


# Task 2.1.2
# Generate a random container with a random code, length, width, height and weight
# The loaded weight should be 0. The weight should be 2 tons for a 20 foot container and 4 tons for a 40 foot container.

def generate_random_container(size=None):
    possible_containers = [[20, 2, 20], [40, 4, 22]]
    random_container_ = random.choice(possible_containers)
    if size == 20:
        random_container_ = possible_containers[0]
    elif size == 40:
        random_container_ = possible_containers[1]
    else: # size == None or size != 20 or size != 40
        random_container_ = random.choice(possible_containers)
        

    random_code = create_container_code()
    length = random_container_[0]
    weight = random_container_[1]
    weight_capacity = random_container_[2]
    random_container = Container(random_code, length, weight, random.randint(0, weight_capacity), weight_capacity) ## random.randint(0, weight_capacity) is the cargo weight (loaded weight) make it a function
    return random_container


def main():
    start = time.time()

    # Create two containers
    big_container = Container("ABO123", 20, 2, 0, 20)
    small_container = Container("ABO345", 40, 4, 0, 22)

    # To-string functions made in the class, and are called automatically when using print(), so we can just print the objects
    print(big_container)
    print(small_container)

    # Set the cargo of the containers to 10 tons
    big_container.set_cargo(10)
    small_container.set_cargo(10)

    print(big_container)
    print(small_container)

    # Try to set the cargo of the containers to 1337 tons, which is more than the max weight. This should raise an exception
    try:
        big_container.set_cargo(1337)
    except Exception as e:
        print(e)
    
    try:
        small_container.set_cargo(1337)
    except Exception as e:
        print(e)
        
    # The cargo should still be 10 tons
    print(small_container)
    print(big_container)

    random_container = generate_random_container()
    print(random_container)


    print(time.time() - start)

if __name__ == "__main__":
    main()