"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the abstract class Vehicle and other classes that
inherit from it.

@file vehicles.py
"""
import math
from abc import ABC, abstractmethod
from city import City, get_city_by_id
from country import find_country_of_city, create_example_countries
from itinerary import Itinerary


class Vehicle(ABC):
    """
    A Vehicle defined by a mode of transportation, which results in a specific duration.
    """

    @abstractmethod
    def compute_travel_time(self, departure: City, arrival: City) -> float:
        """
        Returns the travel duration of a direct trip from one city
        to another, in hours, rounded up to an integer.
        Returns math.inf if the travel is not possible.

        :param departure: the departure city.
        :param arrival: the arrival city.
        :return: the travel time in hours, rounded up to an integer,
                 or math.inf if the travel is not possible.
        """

    def compute_itinerary_time(self, itinerary: Itinerary) -> float:
        """
        Returns a travel duration for the entire itinerary for a given vehicle.
        Returns math.inf if any leg (i.e. part) of the trip is not possible.

        :param itinerary: The itinerary.
        :return: the travel time in hours (an integer),
                 or math.inf if the travel is not possible.
        """
        # TODO
        total_time = 0

        for i in range(len(itinerary.cities) - 1):
            leg_time = self.compute_travel_time(itinerary.cities[i], itinerary.cities[i+1])

            if leg_time == math.inf:
                return math.inf

            total_time += leg_time

        return total_time

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns the class name and the parameters of the vehicle in parentheses.

        :return: the string representation of the vehicle.
        """


class CrappyCrepeCar(Vehicle):
    """
    A type of vehicle that:
        - Can go from any city to any other at a given speed.
    """

    def __init__(self, speed: int) -> None:
        """
        Creates a CrappyCrepeCar with a given speed in km/h.

        :param speed: the speed in km/h.
        """
        # TODO

        self.speed = speed

    def compute_travel_time(self, departure: City, arrival: City) -> float:
        """
        Returns the travel duration of a direct trip from one city
        to another, in hours, rounded up to an integer.

        :param departure: the departure city.
        :param arrival: the arrival city.
        :return: the travel time in hours, rounded up to an integer,
                 or math.inf if the travel is not possible.
        """
        # TODO

        distance = departure.distance(arrival)
        return math.ceil(distance / self.speed)

    def __str__(self) -> str:
        """
        Returns the class name and the parameters of the vehicle in parentheses.
        For example "CrappyCrepeCar (100 km/h)"

        :return: the string representation of the vehicle.
        """
        # TODO

        return "CrappyCrepeCar (" + str(self.speed) + " km/h)"


class DiplomacyDonutDinghy(Vehicle):
    """
    A type of vehicle that:
        - Can travel between any two cities in the same country.
        - Can travel between two cities in different countries only if they are both "primary".
        - Has different speed for the two cases.
    """

    def __init__(self, in_country_speed: int, between_primary_speed: int) -> None:
        """
        Creates a DiplomacyDonutDinghy with two given speeds in km/h:
            - one speed for two cities in the same country.
            - one speed between two primary cities.

        :param in_country_speed: the speed within one country.
        :param between_primary_speed: the speed between two primary cities.
        """
        # TODO

        self.in_country_speed = in_country_speed
        self.between_primary_speed = between_primary_speed

    def compute_travel_time(self, departure: City, arrival: City) -> float:
        """
        Returns the travel duration of a direct trip from one city
        to another, in hours, rounded up to an integer.
        Returns math.inf if the travel is not possible.

        :param departure: the departure city.
        :param arrival: the arrival city.
        :return: the travel time in hours, rounded up to an integer,
                 or math.inf if the travel is not possible.
        """
        # TODO

        distance = departure.distance(arrival)

        if departure.city_type == 'primary' and arrival.city_type == 'primary':
            return math.ceil(distance / self.between_primary_speed)

        if departure.country == arrival.country:
            return math.ceil(distance / self.in_country_speed)

        return math.inf

    def __str__(self) -> str:
        """
        Returns the class name and the parameters of the vehicle in parentheses.
        For example "DiplomacyDonutDinghy (100 km/h | 200 km/h)"

        :return: the string representation of the vehicle.
        """
        # TODO

        return "DiplomacyDonutDinghy (" + str(self.in_country_speed) + " km/h | " + str(
            self.between_primary_speed) + " km/h)"


class TeleportingTarteTrolley(Vehicle):
    """
    A type of vehicle that:
        - Can travel between any two cities if the distance is less than a given maximum distance.
        - Travels in fixed time between two cities within the maximum distance.
    """

    def __init__(self, travel_time: int, max_distance: int) -> None:
        """
        Creates a TeleportingTarteTrolley with a distance limit in km.

        :param travel_time: the time it takes to travel.
        :param max_distance: the maximum distance it can travel.u
        """
        # TODO

        self.travel_time = travel_time
        self.max_distance = max_distance

    def compute_travel_time(self, departure: City, arrival: City) -> float:
        """
        Returns the travel duration of a direct trip from one city
        to another, in hours, rounded up to an integer.
        Returns math.inf if the travel is not possible.

        :param departure: the departure city.
        :param arrival: the arrival city.
        :return: the travel time in hours, rounded up to an integer,
                 or math.inf if the travel is not possible.
        """
        # TODO

        distance = departure.distance(arrival)

        if distance <= self.max_distance:
            return self.travel_time
        else:
            return math.inf

    def __str__(self) -> str:
        """
        Returns the class name and the parameters of the vehicle in parentheses.
        For example "TeleportingTarteTrolley (5 h | 1000 km)"

        :return: the string representation of the vehicle.
        """
        # TODO

        return "TeleportingTarteTrolley (" + str(self.travel_time) + " h | " + str(
            self.max_distance) + " km)"


def create_example_vehicles() -> list[Vehicle]:
    """
    Creates 3 examples of vehicles.

    :return: a list of 3 vehicles.
    """
    return [CrappyCrepeCar(200), DiplomacyDonutDinghy(100, 500), TeleportingTarteTrolley(3, 2000)]


if __name__ == "__main__":
    # we create some example cities
    # we create some example cities
    # create_example_countries()
    #
    # from_cities = set()
    # for city_id in [1036533631, 1036142029, 1458988644]:
    #     from_cities.add(get_city_by_id(city_id))
    #
    # # we create some vehicles
    # vehicles = create_example_vehicles()
    #
    # to_cities = set(from_cities)
    # for from_city in from_cities:
    #     to_cities -= {from_city}
    #     for to_city in to_cities:
    #         print(f"{from_city} to {to_city}:")
    #         for vehicle in vehicles:
    #             print(f"\t{vehicle.compute_travel_time(from_city, to_city)} hours with {vehicle}.")

    create_example_countries()

    city_list = []
    city_list.append(get_city_by_id(1036533631))
    city_list.append(get_city_by_id(1036142029))
    city_list.append(get_city_by_id(4))
    city_list.append(get_city_by_id(5))

    itinerary = Itinerary(city_list)
    dinghy = DiplomacyDonutDinghy(50, 200)
    print(dinghy.compute_itinerary_time(itinerary))

    print(type(dinghy).__name__)
