# Author: Andreas Olborg
# Import the classes from the other files
from Container import *
from ContainerSet import *
from ContainerSetManager import *
from ContainerShipManager import *
from ContainerStack import *
from ContainerSection import *

# random.seed(50) # Set the seed for the random number generator

def task1():
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

    # Try to set the cargo of the containers to 1337 tons, which is more than the max weight
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
    
def task2():
    # Design a data structure to encode a set of containers and implement the associate management functions (add a container, remove a container, look for a container. . . ).
    c1 = Container("ABO123", 20, 2, 0, 20)
    c2 = Container("ABO345", 40, 4, 0, 22)
    c3 = Container("ABO678", 20, 2, 0, 20)
    c4 = Container("ABO910", 40, 4, 0, 22)
    c5 = Container("ABO111", 20, 2, 0, 20)
    c6 = Container("ABO222", 40, 4, 0, 22)
    c7 = Container("ABO333", 20, 2, 0, 20)
    c8 = Container("ABO444", 40, 4, 0, 22)

    # Create a new container set
    container_set = ContainerSet()

    # Add the containers to the set
    container_set.add_container_to_set(c1)
    container_set.add_container_to_set(c2)
    container_set.add_container_to_set(c3)
    container_set.add_container_to_set(c4)
    container_set.add_container_to_set(c5)
    container_set.add_container_to_set(c6)
    container_set.add_container_to_set(c7)
    container_set.add_container_to_set(c8)

    # Print the set
    print(container_set.containers)

    # Remove a container from the set
    container_to_remove = container_set.get_nth_container(0)
    container_set.remove_container_from_set(container_to_remove)

    # Print the set, the first container should be gone
    print(container_set.containers)

    #Look for a container in the set using the code of the container
    container_to_find_with_code = container_set.get_nth_container(0).get_code() # Get the code of the first container in the set
    print(container_set.find_container(container_to_find_with_code)) # Print the container, if it exists in the set

    # Flush the set (remove all containers)
    container_set.flush()

    print("Print the set, it should be empty")
    print(container_set.containers)

def task3():
    # Design a function that generates a container “at random”, by choosing a length, a
    # load and code for the container. This function may be parametric. Design a function
    # (using the previous one) that generates at random a set of containers.
    random_container = generate_random_container()
    print(random_container)

    random_20ft_container = generate_random_container(20)
    print(random_20ft_container)

    random_40ft_container = generate_random_container(40)
    print(random_40ft_container)

    # Create a new container set
    container_set = ContainerSet()
    # Generate a set of random containers, with length 20
    container_set.generate_random_containers(10, 20)
    print(container_set.containers)

    container_set.flush()
    # Generate a set of random containers, with length 40. The set should be empty, since we flushed the previous set
    container_set.generate_random_containers(10, 40)
    print(container_set.containers)

    container_set.flush()

def task4():
    demo_set = ContainerSet()

    # Generate a set of 15 random containers, with length 20 or 40 (chosen at random)
    demo_set.generate_random_containers(15)
    save_set_of_containers(demo_set, "./solution/set_of_containers/demo_set.tsv")
    # The set should be saved in the file "demo_set.tsv" in the folder "set_of_containers"

    demo_set.flush()

    # Load the set from the file "demo_set.tsv" in the folder "set_of_containers"
    demo_set = load_set_of_containers("./solution/set_of_containers/demo_set.tsv")
    # The set should be loaded from the file "demo_set.tsv" in the folder "set_of_containers"
    print(demo_set.containers)

