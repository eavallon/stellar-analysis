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

# This path will change based on where the data-set is located!
path =  "kepler.txt"


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
    returns: a dictionary where they key is the kicnumber and the values are the parameters in the column
    """

    array = read_csv(path)
    out_dictionary = {}

    for star_dictionary in array:
        for key,parameter in star_dictionary.items():
            kicnumber = star_dictionary['Kepler ID']
            if key == column_name and len(parameter) > 0:
                out_dictionary[kicnumber] = parameter

    # as a check for now!
    for k,v in out_dictionary.items():
        print k,v

    return out_dictionary

get_column_data(path, 'Teff')


# call specific column definition, store [dictionaries]
# store into a list based on type definition

# question 1
# create color magnitude plot

# question 2
# compare radii of stars to see if they are similar sizes
# histogram definition
# histogram analysis

# question 3
# compare coordinates definition
# compare coordinates of range to type
#  compare coordinates to color magnitude plot

#
