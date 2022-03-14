import constants as c
import helpers

# Rutgers Delivery System


print(c.bcolors.HEADER + "Welcome to the Rutgers Delivery System. Please enter the application password to continue (See README for password)", c.bcolors.ENDC)

# Verify Password
passwordValidated = False
while passwordValidated is False:
    passwordValidated = helpers.validate_password()

# Verify Correct Values of Routes and Trucks
trucksforRoutes = False
while trucksforRoutes is False:
    trucksforRoutes = helpers.validate_trucks_and_routes()

# Collect Routes and Calculate Shortest Path
for truck in range(trucksforRoutes):
    # Create a List of Valid Destinations
    validDestinations = helpers.create_destination_list(c.coordinateMap)
    validDestinations.append("END ROUTE SELECTION")
    # Ask User to Create Route for Truck
    routeInfo = helpers.get_route_info(truck, validDestinations)
    # Convert Route List to Coordinates List
    coordinateRoute = helpers.convert_route_to_coordinates(
        routeInfo, c.coordinateMap)
    optimalRoute = helpers.get_shortest_route(coordinateRoute)
    print(optimalRoute)
    optimalRouteOrdered = helpers.get_correct_order(optimalRoute)
    finalRoute = helpers.get_location_path(
        optimalRouteOrdered, coordinateRoute)
    print(finalRoute)
