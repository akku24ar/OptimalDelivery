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

    # Get Dictionary of Locations
    dictLocations = helpers.get_coordinate_location(routeInfo)

    # Get Route Locations as Dict
    coordinateRoute = helpers.convert_route_to_coordinates(routeInfo)

    # Generate Weighted Graph
    coordinateGraph = helpers.generate_graph(dictLocations, coordinateRoute)

    # Insert Dummy Node to Graph
    finalCoordinateGraph = helpers.insert_dummy(
        routeInfo[0], coordinateGraph, dictLocations)

    # Get the Optimal Route (Including Dummy Node)
    optimalRoute = helpers.get_shortest_route(
        finalCoordinateGraph, len(routeInfo)+1)

    optimalRoute = optimalRoute[optimalRoute != len(routeInfo)]

    # Reorder Route with Starting and End Location (Without Dummy Node)
    optimalRouteOrdered = helpers.get_correct_order(
        optimalRoute, len(routeInfo)-1, dictLocations)

    # Get Location Names and Total Path Distance
    finalRoute, finalDistance = helpers.get_final_path(
        optimalRouteOrdered, routeInfo)
