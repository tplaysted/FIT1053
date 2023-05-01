"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It puts together all parts of the assignment.

@file onboard_navigation.py
"""
import networkx as nx
import csv
from csv_parsing import create_cities_countries_from_csv
import vehicles
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


if __name__ == '__main__':
    create_cities_countries_from_csv('worldcities_truncated.csv')

