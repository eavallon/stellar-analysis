"""
CSE 160 Final Project: Stellar Analysis
Authors: Ellis Avallone and Tessa Wilkinson

Research Questions:
1) Does gathering data from one section of the sky mean we get all the same type of star?
2) What types of stars (of similar size) in this dataset have the most planets?
3) Do two stars near each other in the sky mean they are located near each other in space?

"""
import numpy as np
import matplotlib.pyplot
import math
import csv
from astropy.coordinates import SkyCoord
import astropy.units as u


# This path will change based on where the data-set is located!
path =  "kepler_test50.txt"


def read_csv(path):
    """
    Read Kepler data set in csv format in path to get out data
    return: store as list of dictionaries where each dictionary is a star and its properties
    """

    out_dictionary = []
    for row in csv.DictReader(open(path)):
        out_dictionary.append(row)

    return out_dictionary


def get_column_data(path, column_name):
    """
    Given a specific column name: return every star in database with parameters in specified column
    returns: a dictionary: the key is the kicnumber of each star and the values are the parameters in the column_name
    """

    array = read_csv(path)
    out_dictionary = {}

    for star_dictionary in array:
        for key,parameter in star_dictionary.items():
            kicnumber = star_dictionary['Kepler ID']
            if key == column_name and len(parameter) > 0:
                out_dictionary[kicnumber] = parameter

    # as a check!
    # for k,v in out_dictionary.items():
    #     print k,v

    return out_dictionary


#get_column_data(path, 'Teff')

# store into a list based on type definition

# question 1
# create color magnitude plot
""" grab 'E(B-V)' column (I think, otherwise B color and subtract V color) and 'KEP Mag' column
color magnitude diagram: the x axis in this diagram is made from subtracting the colors (or temperatures) obtained by
imaging stars with different filters (or color ranges). The blue-color range filter - the visual-color range filter (B-V)
gives a color index in terms of the visual wavelengths that we can observe. This value ranges from 0 to 2 depending on
how red the star is. The y axis is in terms of absolute magnitude (or how bright the star truely is, not just how bright
we see it as), and is inverted on this graph so that as you go to great y values, the absolute magnitude gets smaller in
number. This is because absolute magnitude is one of those historically backwards in scale. (darn conventions!)
The final plot will have hotter, bluer stars towards the top left, and cooler, older stars on the bottom right. A line
connecting these will indicate the 'main sequence' of stars, or the stars that are burning hydrogen as part of the main
life cycle. This is how we will tell which stars are which.
"""

# question 2
# compare radii of stars to see if they are similar sizes
""" grab 'Radius' column
"""
# histogram definition
# histogram analysis

# question 3

def h_m_s_separator(coordinate):
    """input: string of from ra or dec coordinates '## ## ##.###'
    output: list of hour, min, sec values [##, ##, ##.##]
    """
    hour = 0
    min = 0
    sec = 0
    print 'in hms_sep, coord:', coordinate

    for index, value in enumerate(coordinate):
        # all kepler targets will be (+) so this can be omitted
        if value[0] == '+':
            value = value[1:]

        if index < 3 and value != ' ':
            if hour != 0:
                hour = str(hour) + str(value)
            else:
                hour = value
        elif 3 <= index <= 5 and value != ' ':
            if min != 0:
                min = str(min) + str(value)
            else:
                min = value
        elif index > 5 and value != ' ':
            if sec != 0:
                sec = str(sec) + str(value)
            else:
                sec = value

    try:
        return (int(hour), int(min), float(sec))
    except ValueError:
        return (0, 0, 0)


def get_coordinates():
    """
    calls the coordinages
    """

    ra = get_column_data(path, 'RA (J2000)')
    dec = get_column_data(path, 'Dec (J2000)')

    coords = {}
    for k,v in ra.items():
        ra_coordlist = h_m_s_separator(v)
        for key, value in dec.items():
            dec_coordlist = h_m_s_separator(value)
            if k == key:
                coords[k] = [ra_coordlist, dec_coordlist]

    for ke, ve in coords.items():
        print 'out get_coord', ke,ve



get_coordinates()


# compare coordinates definition
# compare coordinates of range to type
#  compare coordinates to color magnitude plot

#
