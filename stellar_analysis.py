"""
CSE 160 Final Project: Stellar Analysis
Authors: Ellis Avallone and Tessa Wilkinson

Research Questions:
1) Does gathering data from one section of the sky mean we get all the same type of star?
2) Does gathering data from one section of the sky mean we get stars of the same size?
3) Do two stars near each other in the sky mean they are located near each other in space?

"""
import numpy as np
import matplotlib.pyplot as plt
import csv


# Begin main program
def read_csv(path):
    """
    Reads in the Kepler data set and returns a dictionary

    Parameters:
        path: a filename

    Returns:
        A list of dictionaries in which the key is a string corresponding to a
        column name in the .csv file, and the values are the properties associated
        with that column.
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
        A dictionary in which the key is the idea number of each star, and the
        values are the parameters in the column_name.
    """
    array = read_csv(path)
    out_dictionary = {}
    for star_dictionary in array:
        for key, parameter in star_dictionary.items():
            kicnumber = star_dictionary['Kepler ID']
            if "RA (J2000)" != key != "Dec (J2000)":
                if len(parameter) > 0:
                    parameter = float(parameter)
            if key == column_name and parameter != np.nan:
                out_dictionary[kicnumber] = parameter

    return out_dictionary


def get_coordinates(ra, dec):
    """
    Given a coordinate, returns a dictionary mapping the stars's id to both its
    coordinate

    Parameters:
        ra: a dictionary mapping a stars id to its Right Ascension (similar to
        longitude)

        dec: a dictionary mapping a stars id to its Declination (similar to
        latitude)

    Returns:
        A dictionary in which the key is the star's id number and the value is an
        array of coordinates.
    """
    coords_dictionary = {}

    for k,v in ra.items():
        ra_coordlist = h_m_s_separator(v)
        for key, value in dec.items():
            dec_coordlist = h_m_s_separator(value)
            if k == key:
                coords_dictionary[k] = [ra_coordlist, dec_coordlist]

    return coords_dictionary


# Question 1

def color_magnitude_plot(magnitude, temperature):
    """
    Given two lists corresponding to the Kepler Magnitude and the Temperature,
    plots them and saves the plot as a .png file.
    
    Parameters:
        magnitude: a dictionary in which the keys are star id numbers and the
        values correspond to the Kepler magnitude of stars.
            
        temperature: a dictionary in which the keys are the star id numbers, and the
        values of values correspond to the E(B-V) of the star.
              
    Returns:
        None
    """
    for key_m, value_m in magnitude.items():
        for key_t, value_t in temperature.items():
            if key_m == key_t:
                try:
                    plt.scatter(value_t, value_m)
                except ValueError:
                    if len(value_t) > 0 < len(value_m):
                        plt.scatter(value_t, value_m)


    plt.gca().invert_yaxis()
    plt.xlabel('Temperature')
    plt.ylabel('Magnitude')
    plt.title('Color Magnitude Diagram')
    plt.show()
    #plt.savefig('color_magnitude', format = 'png')
    plt.clf()
    
    
def get_star_type(magnitude, temperature):
    """
    Given two dictionaries in which the keys are star id numbers, and the values
    are either the Kepler Magnitude or the Temperature, returns a dictionary of star
    types.
    
    Parameters:

        magnitude: a dictionary in which the keys are star id numbers and the
        values correspond to the Kepler magnitude of stars.

        temperature: a dictionary in which the keys are the star id numbers, and the
        values of values correspond to the E(B-V) of the star.

     Returns:
         A dictionary in which the keys are strings of types of stars, and the
         values are lists of star id numbers.
    """
    type_dict = {}
    main_sequence = []
    pre_main_sequence = []
    giants = []
    white_dwarfs = []

    for key_m, value_m in magnitude.items():
        for key_t, value_t in temperature.items():
            if key_m == key_t:
                if 13 < value_m and value_t > 0.17:
                    pre_main_sequence.append(int(key_m))
                elif 12 > value_m:
                    giants.append(int(key_m))
                elif 15 < value_m and value_t < 0.75:
                    white_dwarfs.append(int(key_m))
                else:
                    main_sequence.append(int(key_m))

    type_dict['Main Sequence'] = main_sequence
    type_dict['Pre-Main Sequence'] = pre_main_sequence
    type_dict['Giants'] =  giants
    type_dict['White Dwarfs'] = white_dwarfs

    print "  Number of Main Sequence Stars:", len(main_sequence)
    print "  Number of Pre Main Sequence Stars:", len(pre_main_sequence)
    print "  Number of Giant Stars:", len(giants)
    print "  Number of White Dwarf Stars:", len(white_dwarfs)

    return type_dict


# Question 2

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


# Question 3

