"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class Country.

@file country.py
"""
from tabulate import tabulate
from city import City, create_example_cities


class Country():
    """
    Represents a country.
    """

    name_to_countries = dict()  # a dict that associates country names to instances.

    def __init__(self, name: str, iso3: str) -> None:
        """
        Creates an instance with a country name and a country ISO code with 3 characters.

        :param name: The name of the country
        :param iso3: The unique 3-letter identifier of this country
        :return: None
        """

        self.name = name
        self.iso3 = iso3
        self.cities = []

        # TODO

        Country.name_to_countries[self.name] = self

    def add_city(self, city: City) -> None:
        """
        Adds a city to the country.

        :param city: The city to add to this country
        :return: None
        """
        # TODO

        self.cities.append(city)
        city.country = self.name

    def get_cities(self, city_type: list[str] = None) -> list[City]:
        """
        Returns a list of cities of this country.

        The argument city_type can be given to specify a subset of
        the city types that must be returned.
        Cities that do not correspond to these city types are not returned.
        If None is given, all cities are returned.

        :param city_type: None, or a list of strings, each of which describes the type of city.
        :return: a list of cities in this country that have the specified city types.
        """
        # TODO

        self.cities.sort(key=lambda x: x.population, reverse=True)

        if city_type is None:
            return self.cities
        else:
            list_cities = []

            for el in self.cities:
                if el.city_type in city_type:
                    list_cities.append(el)

            return list_cities

    def print_cities(self) -> None:
        """
        Prints a table of the cities in the country, from most populous at the top
        to least populous. Use the 'tabulate' module to print the table, with row headers:
        "Order", "Name", "Coordinates", "City type", "Population", "City ID".
        Order should start at 0 for the most populous city, and increase by 1 for each city.
        """
        # TODO

        self.cities.sort(key=lambda x: x.population, reverse=True)  # sort

        print("Cities of " + self.name)

        table = [["Order", "Name", "Coordinates", "City type", "Population", "City ID"]]

        for i, el in enumerate(self.cities):
            row = [str(i)] + el.get_table_data()
            table.append(row)

        print(tabulate(table))

    def __str__(self) -> str:
        """
        Returns the name of the country.
        """
        # TODO

        return self.name


def add_city_to_country(city: City, country_name: str, country_iso3: str) -> None:
    """
    Adds a City to a country.
    If the country does not exist, create it.

    :param city: city to add to country
    :param country_name: The name of the country
    :param country_iso3: The unique 3-letter identifier of this country
    :return: None
    """
    # TODO

    if country_name in Country.name_to_countries:
        Country.name_to_countries[country_name].add_city(city)
    else:
        new_country = Country(country_name, country_iso3)
        new_country.add_city(city)


def find_country_of_city(city: City) -> Country:
    """
    Returns the Country this city belongs to.
    We assume there is exactly one country containing this city.

    :param city: The city.
    :return: The country where the city is.
    """
    # TODO

    return Country.name_to_countries[city.country]


def create_example_countries() -> None:
    """
    Creates a few countries for testing purposes.
    Adds some cities to it.
    """
    create_example_cities()
    malaysia = Country("Malaysia", "MAS")
    kuala_lumpur = City.name_to_cities["Kuala Lumpur"][0]
    malaysia.add_city(kuala_lumpur)

    for city_name in ["Melbourne", "Canberra", "Sydney"]:
        add_city_to_country(City.name_to_cities[city_name][0], "Australia", "AUS")

    for city_name in ["Birmingham", "London"]:
        add_city_to_country(City.name_to_cities[city_name][0], "United Kingdom", "GBR")


def test_example_countries() -> None:
    """
    Assuming the correct countries have been created, runs a small test.
    """
    Country.name_to_countries["Australia"].print_cities()


if __name__ == "__main__":
    create_example_countries()
    test_example_countries()

    print("Sydney is in: " + find_country_of_city(City.name_to_cities["Sydney"][0]).name)
