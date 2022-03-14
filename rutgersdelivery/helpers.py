from getpass import getpass
from passlib.hash import bcrypt
import pyinputplus as pyip
from collections import OrderedDict
import constants as c

## Validate password before entering application
def validate_password():
    # Prompt User for Password
    password = getpass()
    #Hash Password
    hasher = bcrypt.using(rounds=13)
    #Compare Given Password Hash with Correct Password Hash
    applicationContinue = hasher.verify(password, "$2b$13$sBfW5r9Cnn6729OtbeY4J.qCqbNieBZt0ZV/dw68c3z9oFjkZPRUi")
    #Print Result Message
    if applicationContinue is False:
        print(c.bcolors.FAIL, "Unable to verify password. See README for correct password. Retry Below:", c.bcolors.ENDC)
        return False
    else: 
        print(c.bcolors.OKGREEN, "Password Validated. Starting Application...", c.bcolors.ENDC)
        print("")
        return True

## Create List of Destinations
def create_destination_list(coordinateMap):
    validValues = []
    for destination in coordinateMap:
        validValues.append(destination)
    return validValues

## Reverse a Map
def reverse_destination_map(coordinateMap):
    invertedCoordinateMap = {v: k for k, v in coordinateMap.items()}
    return invertedCoordinateMap

## Validate that there enough trucks for routes
def validate_trucks_and_routes():
    print(c.bcolors.BOLD, "How Many Trucks are Available?", c.bcolors.ENDC)
    amountOfTrucks = pyip.inputNum()
    print(c.bcolors.BOLD, "How Many Routes are Required?", c.bcolors.ENDC)
    amountofRoutes = pyip.inputNum()

    if amountOfTrucks<amountofRoutes:
        print(c.bcolors.FAIL, "There are not enough trucks for the required routes. Please make sure the amount of trucks is equal to or more than the required routes.", c.bcolors.ENDC)
        print(c.bcolors.BOLD, "Please input valid values of trucks and routes to continue", c.bcolors.ENDC)
        print("")
        return False
    elif amountOfTrucks==amountofRoutes:
        print(c.bcolors.OKGREEN, "Equivalent number of trucks and routes. Continuing...", c.bcolors.ENDC)
        print("")
        return amountOfTrucks
    elif amountofRoutes<amountOfTrucks:
        print(c.bcolors.OKGREEN, "Sufficient amount of trucks supplied.", amountOfTrucks-amountofRoutes, "trucks will not be used.", c.bcolors.ENDC)
        print("")
        return amountofRoutes

## Collect Destinations in Route
def get_route_info(truck, validValues):
    print(c.bcolors.HEADER, "Getting Route Info for Truck", truck+1, c.bcolors.ENDC)
    result = ""
    routeList = []
    while result != "END ROUTE SELECTION":
        print(c.bcolors.WARNING, "When finished, select 'END ROUTE SELECTION'", c.bcolors.ENDC)
        result = pyip.inputMenu(validValues, lettered=True, numbered=False)
        if result != "END ROUTE SELECTION":
            routeList.append(result)
        print(c.bcolors.OKCYAN, "Current Route List:", routeList, c.bcolors.ENDC)
        print("")

    # Filter results to remove duplicates
    filteredResult = list(OrderedDict.fromkeys(routeList))
    return filteredResult

## Map Route to Coordinates
def convert_route_to_coordinates(routeInfo, coordinateMap):
    routeCoordinates = []
    for destination in routeInfo:
        destinationCoordinate = coordinateMap[destination]
        routeCoordinates.append(destinationCoordinate)
    print(routeCoordinates)
    return routeCoordinates