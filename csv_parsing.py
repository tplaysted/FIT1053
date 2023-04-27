"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a parser that reads a CSV file and creates instances
of the class City and the class Country.

@file csv_parsing.py
"""
import csv
from city import City
from country import Country, add_city_to_country


def create_cities_countries_from_csv(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.

    :param path_to_csv: The path to the CSV file.
    """

    with open(path_to_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        attribute_names = ["city_ascii", "lat", "lng", "country", "iso3", "capital", "population", "id"]
        attribute_to_column = dict()

        header = next(reader)

        for attribute in attribute_names:
            attribute_to_column[attribute] = header.index(attribute)

        for i, row in enumerate(reader):
            name = row[attribute_to_column['city_ascii']]
            coordinates = (float(row[attribute_to_column['lat']]), float(row[attribute_to_column['lng']]))
            city_type = row[attribute_to_column['capital']]

            population = row[attribute_to_column['population']]
            if population == '':
                population = 0
            else:
                population = int(population)

            city_id = int(row[attribute_to_column['id']])

            country_name = row[attribute_to_column['country']]
            country_iso3 = row[attribute_to_column['iso3']]

            new_city = City(name, coordinates, city_type, population, city_id)
            add_city_to_country(new_city, country_name, country_iso3)


if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    for country in Country.name_to_countries.values():
        country.print_cities()
