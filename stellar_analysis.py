"""
CSE 160 Final Project: Stellar Analysis
Authors: Ellis Avallone and Tessa Wilkinson

Research Questions:
1) Does gathering data from one section of the sky mean we get all the same type of star?
2) Are stars of the same type typically the same size?
3) What type of stars are most likely to be near a star in our sky?
"""
import numpy as np
import matplotlib.pyplot as plt
import csv

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
    path_data = csv.DictReader(open(path))
    
    # Creates a dictionary from filename
    for row in path_data:
        out_dictionary.append(row)
    path_data.close()
    return out_dictionary


def get_column_data(data, column_name):
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

    out_dictionary = {}
    
    # Iterating through each dictionary corresponding to 1 row in the file
    for star_dictionary in data:
        for key, parameter in star_dictionary.items():
            star_id = star_dictionary['Kepler ID']
            # Excludes rows whose values aren't floats
            if "RA (J2000)" != key != "Dec (J2000)":
                if len(parameter) > 0:
                    parameter = float(parameter)
            # Add to final output dictionary
            if key == column_name and len(str(parameter)) > 0 and parameter != np.nan and type(parameter) != None:
                out_dictionary[star_id] = parameter
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
    
    # Iterate through each coordinate
    for (k,v), (key,value) in zip(ra.items(), dec.items()):
        ra_coordlist = h_m_s_separator(v)
        dec_coordlist = h_m_s_separator(value)
        if k == key:
            coords_dictionary[k] = [ra_coordlist, dec_coordlist]
    return coords_dictionary


# Question 1:
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
    # Iterate through each magnitude element and temperature element
    for key_m, value_m in magnitude.items(): 
        for key_t, value_t in temperature.items():
            # Check if the star id is in both dictionaries
            if key_m == key_t:
                # Plot data
                try:
                    plt.scatter(value_t, value_m)
                except ValueError:
                    if len(value_t) > 0 < len(value_m):
                        plt.scatter(value_t, value_m)

    plt.gca().invert_yaxis()
    plt.xlabel('Temperature')
    plt.ylabel('Magnitude')
    plt.title('Color Magnitude Diagram')
    #plt.show()
    plt.savefig('color_magnitude', format = 'png')
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
    
    # Iterate through each magnitude element and temperature element
    for key_m, value_m in magnitude.items():
        for key_t, value_t in temperature.items():
            # Check if the star id is in both dictionaries
            if key_m == key_t:
                # Restrictions relating to each star type
                if 13 < value_m and value_t > 0.17:
                    pre_main_sequence.append(int(key_m))
                elif 12 > value_m:
                    giants.append(int(key_m))
                elif 15 < value_m and value_t < 0.75:
                    white_dwarfs.append(int(key_m))
                else:
                    main_sequence.append(int(key_m))

    type_dict['Main Sequence'] = main_sequence
    type_dict['Pre Main Sequence'] = pre_main_sequence
    type_dict['Giants'] =  giants
    type_dict['White Dwarfs'] = white_dwarfs
    
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
    plt.grid()
    #plt.show()
    plt.savefig(data_title, format = 'png')
    plt.clf()
    

def histogram_stats(data):
    """
    Given a dataset, computes various statistics that will be used to analyze 
    properties of the dataset alongside its histogram plot.
    
    Parameters:
        data: a dataset
    
    Returns:
        The sample size, mean, and standard deviation of the dataset.
    """
    if len(data) > 0:
        # Compute statistics
        sample_size = len(data)
        mean = np.mean(data)
        standard_dev = np.std(data)
    
        print '  Summary Statistics:'
        print '\t' + 'Sample Size:', sample_size
        print '\t' + 'Sample Mean:', mean
        print '\t' + 'Sample Standard Deviation:', standard_dev
        
    