def task5():
    # Design a data structure to encode container ships implement the associated management
    # functions: look for a container in the ship, look for a place where a container
    # can be loaded, load a container into the ship, remove a container from the ship. . . .
    # Note that it is not possible to load a 40 feet container onto a single 20 feet container
    # (there should no holes).

    # Here, my assumptions #1 are important. These are explained in the README.md file
    ship_dimensions = [24, 22, 18] # [length, width, height]
    ship = ContainerShip(ship_dimensions[0], ship_dimensions[1], ship_dimensions[2])

    # Create a set of 500 big and small containers (100 of each) to load into the ship (the set is generated randomly)
    container_set = ContainerSet()
    container_set.generate_random_containers(250, 20)
    container_set.generate_random_containers(250, 40)

    # Load the containers into the ship
    for container in container_set.containers:
        ship.add_container(container)
    

    # Find places where containers can be loaded. These are the stacks that are not full, and may not be the most optimal places to load the containers.
    # !!! Make this a function of the ship !!!
    available_stacks = ship.get_stacks_that_are_not_full()
    print("Available stacks to load containers: ")
    for stack in available_stacks:
        print(stack.get_location_in_section(), "in section ", stack.get_sectionID())

    # Find a container in the ship
    container_to_find, section, stack = ship.find_container("0490")
    print("Container was found: ", container_to_find.get_code())

    # Remove the container we just found from the ship
    print("Removing container: ", container_to_find.get_code())
    ship.remove_container("0490") # This function takes in the code of the container to remove


    # Find a container in the ship
    container_to_find = ship.find_container("0490")
    print("Container to find: ", container_to_find)
    
    # Print the ship
    print(ship)

def task6():
    time_start = time.time()
    # Design a function that prints out the load of a ship into a file and function that loads
    # the load of a ship from a file. Propose a TSV format for these files.
    ship_dimensions = [24, 22, 18] # [length, width, height]
    ship = ContainerShip(ship_dimensions[0], ship_dimensions[1], ship_dimensions[2])

    # Create a set of 5000 big and small containers to load into the ship (the set is generated randomly)
    container_set = ContainerSet()
    container_set.generate_random_containers(5000) # 5000 containers of random length

    save_set_of_containers(container_set, "./solution/set_of_containers/demo_set_5k.tsv")

    # Load the containers containter by container into the ship (task 7 actually)
    for container in container_set.containers:
        ship.add_container(container)

    # Print the ship
    print(ship)

    print("New ship: \n\n\n")

    # Save the ship to a file (pretty version)
    save_ship_with_containers_to_file(ship, "./solution/saved_ships/demo_ship.tsv")

    # Make a new Container Set, and load the containers from the file to a new Ship. These two ships should be identical
    container_set = load_set_of_containers("./solution/set_of_containers/demo_set_5k.tsv")
    ship2 = ContainerShip(ship_dimensions[0], ship_dimensions[1], ship_dimensions[2])
    
    # Load the containers into the ship
    for container in container_set.containers:
        ship2.add_container(container)

    # Save the ship to a file
    # save_ship_with_containers_to_file(ship2, "./solution/saved_ships/demo_ship_basic2.tsv")

    # Print the ship
    print(ship2)


    end_time = time.time()
    print("Time load the ship and saving it: ", end_time - time_start)

def task7():
    # THE PART WHERE YOU ARE SUPPOSED TO LOAD A SHIP CONTAINER BY CONTAINER IS SOLVED AND DEMONSTRATED IN SAVE_SHIP_WITH_CONTAINERS_TO_FILE() IN THE CONTAINERSHIPMANAGER CLASS
    # THIS FUNCTION IS CALLED IN TASK6()
    ship_dimensions = [24, 22, 18] # [length, width, height]
    ship = ContainerShip(ship_dimensions[0], ship_dimensions[1], ship_dimensions[2])

    # Create a set of 5000 big and small containers to load into the ship (the set is generated randomly)
    container_set = ContainerSet()
    container_set.generate_random_containers(5000) # 5000 containers of random length

    save_set_of_containers(container_set, "./solution/set_of_containers/demo_set_5k.tsv")

    # Load the containers containter by container into the ship (task 7 actually)
    containers_in_ship = []
    for container in container_set.containers:
        ship.add_container(container)
        containers_in_ship.append(container)
 
    # Unload the ship container by container by always popping from the heaviest stack in the heaviest section
    # Store the popped containers in a list (referring to the task description of "corresponding ordered list of containers")
    popped_containers = ship.unload_all_containers()
    for container in popped_containers:
        print("Unloading ship... Popped container: ", container)
    
def task8():
    # For stability reasons, heady containers must be placed below light ones. Design a
    # new loading function that takes into account this constraint, i.e. that piles containers
    # in decreasing weight order.

    # Here, my assumptions #2 are important. These are explained in the documentation.txt file
    # The function is implemented in the ContainerStack class, in the add_container_to_stack function.
    # The functionality of this logic is also confirmed in the ship.are_containers_placed_in_descending_order() function.

    return

