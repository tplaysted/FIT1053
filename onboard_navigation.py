"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It puts together all parts of the assignment.

@file onboard_navigation.py
"""
import networkx as nx
import csv

from csv_parsing import create_cities_countries_from_csv
from vehicles import create_example_vehicles, Vehicle
from city import City
from map_plotting import plot_itinerary
import path_finding


def validate_input(prompt: str, inputs: list[str]) -> str:
    """
    Gets a validated input from the user as in A1

    :param prompt:
    :param inputs:
    :return:
    """
    while True:
        choice = input(prompt)

        if choice in inputs:
            return choice
        else:
            print('Whoops! \'' + str(choice) + '\' was not a valid choice.')


def export_graph_to_csv(g: nx.Graph(), filename: str) -> None:
    """
    Assumes that the edges of g are of the form [(int, int), float] and writes one edge to a row in a csv file.

    :param g: networkx graph object
    :param filename: string representing the filename excluding '.csv'
    :return: None
    """

    with open(filename + '.csv', 'w', newline='') as csvfile:
        graphwriter = csv.writer(csvfile)

        for edge in list(g.edges):
            graphwriter.writerow([edge[0], edge[1], g.edges[edge[0], edge[1]]['weight']])


def import_graph_from_csv(filename: str) -> nx.Graph():
    """
    Imports the graph stored in filename (INCLUDING '.csv'). Assumes rows take the form x,y,float
    and maps these to edges [(int(x), int(y)), 'weight'=float]

    :param filename: filename including extension i.e. 'test_graph.csv'
    :return: reference to the new graph object
    """
    g = nx.Graph()

    with open(filename, 'r', newline='') as csvfile:
        graphreader = csv.reader(csvfile)

        for row in graphreader:
            g.add_edge(int(row[0]), int(row[1]), weight=float(row[2]))

    return g


def get_user_vehicle_choice(v: list[Vehicle]) -> Vehicle:
    """
    Get a valid choice of vehicle from the user given a list of vehicles

    :param v:
    :return:
    """
    choices = [str(i + 1) for i in range(len(v))]

    for i in range(len(v)):
        print(str(i + 1) + ": " + str(v[i]))

    user_choice = v[int(validate_input("Input your choice: ", choices)) - 1]
    print("Selected " + str(user_choice))
    return user_choice


def get_user_city_name(prompt: str) -> City:
    """
    Get the name of an existing city from the user. Convert all input strings to title case.

    :param prompt:
    :return:
    """
    while True:
        name = input(prompt).title()

        if name in City.name_to_cities:
            c = City.name_to_cities[name][0]
            print("Selected " + str(c))
            return c
        else:
            print("Couldn't find '" + name + "' in the database. ")
            prompt = "Please try again: "


if __name__ == '__main__':
    # ---- Set up by loading in vehicles, cities and graph data ---- #
    print("Hold on a tic, loading the world data...")

    create_cities_countries_from_csv('worldcities_truncated.csv')
    v = create_example_vehicles()

    v_names = ['ddd_100_500.csv', 'ttt_3_2000.csv']

    for i in range(1, 3):
        path_finding.WorldGraphs.vehicle_to_graphs[str(v[i])] = import_graph_from_csv(v_names[i - 1])

    # ---- Get the user's vehicle choice ---- #
    print("Ok, done! What vehicle would you like to use?")

    user_v = get_user_vehicle_choice(v)

    # ---- Get the user's choice of city ---- #
    c1 = get_user_city_name("Please input a starting city: ")
    c2 = get_user_city_name("Please input a destination city: ")

    # ---- Do path finding ---- #
    itinerary = path_finding.find_shortest_path(user_v, c1, c2)

    if itinerary is None:
        print("Unfortunately, there is no path from " + c1.name + " to " + c2.name +
              " with the " + str(user_v))
    else:
        print(itinerary)
        print("This journey will take " + str(user_v.compute_itinerary_time(itinerary)) +
              "h using " + str(user_v))
        plot_itinerary(itinerary)
