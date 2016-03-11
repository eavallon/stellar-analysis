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
import pandas as pd

<<<<<<< HEAD
path =  "kepler_test50.txt"

# This path will change based on where the data-set is located!
#path =  "kepler.txt"
=======
# This path will change based on where the data-set is located!
path =  "kepler_test50.txt"

import pandas as pd
# dataframe = pd.DataFrame.from_csv(path, sep = ',')
# teff = dataframe['Teff']
>>>>>>> f782fa2a16f06b7d014d543a10d5cf97f6c29d63

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
    Given a filename and a specific column name, returns every star in the 
    database with parameters in the specified column.
    
    Parameters:
        path: a filename corresponding to a csv file.
        
        column_name: a string corresponding to the column we wish to pull data 
                     from.
    
    Returns: 
        A dictionary in which the key is the kicnumber of each star and the 
        values are the parameters in the column_name.
    """

    array = read_csv(path)
    out_dictionary = {}
    for star_dictionary in array:
        for key, parameter in star_dictionary.items():
            kicnumber = star_dictionary['Kepler ID']
<<<<<<< HEAD
            if "RA (J2000)" != key != "Dec (J2000)":
=======
            if 'RA (J2000)' !=  key != 'Dec (J2000)':
>>>>>>> f782fa2a16f06b7d014d543a10d5cf97f6c29d63
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

<<<<<<< HEAD
# question 1
# create color magnitude plot
=======
>>>>>>> f782fa2a16f06b7d014d543a10d5cf97f6c29d63
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
<<<<<<< HEAD

=======
>>>>>>> f782fa2a16f06b7d014d543a10d5cf97f6c29d63
def color_magnitude_plot(magnitude, temperature):
    """
    Given two lists corresponding to the Kepler Magnitude and the Temperature,
    plots them and saves the plot as a .png file.
    
    Parameters:
        magnitude: a list of values corresponding to the Kepler magnitude of stars.
            
        temperature: a list of values corresponding to the color indicies of stars.
              
    Returns:
        None
    """
    
    #make parameters the dictionaries
    #iterate through parameters, and make sure keys are the same
    
    magnitude.reverse()
    print len(magnitude)
    print len(temperature)
    plt.scatter(temperature, magnitude)
    plt.xlabel('Temperature')
    plt.ylabel('Magnitude')
    plt.title('Color Magnitude Diagram')
    plt.show()
    #plt.savefig('color_magnitude', format = 'png')
    plt.clf()
    
    
def get_star_type(magnitude, temperature):
    """
    Given two lists corresponding to the Kepler Magnitude and the Temperature, 
    and coordinate restrictions corresponding to the desired type of star, 
    returns a dictionary that includes only those stars.
    
    Parameters:
        magnitude: a list of values corresponding to the Kepler magnitude of stars.
            
        temperature: a list of values corresponding to the color indicies of stars.
        
     Returns:
         Four lists of kicnumbers corresponding to stars of type main sequence, 
         pre-main sequence, giant, and white dwarf. Also prints the amount of
         each type of star in our dataset.
    """
    main_sequence = []
    pre_main_sequence = []
    giants = []
    white_dwarfs = []
    
    print "Number of Main Sequence Stars:", len(main_sequence)
    print "Number of Pre Main Sequence Stars:", len(pre_main_sequence)
    print "Number of Giant Stars:", len(giants)
    print "Number of While Dwarf Stars:", len(white_dwarfs)


# question 2
# compare radii of stars to see if they are similar sizes
<<<<<<< HEAD
=======
""" grab 'Radius' column
"""

>>>>>>> f782fa2a16f06b7d014d543a10d5cf97f6c29d63
# histogram definition
# histogram analysis

def plot_histogram(data, x_label, data_title):
    """
    Given a dataset, plots the data as a histogram, and saves it as a .png 
    file. 
    
    Parameters:
        data: a dataset corresponding to a property of a star.
        
        x_label: a string corresponding to the label on the histogram's x-axis.
        
        data_title: a string corresponding to the title of the histogram and the 
                    name the histogram will be saved as.
    
    Returns:
        None
    """
    n, bins, patches = plt.hist(data, 50, normed=1)
    
    plt.xlabel(x_label)
    plt.ylabel('Frequency')
    plt.title(data_title)
    plt.text()
    plt.grid(True)
    #plt.show()
    #plt.savefig(data_title, format = 'png')
    

def histogram_stats(data):
    """
    Given a dataset, computes various statistics that will be used to analyze 
    properties of the dataset alongside its histogram plot.
    
    Parameters:
        data: a dataset
    
    Returns:
        The sample size, mean, and standard deviation of the dataset.
    """
    sample_size = len(data)
    mean = np.mean(data)
    standard_dev = np.std(data)
    
    print 'Summary Statistics:'
    print ' Sample Size:', sample_size
    print ' Sample Mean:', mean
    print ' Sample Standard Deviation:', standard_dev

    return standard_dev


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
<<<<<<< HEAD
    calls the coordinates
=======
    Checks if one star/coordinate is within some range of some other star/coordinate
>>>>>>> f782fa2a16f06b7d014d543a10d5cf97f6c29d63
    """

    # TODO: refactor this!
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

    close = []
    for k, c in get_coordinates().items():
        if check_if_coords_close(coord[0], c[0], 10) and check_if_coords_close(coord[1], c[1], 10)  and kic != k:
            close.append(int(k))

    return close

