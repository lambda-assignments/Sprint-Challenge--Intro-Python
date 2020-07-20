"""Create a class to hold a city location. Call the class "City". It should have
fields for name, lat and lon (representing latitude and longitude).


We have a collection of US cities with population over 750,000 stored in the
file "cities.csv". (CSV stands for "comma-separated values".)

In the body of the `cityreader` function, use Python's built-in "csv" module
to read this file so that each record is imported into a City instance. Then
return the list with all the City instances from the function.
Google "python 3 csv" for references and use your Google-fu for other examples.

Store the instances in the "cities" list, below.

Note that the first line of the CSV is header that describes the fields--this
should not be loaded into a City object."""
import os

__location__ = str(os.path.abspath(os.getcwd()))

class City:
    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lon = lng

class CityData:

    def __init__(self, attrs, data):
        for i in range(0, len(attrs)):
            val = float(data[i]) if attrs[i] in ['lat', 'lng'] else data[i]
            self.__setattr__(attrs[i], val)



class CityReader:
    """
    """
    _cols = 0
    rows = 0
    stream = {}

    def __init__(self, filepath_or_buffer: str, delimiter=',') -> None:
        with open(filepath_or_buffer) as f:
            import csv
            idx = 0
            data = csv.reader(f, delimiter=delimiter)
            for row in data:
                if self._cols == 0:
                    self._cols = len(row)
                    self.column_names = row
                    self.stream = {h:[] for h in row}
                    continue
                for i, n in enumerate(self.column_names):
                    self.stream[n].append(row[i])
                idx += 1
        self.rows = idx

    def row(self, idx_loc):
        return [self.stream[k][idx_loc] for k in self.stream.keys()]

    def build_city(self, row):
        return CityData(self.column_names, self.row(row))

    @property
    def shape(self):
        return self._cols, self.rows


def cityreader():

    city_data = CityReader(__location__ + '/cityreader/cities.csv')
    cities = [
        city_data.build_city(cnt) for cnt in range(city_data.rows)
    ]
    return cities

print(cityreader()[0].city)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []

  # Go through each city and check to see if it falls within
  # the specified coordinates.

  return within
