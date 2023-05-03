"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a function to create a path, encoded as an Itinerary, that is shortest for some Vehicle.

@file path_finding.py
"""
import math
import networkx as nx

from city import City, get_city_by_id
from itinerary import Itinerary
from vehicles import Vehicle, create_example_vehicles, DiplomacyDonutDinghy
from csv_parsing import create_cities_countries_from_csv
from map_plotting import plot_itinerary


class WorldGraphs:
    """
    A global class which stores a dictionary of graph objects, unique to each vehicle instantiation
    """

    vehicle_to_graphs = dict()


def build_world_graph(vehicle: Vehicle) -> nx.Graph():
    """
    Takes all cities in existence at run-time and computes a time-weighted graph of the world
    based on a specific vehicle. Adds this (very large) graph to the WorldGraph dictionary,
    or overwrites it if one already exists.

    :param vehicle: to travel the world with
    :return: None
    """

    g = nx.complete_graph([x for x in City.id_to_cities])  # initialise a completely connected graph

    for edge in g.edges():  # modify this graph one edge at a time, removes edges if travel is not possible
        time = vehicle.compute_travel_time(get_city_by_id(edge[0]), get_city_by_id(edge[1]))

        if time == math.inf:
            g.remove_edge(edge[0], edge[1])
        else:
            g.add_edge(edge[0], edge[1], weight=time)

    WorldGraphs.vehicle_to_graphs[str(vehicle)] = g  # call hash() to index the vehicle
    return g


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Itinerary | None:
    """
    Returns the shortest path between two cities for a given vehicle as an Itinerary,
    or None if there is no path.

    :param vehicle: The vehicle to use.
    :param from_city: The departure city.
    :param to_city: The arrival city.
    :return: The shortest path from departure to arrival, or None if there is none.
    """
    # ---- Crepe Car is always a direct path ---- #
    if type(vehicle).__name__ == 'CrappyCrepeCar':
        return Itinerary([from_city, to_city])

    # ---- Build world graph if it doesn't already exist ---- #
    if not str(vehicle) in WorldGraphs.vehicle_to_graphs:
        g = build_world_graph(vehicle)
    else:
        g = WorldGraphs.vehicle_to_graphs[str(vehicle)]

    # ---- Compute the shortest path ---- #
    try:
        if not nx.has_path(g, from_city.city_id, to_city.city_id):
            return None
        else:
            path = [get_city_by_id(x) for x in nx.shortest_path(g, from_city.city_id, to_city.city_id, weight='weight')]
            return Itinerary(path)
    except nx.exception.NodeNotFound:  # singleton nodes will not load in from csv. There is no path to or from them.
        return None


if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    vehicles = create_example_vehicles()

    from_cities = set()
    for city_id in [1036533631, 1036142029, 1458988644]:
        from_cities.add(get_city_by_id(city_id))

    to_cities = set(from_cities)

    for from_city in from_cities:
        to_cities -= {from_city}
        for to_city in to_cities:
            print(f"{from_city} to {to_city}:")
            for test_vehicle in vehicles:
                shortest_path = find_shortest_path(test_vehicle, from_city, to_city)
                print(f"\t{test_vehicle.compute_itinerary_time(shortest_path)}"
                      f" hours with {test_vehicle} with path {shortest_path}.")