def percent_list_in_list(list1, list2):
    """
    list1 = list of kic numbers
    list2 = list of kic numbers
    output: the percentage of numbers in list1 that are also in list2
    """

    match_sum = 0
    total = len(list2)
    if len(list1) > 0 < len(list2):

        for kic in list1:
            for k in list2:
                if kic == k:
                    match_sum += 1

        percentage =  float(match_sum) / float(total)

        return percentage

def near_stars_same_type_percentage(type_dict):
    """
    Checks to see if stars that are near each other are of the same type
    input: type_list - list of kic numbers for each type of star
    output: dictionary where the keys are kic numbers and the values are percentages saying how many
            stars near it of the same type
    """

    out_percents_dict = {}
    for k,v in get_coordinates().items():
        near_stars_list = find_surrounding_stars(k, v)

<<<<<<< HEAD
#get_coordinates()
=======
        for startype, starlist in type_dict.items():
            if len(near_stars_list) > 0:
                out_percents_dict[k] = percent_list_in_list(near_stars_list, starlist)
>>>>>>> f782fa2a16f06b7d014d543a10d5cf97f6c29d63

    print out_percents_dict
    return out_percents_dict


def plot_near_stars_same_type_histogram(data, type_dict):
    """
    Given a dataframe, plots the data as a histogram, and saves it as a .png
    file.

    Parameters:
        data: a dataframe in which each element corresponds to the number of
              planets around a star.

    Returns:
        None
    """
    a = []
    for n, (t,kics) in enumerate(type_dict.items()):
        for k,p in data.items():
            if int(k) in kics:
                plt.scatter(n, p, marker = '*', linestyle = '-')
                a.append(t)


    plt.xticks(np.arange(len(a)), a)
    plt.xlabel('Type of Stars')
    plt.ylabel('Percentage ')
    plt.title('Histogram: Near Stars of the Same Type')
    # plt.text()
    # plt.grid(True)
    plt.show()
    plt.savefig('near_stars_type_histogram', format = 'png')


def classify_by_type(graph_content):
    """
    to get types

    out: dictionary key= types and values = list of kic numbers of stars of that type
    """
    type_dict = {}
    if 0 > graph_content > .60:
        store['main_sequence'] = []
    elif graph_content < .40:
        print 'young star'
    else:
        print 'old star'

    type_dict = {'main_sequence':[1026132, 893676, 893004, 893946], 'young stars': [757137, 893944, 1026146, 757450, 892911, 892977]}
    return type_dict

# for now!
graph_content = 1


# of coordinates by pulling in ra and dec columns from dataset
# compare the coordinates by range
# what stars lie within a certain range of each other

types = classify_by_type(graph_content)
same_type_percentage_by_location = near_stars_same_type_percentage(types)
# compare types of stars within that range
#statistics of how many of the surrounding stars are the same type as one of these
histogram_stats(same_type_percentage_by_location.values())

# check if in the same list for type
# compare positions on the stellar magnitude diagram (first plot)

plot_near_stars_same_type_histogram(same_type_percentage_by_location, types )


<<<<<<< HEAD

def main():
    path =  "kepler_test50.txt"
    #path = "kepler.txt"
    
    # Question 1:
    # column name "KEP Mag" isn't in main data file, but is in test file
    magnitude = get_column_data(path, "KEP Mag").values()
    temperature = get_column_data(path, "E(B-V)").values()
    
    color_magnitude_plot(magnitude, temperature)
    
    # Question 2
    star_radii = get_column_data(path, "Radius")
    histogram_stats(star_radii.values())
    
    
if __name__ == "__main__":
    main()
    
        
=======
#
# def main():
#
#
#
#     if __name__ == "__main__":
#         main()


>>>>>>> f782fa2a16f06b7d014d543a10d5cf97f6c29d63
