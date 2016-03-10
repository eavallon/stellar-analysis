"""
CSE 160 Final Project: Stellar Analysis
Authors: Ellis Avallone and Tessa Wilkinson

Research Questions:
1) Does gathering data from one section of the sky mean we get all the same type of star?
2) What types of stars (of similar size) in this dataset have the most planets?
3) Do two stars near each other in the sky mean they are located near each other in space?

"""
import numpy as np
import matplotlib.pyplot as plt
import math
import csv
from astropy.coordinates import SkyCoord
import astropy.units as u

# This path will change based on where the data-set is located!
path =  "kepler_test50.txt"

import pandas as pd
# dataframe = pd.DataFrame.from_csv(path, sep = ',')
# teff = dataframe['Teff']

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
        for key, parameter in star_dictionary.items():
            kicnumber = star_dictionary['Kepler ID']
            if 'RA (J2000)' !=  key != 'Dec (J2000)':
                parameter = float(parameter)
            if key == column_name and parameter != np.nan:
                out_dictionary[kicnumber] = parameter

    return out_dictionary

def dict_to_list(column_dict):
    '''
    A way to convert dicitonarys to lists

    input: column_dictionary
    output: list
    '''
    for key, values in column_dict.items():
        return [key, values]

def get_another_kic_value(kic, column_dict):
    """
    We use a lot of dictionaries! So, this is a way to iterate through a dictionary looking for values

    input: kic = kicnumber
           column_dict = dictionary
    output: float value
    """

    for k,value in column_dict.items():
        if k == kic:
            if 0 != value != np.nan:
                return value



def get_coordinates():
    """
    runs through the data file to get the coordinates for each star
    output: a dictionary with key = kicnumber and value = array of ra and dec coordinates
    """

    ra = get_column_data(path, 'RA (J2000)')
    dec = get_column_data(path, 'Dec (J2000)')

    coords_dictionary = {}

    for k,v in ra.items():
        ra_coordlist = h_m_s_separator(v)
        for key, value in dec.items():
            dec_coordlist = h_m_s_separator(value)
            if k == key:
                coords_dictionary[k] = [ra_coordlist, dec_coordlist]

    return coords_dictionary

""" grab 'E(B-V)' column (I think, otherwise B color and subtract V color) and 'KEP Mag' column
color magnitude diagram: the x axis in this diagram is made from subtracting the colors (or temperatures) obtained by
imaging stars with different filters (or color ranges). The blue-color range filter - the visual-color range filter (B-V)
gives a color index in terms of the visual wavelengths that we can observe. This value ranges from 0 to 2 depending on
how red the star is. The y axis is in terms of absolute magnitude (or how bright the star truly is, not just how bright
we see it as), and is inverted on this graph so that as you go to great y values, the absolute magnitude gets smaller in
number. This is because absolute magnitude is one of those historically backwards in scale. (darn conventions!)
The final plot will have hotter, bluer stars towards the top left, and cooler, older stars on the bottom right. A line
connecting these will indicate the 'main sequence' of stars, or the stars that are burning hydrogen as part of the main
life cycle. This is how we will tell which stars are which.
"""
def color_magnitude_plot(magnitude, temperature):
    """
    Given two lists Kepler Magnitude and the Temperature and saves it as a .png file.
    
    Parameters:
        data: a dataframe consisting of the Kepler Magnitude and Temperature of 
              various stars.
              
    Returns:
        None
    """
    


# question 2
# compare radii of stars to see if they are similar sizes
""" grab 'Radius' column
"""

# histogram definition
# histogram analysis

def plot_planet_histogram(planet_data):
    """
    Given a dataframe, plots the data as a histogram, and saves it as a .png 
    file. 
    
    Parameters:
        data: a dataframe in which each element corresponds to the number of 
              planets around a star.
    
    Returns:
        None
    """
    n, bins, patches = plt.hist(planet_data, 50)
    
    plt.xlabel('Number of Planets')
    plt.ylabel('Frequency')
    plt.title('Histogram of Planets')
    plt.text()
    plt.grid(True)
    plt.show()
    plt.savefig('planet-histogram', format = 'png')
    

def histogram_stats(data):
    """
    Given a dataframe, computes various statistics that will be used to analyze 
    properties of that dataframe alongside the histogram plot.
    
    Parameters:
        data: a dataframe
    
    Returns:
        The sample size, mean, and standard deviation of the dataframe.
    """
    sample_size = len(data)
    mean = mean(data)
    standard_dev = np.std(data)
    print 'Summary Statistics:'
    print ' Sample Size:', sample_size
    print ' Sample Mean:', mean
    print 'Sample Standard Deviation:', standard_dev


# question 3

def h_m_s_separator(coordinate):
    """
    Given the coordiates of a star as a string '## ## ##.###' covert to a list of values
    output: list of hour, min, sec values [##, ##, ##.##]
    """
    hour = 0
    min = 0
    sec = 0
    #print 'in hms_sep, coord:', coordinate

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
        return [int(hour), int(min), float(sec)]
    except ValueError:
        return [0, 0, 0]




def check_if_coords_close(coord3d, other_coord3d, range):
    """
    """
    hour1 = coord3d[0]
    min1 = coord3d[1]
    sec1 = coord3d[2]

    hour2 = other_coord3d[0]
    min2 = other_coord3d[1]
    sec2 = other_coord3d[2]

    if hour1 == hour2 and min1 == min2:
        diff = np.abs(sec1 - sec2)
        if diff < range:
            return True
        else:
            return False


def find_surrounding_stars(kic, coord):
    '''
    Returns a list of stars that are close to the star presented

    input: kic star, coordinate of the kic star
    output: list
    '''

    # get_column_data()

    ra_close = []
    dec_close = []

    for k, c in get_coordinates().items():
        if check_if_coords_close(coord[0], c[0], 3) and kic != k:
            ra_close.append(k)
        if check_if_coords_close(coord[1], c[1], 3) and kic != k:
            dec_close.append(k)


    print ra_close
    print dec_close

for k,v in get_coordinates().items():
    print find_surrounding_stars(k, v)
# compare coordinates definition
# compare coordinates of range to type
#  compare coordinates to color magnitude plot



# of coordinates by pulling in ra and dec columns from dataset
# compare the coordinates (similar to blur homework)
# what stars lie within a certain range of each other
# compare types of stars within that range
# check if in the same list for type
# compare positions on the stellar magnitude diagram (first plot)
#



#
# def main():
#
#
#
# if __name__ == "__main__":
#     main()
#

