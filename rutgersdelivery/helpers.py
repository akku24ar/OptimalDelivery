from getpass import getpass
from passlib.hash import bcrypt
import pyinputplus as pyip
import mlrose_hiive as mlrose
import numpy as np
from collections import OrderedDict
import constants as c

# Validate password before entering application


def validate_password():
    # Prompt User for Password
    password = getpass()
    # Hash Password
    hasher = bcrypt.using(rounds=13)
    # Compare Given Password Hash with Correct Password Hash
    applicationContinue = hasher.verify(
        password, "$2b$13$sBfW5r9Cnn6729OtbeY4J.qCqbNieBZt0ZV/dw68c3z9oFjkZPRUi")
    # Print Result Message
    if applicationContinue is False:
        print(c.bcolors.FAIL, "Unable to verify password. See README for correct password. Retry Below:", c.bcolors.ENDC)
        return False
    else:
        print(c.bcolors.OKGREEN,
              "Password Validated. Starting Application...", c.bcolors.ENDC)
        print("")
        return True

# Create List of Destinations


def create_destination_list(coordinateMap):
    validValues = []
    for destination in coordinateMap:
        validValues.append(destination)
    return validValues

# Reverse a Map


def reverse_destination_map(coordinateMap):
    invertedCoordinateMap = {v: k for k, v in coordinateMap.items()}
    return invertedCoordinateMap

# Validate that there enough trucks for routes


def validate_trucks_and_routes():
    print(c.bcolors.BOLD, "How Many Trucks are Available?", c.bcolors.ENDC)
    amountOfTrucks = pyip.inputNum()
    print(c.bcolors.BOLD, "How Many Routes are Required?", c.bcolors.ENDC)
    amountofRoutes = pyip.inputNum()

    if amountOfTrucks < amountofRoutes:
        print(c.bcolors.FAIL, "There are not enough trucks for the required routes. Please make sure the amount of trucks is equal to or more than the required routes.", c.bcolors.ENDC)
        print(c.bcolors.BOLD,
              "Please input valid values of trucks and routes to continue", c.bcolors.ENDC)
        print("")
        return False
    elif amountOfTrucks == amountofRoutes:
        print(c.bcolors.OKGREEN,
              "Equivalent number of trucks and routes. Continuing...", c.bcolors.ENDC)
        print("")
        return amountOfTrucks
    elif amountofRoutes < amountOfTrucks:
        print(c.bcolors.OKGREEN, "Sufficient amount of trucks supplied.",
              amountOfTrucks-amountofRoutes, "trucks will not be used.", c.bcolors.ENDC)
        print("")
        return amountofRoutes

# Collect Destinations in Route


def get_route_info(truck, validValues):
    print(c.bcolors.HEADER, "Getting Route Info for Truck", truck+1, c.bcolors.ENDC)
    result = ""
    routeList = []
    while result != "END ROUTE SELECTION":
        print(c.bcolors.WARNING,
              "When finished, select 'END ROUTE SELECTION'", c.bcolors.ENDC)
        result = pyip.inputMenu(validValues, lettered=True, numbered=False)
        if result != "END ROUTE SELECTION":
            routeList.append(result)
        print(c.bcolors.OKCYAN, "Current Route List:", routeList, c.bcolors.ENDC)
        print("")

    # Filter results to remove duplicates
    filteredResult = list(OrderedDict.fromkeys(routeList))
    return filteredResult

# Create Dictionary of All Route Locations


def get_coordinate_location(locations):
    coordinateLocation = {}
    counter = 0
    for item in locations:
        coordinateLocation[item] = counter
        counter += 1
    return coordinateLocation

# Map Route to Coordinates


def convert_route_to_coordinates(routeInfo):
    routeCoordinates = {}
    for destination in routeInfo:
        routeCoordinates[destination] = c.coordinateMap[destination]
    return routeCoordinates

# Get Distance Between Two Points


def get_distance(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

# Generate Weighted Graph of Route


def generate_graph(coordinateLocations, coordinateMap):
    output = []
    v = list(coordinateMap.values())
    k = list(coordinateMap.keys())
    i = 0
    while (i < len(v)):
        for item in v[i+1:]:
            distance = get_distance(v[i], item)
            output.append((coordinateLocations.get(
                k[i]), coordinateLocations.get(k[v.index(item)]), distance))
        i += 1
    return output

# Add Dummy to Graph


def insert_dummy(start, loc, coordinateLocations):
    dummyInt = len(coordinateLocations.keys())
    for k, v in coordinateLocations.items():
        if (start == k):
            loc.append((v, dummyInt, 0.1))
        elif (k == "Truck Depot"):
            loc.append((v, dummyInt, 0.1))
        else:
            loc.append((v, dummyInt, 100000))
    return loc

# Get Shortest Path (With Dummy Node)


def get_shortest_route(dist_list, lenList):
    fitness_coords = mlrose.TravellingSales(distances=dist_list)
    problem_fit = mlrose.TSPOpt(
        length=lenList, fitness_fn=fitness_coords, maximize=False)
    best_state, best_fitness, x = mlrose.genetic_alg(
        problem_fit, random_state=2)
    return best_state

# Reorder Path with Pickup Point and Last Point (Without Dummy Node)


def get_correct_order(route, last, indexes):
    orderedRoute = route.tolist()
    orderedRoute.remove(last)
    if (orderedRoute[0] == 0):
        orderedRoute.append(last)
        return orderedRoute
    elif (orderedRoute[len(orderedRoute)-1] == 0):
        orderedRoute = orderedRoute[::-1]
        orderedRoute.append(last)
        return orderedRoute
    else:
        reordered = []
        pickupPointIndex = orderedRoute.index(0)
        for k, v in indexes.items():
            if (v == orderedRoute[pickupPointIndex]):
                cur = np.asarray(c.coordinateMap[k])
            elif (v == orderedRoute[pickupPointIndex-1]):
                prev = np.asarray(c.coordinateMap[k])
            elif (v == orderedRoute[pickupPointIndex+1]):
                next = np.asarray(c.coordinateMap[k])
        #print(prev, cur, next)

        dist1 = np.linalg.norm(cur-prev)
        dist2 = np.linalg.norm(cur-next)
        #print(dist1, dist2)
        if (dist1 < dist2):  # ABCKUV wrong
            reordered.append(0)
            for item in orderedRoute[:pickupPointIndex]:
                reordered.append(item)
            for item in reversed(orderedRoute[pickupPointIndex+1:]):
                reordered.append(item)
            reordered.append(last)
        else:
            for item in orderedRoute[pickupPointIndex:]:
                reordered.append(item)
            for item in orderedRoute[:pickupPointIndex]:
                reordered.append(item)
            reordered.append(last)
        return reordered

# Get Path with Locations and Total Distance


def get_final_path(ordered, locationList):
    output = []
    totalDistance = 0
    for index in ordered:
        output.append(locationList[index])
    cur = 0
    nex = 1
    while (nex < len(output)):
        temp = get_distance(np.asarray(c.coordinateMap[output[cur]]), np.asarray(
            c.coordinateMap[output[nex]]))
        totalDistance = totalDistance + temp
        cur += 1
        nex += 1

    return output, totalDistance