def plot_parameter_histogram(type_dict, column_dict, parameter_name):
    """
    Given a type dictionary and a parameter dictionary, plots a histogram of the 
    parameter per type.
    
    Parameters:
        type_dict: a dictionary in which the keys are strings corresponding to
                   the types of stars, and the values are lists of star id 
                   numbers.
        
        column_dict: a dictionary in which the keys are strings corresponding to
                     a star's id number, and the values are floats corresponding
                     to the parameter.
        
        parameter_name: a string representing the parameter being plotted.
        
    Returns:
        a dictionary mapping star types to list of radii.
    """
    type_lst = []
    # Iterate through each type, ensures the keys in the return dict are the 
    # same as in type_dict
    for star_type in type_dict.keys():
        type_lst.append(star_type)
        
    type_to_dict = {}
    
    # Iterate through type_dict
    for n, (name, star_id) in enumerate(type_dict.items()):
        if name == type_lst[n]:
            save = []
            for key, value in column_dict.items():
                # Create a list of parameter values
                if int(key) in star_id:
                    save.append(value)
                    
            type_to_dict[name] = save 
             
    # Plot a histogram for each star type
    for star_type, parameter in type_to_dict.items():
        plot_histogram(parameter, parameter_name, star_type)
        
    return type_to_dict
    

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
    
    # Iterate through each part of the coordinate
    for index, value in enumerate(coordinate):
        # All kepler targets will be (+) declination: ignore '+' in first index
        if value[0] == '+':
            value = value[1:]

        # Obtain the hour, minute, and second values based on index
        if index < 3 and value != ' ':
            hour = str(hour) + str(value) if hour != 0 else value
        elif 3 <= index <= 5 and value != ' ':
            minute = str(minute) + str(value) if minute != 0 else value
        elif index > 5 and value != ' ':
            sec = str(sec) + str(value) if sec != 0 else value

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
        return diff < coord_range


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
        if check_if_coords_close(coord[0], c[0], 30) and check_if_coords_close(coord[1], c[1], 30)  and kic != k:
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


def proximity_type_check(type_dict, ra, dec):
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
    
    # Iterate through each coordinate pair
    for k,v in get_coordinates(ra, dec).items():
        near_stars_list = find_surrounding_stars(k, v, ra, dec)
        for startype, starlist in type_dict.items():
            if len(near_stars_list) > 0:
                out_percents_dict[k] = percent_list_in_list(near_stars_list, starlist)

    return out_percents_dict


def proximity_type_histogram(data, type_dict):
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
    y= {}
    out = []

    # iterate through the data and types
    for k,percents in data.items():
        for n, (t,kiclist) in enumerate(type_dict.items()):
            if int(k) in kiclist:
                if n not in y.keys():
                    y[n] = percents
                else:
                    stack = np.hstack((n, percents))
                    y[n] = stack

    # plot the average of the data in a bar plot
    for index, values in y.items():
        average = sum(values) / len(y)
        plt.bar(index, average, width = 1, align = 'center', )
        out.append(average)

    plt.xticks(np.arange(len(type_dict)), type_dict.keys())
    plt.xlabel('Type of Stars')
    plt.xlim(-1, len(type_dict.keys())+1)

    plt.ylabel('Percentage')
    plt.title('Histogram: Percentage of Proximity Stars by Type')
    plt.autoscale(tight = False)
    plt.ylim(0, 1.0)
    #plt.show()
    plt.savefig('Proximity_Type_histogram', format = 'png')
    plt.clf()
    
    return out


# The code in this function is executed when this file is run as a Python program
def main(test = True):
    # A test file and our main file
    path = "kepler_test50.txt" if test == True else "kepler_500.txt"

    # Get data from csv file
    star_data = read_csv(path) 

    # Question 1:
    magnitude = get_column_data(star_data, "KEP Mag")
    temperature = get_column_data(star_data, "E(B-V)")
    types = get_star_type(magnitude, temperature)
    print 'Question 1:'
    color_magnitude_plot(magnitude, temperature)
    
    # Numerical results
    print '  Number of Stars per Type:'
    print '\t' + 'Number of Main Sequence Stars:', len(types['Main Sequence'])
    print '\t' + 'Number of Pre Main Sequence Stars:', len(types['Pre Main Sequence'])
    print '\t' + 'Number of Giant Stars:', len(types['Giants'])
    print '\t' + 'Number of White Dwarf Stars:', len(types['White Dwarfs'])

    print ' '
    # Question 2:
    star_radii = get_column_data(star_data, "Radius")
    type_radius = plot_parameter_histogram(types, star_radii, 'Radius')
    print 'Question 2:'
    
    # Numerical results
    print 'Main Sequence Radii:'
    histogram_stats(type_radius['Main Sequence'])
    print 'Pre Main Sequence Radii:'
    histogram_stats(type_radius['Pre Main Sequence'])
    print 'Giant Radii:'
    histogram_stats(type_radius['Giants'])
    print 'White Dwarf Radii:'
    histogram_stats(type_radius['White Dwarfs'])
    
    print ' '
    # Question 3:
    ra = get_column_data(star_data, 'RA (J2000)')
    dec = get_column_data(star_data, 'Dec (J2000)')
    print "Question 3:"
    print "  Percentage of Stars in Proximity by Type:"
    
    percentage = proximity_type_check(types, ra, dec)
    output = proximity_type_histogram(percentage, types)
    histogram_stats(percentage.values())

    for n, i in enumerate(types.keys()):
        print '\t' + str(i), output[n]
        
if __name__ == "__main__":
    main()