def h_m_s_separator(coordinate):
    """
    Converts a coordinate of a star to a list of values.

    Parameters:
        coordinate: a string corresponding to a stars location in
        'hours, minutes, second' format

    Returns:
        A list of values corresponding to the hour, minute, and second.
    """
    hour = 0
    minute = 0
    sec = 0

    for index, value in enumerate(coordinate):
        # all kepler targets will be (+) declination so this can be omitted
        if value[0] == '+':
            value = value[1:]

        if index < 3 and value != ' ':
            if hour != 0:
                hour = str(hour) + str(value)
            else:
                hour = value
        elif 3 <= index <= 5 and value != ' ':
            if minute != 0:
                minute = str(minute) + str(value)
            else:
                minute = value
        elif index > 5 and value != ' ':
            if sec != 0:
                sec = str(sec) + str(value)
            else:
                sec = value

    try:
        return [int(hour), int(minute), float(sec)]
    except ValueError:
        return [0, 0, 0]


def check_if_coords_close(coord1, coord2, coord_range):
    """
    Checks if the first star/coordinate given is within range of the second
    star/coordinate.

    Parameters:
        coord1: a list that represents one coordinate of a star

        coord2: a list that represents a coordinate of another star

        coord_range: an integer value corresponding to a range around coord1

    Returns:
        A boolean Value
    """
    hour1 = coord1[0]
    min1 =  coord1[1]
    sec1 = coord1[2]

    hour2 = coord2[0]
    min2 = coord2[1]
    sec2 = coord2[2]

    if hour1 == hour2 and min1 == min2:
        diff = np.abs(sec1 - sec2)
        diff < coord_range


def find_surrounding_stars(kic, coord, ra, dec):
    """
    Given a star's id and it's coordinates, returns a list of stars that
    are close to the given star.

    Parameters:
        kic: an integer value representing the star's id number star

        coord: a list corresponding to the star's location

        ra: a dictionary mapping a stars id to its Right Ascension (similar to
            longitude).

        dec: a dictionary mapping a stars id to its Declination (similar to
            latitude).

    Returns: a list of star id numbers
    """

    close = []
    for k, c in get_coordinates(ra, dec).items():
        if check_if_coords_close(coord[0], c[0], 10) and check_if_coords_close(coord[1], c[1], 10)  and kic != k:
            close.append(int(k))

    return close


def percent_list_in_list(list1, list2):
    """
    Given two lists, returns the percentage of the values that are in both lists

    Parameters:

        list1 = A list of star id numbers

        list2 = A list of star id numbers

    Returns:
        The float representing the percentage of values in both lists
    """
    total = len(list2)

    if len(list1) > 0 < len(list2):
        set1 = set(list1)
        set2 = set(list2)
        out = list(set1 & set2)
        percentage =  float(len(out)) / float(total)
        return percentage


def near_stars_same_type_percentage(type_dict, ra, dec):
    """
    Given dictionary of star types, checks to see if stars that are near each
    other are of the same type

    Parameters:

        type_dict: dictionary in which the keys are strings corresponding to
                   the types of stars, and the values are lists of star id numbers.

        ra: a dictionary mapping a stars id to its Right Ascension (similar to
            longitude).

        dec: a dictionary mapping a stars id to its Declination (similar to
            latitude).

    Returns:
        A dictionary in which the keys are star id numbers, and the values are
        floats representing percentage of same type stars in the surrounding
        area.
        """
    out_percents_dict = {}

    for k,v in get_coordinates(ra, dec).items():
        near_stars_list = find_surrounding_stars(k, v, ra, dec)
        for startype, starlist in type_dict.items():
            if len(near_stars_list) > 0:
                out_percents_dict[k] = percent_list_in_list(near_stars_list, starlist)

    return out_percents_dict


def plot_near_stars_same_type_histogram(data, type_dict):
    """
    Given a dataset, plots the data as a histogram, and saves it as a .png
    file.

    Parameters:
        data: a dictionary in which they keys are star id numbers, and the values
              are percentages

        type_dict: dictionary in which the keys are strings corresponding to
                the types of stars, and the values are lists of star id numbers.

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
    plt.show()
    #plt.savefig('near_stars_type_histogram', format = 'png')


def main():
    path =  "kepler_test50.txt"
    #path = "kepler.txt"
    
    # call variables
    magnitude = get_column_data(path, "KEP Mag")
    temperature = get_column_data(path, "E(B-V)")
    ra = get_column_data(path, 'RA (J2000)')
    dec = get_column_data(path, 'Dec (J2000)')
    star_radii = get_column_data(path, "Radius")
    logg = get_column_data(path, 'Log G')


    # Question 1:
    print "Question 1:"
    print "  Number of Stars per Type:"
    color_magnitude_plot(magnitude, temperature)
    
    # Question 2
    print 'Question 2:'
    types = get_star_type(magnitude, temperature)
    histogram_stats(star_radii.values())
    histogram_stats(logg.values())

    # Question 3
    print "Question 3:"
    print "  Percentage of Stars in Close Proximity of the Same Type:"
    percentage = near_stars_same_type_percentage(types, ra, dec)
    #histogram_stats(percentage.values())
    #plot_near_stars_same_type_histogram(percentage, types)


if __name__ == "__main__":
    main()
    
