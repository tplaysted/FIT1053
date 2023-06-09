"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It allows plotting an Itinerary as the picture of a map.

@file map_plotting.py
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from itinerary import Itinerary
from city import City
import numpy as np


def plot_itinerary(itinerary: Itinerary, projection='robin', line_width=2, colour='b') -> None:
    """
    Plots an itinerary on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2_city3_..._cityX.png.

    :param itinerary: The itinerary to plot.
    :param projection: The map projection to use.
    :param line_width: The width of the line to draw.
    :param colour: The colour of the line to draw.
    """
    # TODO

    # create bounding box
    max_lat = max([city.coordinates[0] for city in itinerary.cities])
    max_lon = max([city.coordinates[1] for city in itinerary.cities])

    min_lat = min([city.coordinates[0] for city in itinerary.cities])
    min_lon = min([city.coordinates[1] for city in itinerary.cities])

    # lon_0 is central longitude of projection.
    # resolution = 'c' means use crude resolution coastlines.
    m = Basemap(projection=projection, resolution='c', lon_0=0, lat_0=0)
    m.drawcoastlines()
    m.fillcontinents(color='coral', lake_color='aqua')
    # draw parallels and meridians.
    m.drawparallels(np.arange(-90., 120., 30.))
    m.drawmeridians(np.arange(0., 360., 60.))
    m.drawmapboundary(fill_color='aqua')

    for i in range(len(itinerary.cities) - 1):
        lon1 = itinerary.cities[i].coordinates[1]
        lat1 = itinerary.cities[i].coordinates[0]
        lon2 = itinerary.cities[i+1].coordinates[1]
        lat2 = itinerary.cities[i+1].coordinates[0]
        m.drawgreatcircle(lon1, lat1, lon2, lat2, linewidth=2, color=colour)

    plt.title("Itinerary")
    plt.show()


if __name__ == "__main__":
    # create some cities
    city_list = list()

    city_list.append(City("Melbourne", (-37.8136, 144.9631), "primary", 4529500, 1036533631))
    city_list.append(City("Sydney", (-33.8688, 151.2093), "primary", 4840600, 1036074917))
    city_list.append(City("Brisbane", (-27.4698, 153.0251), "primary", 2314000, 1036192929))
    city_list.append(City("Perth", (-31.9505, 115.8605), "1992000", 2039200, 1036178956))

    # plot itinerary
    plot_itinerary(Itinerary(city_list))
