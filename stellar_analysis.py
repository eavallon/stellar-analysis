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
import pandas as pd
import csv

path =  "kepler.txt"
def read_csv(path):

    """
<<<<<<< HEAD
    Read Kepler dataset in path that is in csv format to get out data
    return: store as list of dictionaries where each dictionary is a star and its properties
=======
    Read Kepler dataset in path that is in .csv format to get out data
    return: store in dictionary
>>>>>>> 1d47de848be7d6a079be0735afbcd221abec51d1
    """

    out_dictionary = []
    for row in csv.DictReader(open(path)):
        out_dictionary.append(row) # need to see data in to output stuffs

    # alternate way:
    # df = pd.DataFrame(path)
    # name = df['column_name']

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
# compare coordinates definition
# compare coordinates of range to type
#  compare coordinates to color magnitude plot

#
def main():
    
    
    
if __name__ == "__main__":
    main()
    
        