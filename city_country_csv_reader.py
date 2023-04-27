"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a parser that reads a CSV file and creates instances
of the class City and the class Country.

@file city_country_csv_reader.py
"""
import csv
from city import City
from country import Country


def create_cities_countries_from_csv(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.

    :param path_to_csv: The path to the CSV file.
    """

    with open(path_to_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)

        attribute_names = ['city_ascii', 'lat', 'lng', 'capital', 'population', 'id', 'country', 'iso3']
        attribute_to_column = []

        for i, row in enumerate(reader):
            if i == 0:


if __name__ == "__main__":

    create_cities_countries_from_csv('worldcities_truncated_aus.csv')
    # create_cities_countries_from_csv("worldcities_truncated.csv")
    # for country in Country.name_to_countries.values():
    #     country.print_cities()
