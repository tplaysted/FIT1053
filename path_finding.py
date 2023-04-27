"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a function to create a path, encoded as an Itinerary, that is shortest for some Vehicle.

@file path_finding.py
"""
import math
import networkx as nx

from city import City, get_city_by_id
from itinerary import Itinerary
from vehicles import Vehicle, create_example_vehicles
from csv_parsing import create_cities_countries_from_csv
from map_plotting import plot_itinerary


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Itinerary | None:
    """
    Returns the shortest path between two cities for a given vehicle as an Itinerary,
    or None if there is no path.

    :param vehicle: The vehicle to use.
    :param from_city: The departure city.
    :param to_city: The arrival city.
    :return: The shortest path from departure to arrival, or None if there is none.
    """

    # ---- We need to build a graph representation of the world ---- #

    g = nx.complete_graph([x for x in City.id_to_cities])

    for edge in g.edges():
        time = vehicle.compute_travel_time(get_city_by_id(edge[0]), get_city_by_id(edge[1]))

        if time == math.inf:
            g.remove_edge(edge[0], edge[1])
        else:
            g.add_edge(edge[0], edge[1], weight=time)

    # ---- Compute the shortest path ---- #

    if not nx.has_path(g, from_city.city_id, to_city.city_id):
        return None
    else:
        path = [get_city_by_id(x) for x in nx.shortest_path(g, from_city.city_id, to_city.city_id, weight='weight')]
        return Itinerary(path)


if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    vehicles = create_example_vehicles()

    test_vehicle = vehicles[2]
    shortest_path = find_shortest_path(test_vehicle, get_city_by_id(1392685764), get_city_by_id(1484074285))
    print(f"\t{test_vehicle.compute_itinerary_time(shortest_path)}"
          f" hours with {test_vehicle} with path {shortest_path}.")

    plot_itinerary(shortest_path)

    # from_cities = list()
    # for city_id in [1036533631, 1036142029, 1458988644]:
    #     from_cities.append(get_city_by_id(city_id))
    #
    # to_cities = list(from_cities)

    # for from_city in from_cities:
    #     to_cities -= {from_city}
    #     for to_city in to_cities:
    #         print(f"{from_city} to {to_city}:")
    #         for test_vehicle in vehicles:
    #             shortest_path = find_shortest_path(test_vehicle, from_city, to_city)
    #             print(f"\t{test_vehicle.compute_itinerary_time(shortest_path)}"
    #                   f" hours with {test_vehicle} with path {shortest_path}.")