def task9():
    time_start = time.time()
    # Design a function that prints out the load of a ship into a file and function that loads
    # the load of a ship from a file. Propose a TSV format for these files.
    ship = load_ship_with_containers_from_file(6500)

    # Calculate the weight of the parts of the ship
    print("Total weight of the portside: ", ship.calculate_port_weight(), " tonnes")
    print("Total weight of the starboard: ", ship.calculate_starboard_weight(), " tonnes")
    print("Total weight of the front: ", ship.calculate_front_weight(), " tonnes")
    print("Total weight of the middle: ", ship.calculate_middle_weight(), " tonnes")
    print("Total weight of the back: ", ship.calculate_back_weight(), " tonnes")
    print("Total weight of the ship: ", ship.calculate_total_weight(), " tonnes")

    print("Are containers placed in descending order? : ", ship.are_containers_placed_in_descending_order())
    print("Are ships balanced? : ", ship.is_ship_balanced(5,10))



    end_time = time.time()
    print("Code run-time: ", end_time - time_start)
    return

def task10():
    # Design a new loading function that takes into account the stability constraints.
    # Assumptions #4 describes the solving of this task
    return

def task11():
    # Assuming that it takes about 4 minutes to load or unload a container with a crane.
    # Design a function that calculates how much time it takes to load or unload the ship
    # with 1 crane.

    # We have to load the ship with 1 crane, and unload it with 1 crane. How much time does it take?
    # We are keeping track of an operation counter, and we are adding 1 to it every time we load or unload a container.
    # To get the time, we multiply the operation counter by 4 minutes (240 seconds)

    # Load the ship from file
    ship = load_ship_with_containers_from_file(6500)

    # Calculate the time to load the ship
    print("If we use 1 crane to load/unload the ship, it will take:")
    single_crane_loading_operations = ship.get_single_crane_loading_operation_counter()
    time_for_single_crane_loading = ship.get_time_to_load_ship(single_crane_loading_operations)
    print(time_for_single_crane_loading)

    # Calculate the time to unload the ship
    single_crane_unloading_operations = ship.get_single_crane_unloading_operation_counter()
    time_for_single_crane_unloading = ship.get_time_to_unload_ship(single_crane_unloading_operations)
    print(time_for_single_crane_unloading)
    



    

def task12():
    # Same questions with 4 cranes. What do you observe?
    # We simplify the the problem by assuming we only have 3 cranes. Then we would need to 

    # Load the ship from file   
    ship = load_ship_with_containers_from_file(6500)
    
    # Calculate the time to load the ship with 3 cranes
    print("If we use 3 cranes to load/unload the ship, it will take:")
    max_operations_for_three_cranes = ship.get_max_triple_crane_loading_operation_counter()
    time_for_three_cranes = ship.get_time_to_load_ship(max_operations_for_three_cranes)
    print(time_for_three_cranes)

    # Calculate the time to unload the ship with 3 cranes
    max_operations_for_three_cranes = ship.get_max_triple_crane_unloading_operation_counter()
    time_for_three_cranes = ship.get_time_to_unload_ship(max_operations_for_three_cranes)
    print(time_for_three_cranes)


def main():
    begin_time = time.time()
    print("------------------------------------- TASK 1 -------------------------------------")
    task1()
    print("------------------------------------- TASK 2 -------------------------------------")
    task2()
    print("------------------------------------- TASK 3 -------------------------------------")
    task3()
    print("------------------------------------- TASK 4 -------------------------------------")
    task4()
    print("------------------------------------- TASK 5 -------------------------------------")
    task5()
    print("------------------------------------- TASK 6 -------------------------------------")
    task6()
    print("------------------------------------- TASK 7 -------------------------------------")
    task7()
    print("------------------------------------- TASK 8 -------------------------------------")
    task8()
    print("------------------------------------- TASK 9 -------------------------------------")
    task9()
    print("------------------------------------- TASK 10 -------------------------------------")
    task10()
    print("------------------------------------- TASK 11 -------------------------------------")
    task11()
    print("------------------------------------- TASK 12 -------------------------------------")
    task12()
    end_time = time.time()
    print("Total run-time of all tasks: ", end_time - begin_time)



    
if __name__ == "__main__":
    main()
