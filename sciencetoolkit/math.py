'''
Math helper functions for Jython

Authors:
    Andrew Valente


All functions are written in pure Python and will thus work with Jython and
standard Python. There are basic statistical functions and utilities for common
array operations. Meant for helping with some ImageJ scripting tools.

    STATISTICAL:
    average() - mean
    median() - median
    stdev() - standard deviation (sample or population via flag)

    ARRAY OPERATIONS:
    countif()
    equals() - apply the "==" operator between two lists or a list and a scalar
               element-wise
'''

# STATISTICAL FUNCTIONS --------------------------------------------------------
def average(data):
    '''
    Calculate the average from the elements of a list.

    Parameters
    ----------
    data : list
        The 1d list to compute the average from.

    Returns
    -------
    data_mean : float
        The average (mean) of the data.
    '''
    data_entries = len(data)
    data_mean = sum([(entry/data_entries) for entry in data])
    return(data_mean)

def median(data):
    '''
    TODO: complete
    '''
