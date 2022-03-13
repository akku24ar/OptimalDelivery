import pyinputplus as pyip
from getpass import getpass
from passlib.hash import bcrypt
from collections import OrderedDict

## ANSI escape sequences for pretty font in CLI
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

## Validate password before entering application
def get_password():
    # Prompt User for Password
    password = getpass()

    #Hash Password
    hasher = bcrypt.using(rounds=13)

    #Compare Given Password Hash with Correct Password Hash
    applicationContinue = hasher.verify(password, "$2b$13$sBfW5r9Cnn6729OtbeY4J.qCqbNieBZt0ZV/dw68c3z9oFjkZPRUi")

    #Print Result Message
    if applicationContinue is False:
        return False
    else: 
        print(bcolors.OKGREEN, "Password Validated. Starting Application...", bcolors.ENDC)
        print("")
        return True

## Validate that there enough trucks for routes
def validate_trucks_and_routes():
    global trucksforRoutes

    print(bcolors.BOLD, "How Many Trucks are Available?", bcolors.ENDC)
    amountOfTrucks = pyip.inputNum()
    print(bcolors.BOLD, "How Many Routes are Required?", bcolors.ENDC)
    amountofRoutes = pyip.inputNum()

    if amountOfTrucks<amountofRoutes:
        return False
    elif amountOfTrucks==amountofRoutes:
        trucksforRoutes = amountOfTrucks
        print(bcolors.OKGREEN, "Equivalent number of trucks and routes. Continuing...", bcolors.ENDC)
        print("")
        return True
    elif amountofRoutes<amountOfTrucks:
        trucksforRoutes = amountofRoutes
        print(bcolors.OKGREEN, "Sufficient amount of trucks supplied.", amountOfTrucks-amountofRoutes, "trucks will not be used.", bcolors.ENDC)
        print("")
        return True

## Collect Destinations in Route
def get_route_info(truck):
    print(bcolors.HEADER, "Getting Route Info for Truck", truck+1, bcolors.ENDC)
    result = ""
    routeList = []
    while result != "END ROUTE SELECTION":
        print(bcolors.WARNING, "When finished, select 'END ROUTE SELECTION'", bcolors.ENDC)
        result = pyip.inputMenu(validValues, lettered=True, numbered=False)
        if result != "END ROUTE SELECTION":
            routeList.append(result)
        print(bcolors.OKCYAN, "Current Route List:", routeList, bcolors.ENDC)
        print("")

    # Filter results to remove duplicates
    filteredResult = list(OrderedDict.fromkeys(routeList))
    return filteredResult

def convert_route_to_coordinates(routeInfo):
    routeCoordinates = []
    for destination in routeInfo:
        destinationCoordinate = coordinateMap[destination]
        routeCoordinates.append(destinationCoordinate)
    print(routeCoordinates)
    return routeCoordinates


# Valid Destinations
validValues = ["Food Distribution Hub",
               "Tacoria",
               "Halal Guys",
               "Hansel n Griddle",
               "Tatas Pizza",
               "Judys Kitchen",
               "Cafe West",
               "The Yard",
               "Brower Commons",
               "Panera Bread",
               "Busch Dining Hall"
               "Smoothie Bar",
               "Woodys",
               "Kilmers Market",
               "Henrys Diner",
               "Rutgers Cinema",
               "Livingston Dining Hall",
               "Neilson Dining Hall",
               "Harvest",
               "Cook Douglass Student Center",]
validValues.append("END ROUTE SELECTION")

coordinateMap = {"Food Distribution Hub": (5,5),
                "Tacoria": (6,6),
                "Halal Guys": (6,7),
                "Hansel n Griddle": (7,8),
                "Tatas Pizza": (9,9),
                "Judys Kitchen": (8,8),
                "Cafe West": (6,9),
                "The Yard": (7,9),
                "Brower Commons": (9,8),
                "Panera Bread": (8,6),
                "Busch Dining Hall": (4,6),
                "Smoothie Bar": (4,7),
                "Woodys": (3,8),
                "Kilmers Market": (3,3),
                "Henrys Diner": (2,2),
                "Rutgers Cinema": (2,4),
                "Livingston Dining Hall": (4,4),
                "Neilson Dining Hall": (7,3),
                "Harvest": (8,4),
                "Cook Douglass Student Center": (9,2)}

invertedCoordinateMap = {v: k for k, v in coordinateMap.items()}
               
print(bcolors.HEADER + "Welcome to the Rutgers Delivery System. Please enter the application password to continue (See README for password)", bcolors.ENDC)

# Verify Password
while get_password() is False:
    print(bcolors.FAIL, "Unable to verify password. See README for correct password. Retry Below:", bcolors.ENDC)

# Verify Correct Values of Routes and Trucks
while validate_trucks_and_routes() is False:
    print(bcolors.FAIL, "There are not enough trucks for the required routes. Please make sure the amount of trucks is equal to or more than the required routes.", bcolors.ENDC)
    print(bcolors.BOLD, "Please input valid values of of trucks and routes to continue", bcolors.ENDC)
    print("")
    

for truck in range(trucksforRoutes):
    routeInfo = get_route_info(truck)
    coordinateRoute = convert_route_to_coordinates(routeInfo)