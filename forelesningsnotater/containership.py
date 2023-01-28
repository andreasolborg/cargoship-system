# TPK 4186 - 2023 - Assignment

# Teacher philospy: Few to none comments in code. The program should be self explaining.
# Dont use packages. e.g. pandas.

# There is no need for exeption handling. The program is a contract between the
# creator and user. It can for example come with instructions which is the
# contract.

# There is no preference in using OOP. As the program written here is basicly OOP.

# It is possible to submit multiple times. Every time you will get comments on
# how to perform better.


import sys

# 1 Containers
def Container_New(serialNumber, length, weight, cargo):
    return [serialNumber, length, weight, cargo]

def Container_NewSmall(serialNumber, cargo):
    return [serialNumber, 20, 2, cargo]

def Container_NewLarge(serialNumber, cargo):
    return [serialNumber, 40, 4, cargo]

def Container_GetSerialNumber(container):
    return container[0]

def Container_GetLength(container):
    return container[1]

def Container_GetWeight(container):
    return container[2]

def Container_GetCargo(container):
    return container[3]

def Container_SetSerialNumber(container, serialNumber):
    container[0] = serialNumber

def Container_SetLength(container, length):
    container[1] = length

def Container_SetWeight(container, weight):
    container[2] = weight

def Container_SetCargo(container, cargo):
    container[3] = cargo

def Container_GetTotalWeight(container):
    return Container_GetWeight(container) + Container_GetCargo(container)

# 2 Ships

def Ship_New(length, width, height):
    return [length, width, height, []]

def Ship_GetLength(ship):
    return ship[0]

def Ship_GetWidth(ship):
    return ship[1]

def Ship_GetHeight(ship):
    return ship[2]

def Ship_SetLength(ship, length):
    ship[0] = length

def Ship_SetWidth(ship, width):
    ship[1] = width

def Ship_SetHeight(ship, height):
    ship[2] = height

def Ship_GetContainers(ship):
    return ship[3]

def Ship_GetNumberOfContainers(ship):
    return len(Ship_GetContainers(ship))

def Ship_GetNthContainer(ship, index):
    containers = Ship_GetContainers(ship)
    return containers[index]

def Ship_InsertContainer(ship, container, index):
    containers = Ship_GetContainers(ship)
    containers.insert(index, container)

def Ship_AppendContainer(ship, container):
    containers = Ship_GetContainers(ship)
    containers.append(container)

def Ship_LoadContainer1(ship, container):
    containers = Ship_GetContainers(ship)
    containers.append(container)


def Ship_LoadContainer(ship, newContainer):
    newContainerWeight = Container_GetWeight(newContainer)
    loaded = False
    i = 0
    while i<Ship_GetNumberOfContainers(ship):
        container = Ship_GetNthContainer(ship, i)
        containerWeight = Container_GetWeight(container)
        if containerWeight<=newContainerWeight:
            Ship_InsertContainer(ship, newContainer, i)
            loaded = True
            break
        i = i + 1
    if not loaded:
        Ship_AppendContainer(ship, newContainer)

def Ship_PushContainer(ship,container):
    containers = Ship_GetContainers(ship)
    containers.append(container)

def Ship_PopContainer(ship):
    if Ship_GetNumberOfContainers() == 0:
        return None
    containers = Ship_GetContainers(ship)
    containers.pop()

def Ship_GetTopContainer(ship): #Add error handling for empty list
    if Ship_GetNumberOfContainers() == 0:
        return None
    containers = Ship_GetContainers(ship)
    return containers[-1]
    


# 3 Printers

def Container_Print(container):
    serialNumber = Container_GetSerialNumber(container)
    length = Container_GetLength(container)
    weight = Container_GetWeight(container)
    cargo = Container_GetCargo(container)
    totalWeight = Container_GetTotalWeight(container)  
    print(str(serialNumber) + " " + str(length) + " " + str(weight) + " " + str(cargo) + " " + str(totalWeight))

def Ship_Print(ship):
    length = Ship_GetLength(ship)
    width = Ship_GetWidth(ship)
    height = Ship_GetHeight(ship)
    containers = Ship_GetContainers(ship)
    print("Ship")
    print(str(length) + " " + str(width) + " " + str(height))
    for container in containers:
        Container_Print(container)

def Sort_Containers(ship, containers):
    containers = Ship_GetContainers(ship)
    containers.sort(key=lambda x: x[3])

    



# Main

ship = Ship_New(23,22,18)
c1 = Container_NewSmall(20230126001, 9)
c3 = Container_NewLarge(20230126003, 7)
c2 = Container_NewSmall(20230126002, 8)
c4 = Container_NewLarge(20230126004, 8)
Ship_LoadContainer(ship, c1)
Ship_LoadContainer(ship, c2)
Ship_LoadContainer(ship, c3)
Ship_LoadContainer(ship, c4)
print(Ship_GetContainers)

Ship_Print(ship)

#Sort_Containers(ship, Ship_GetContainers)




