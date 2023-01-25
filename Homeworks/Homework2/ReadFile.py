#!/usr/bin/env python
# coding: utf-8

# This imports the relevant modules: NumPy and AstroPy.

import numpy as np
import astropy.units as u

'''
This function reads a data file that's formatted in the typical way that we expect in this class.In such 
a file, the first line would be the time of the simulation, the second line the number of particles,
the third line the header for each column, and from then on we have the actual data.

Input: filename - the name of the data file, obviously.

Outputs:
1. time - the time of the simulation (type: float)
2. particle_num - the number of particles in the simulation (type: int)
3. data - a NumPy array with all the data from the file (type: NumPy array)
'''

def Read(filename):
    # This line opens the data file.
    file = open(filename, 'r')
    
    # This part retrieves the time of the simulation, which is stored in the data file's 1st line.
    line1 = file.readline()
    label, value = line1.split()
    time = float(value)*u.Myr # This converts the time into a float with units of Myr.
        
    # This part retrieves the particle number in the simulation, which is stored in the data file's 2nd line.
    line2 = file.readline()
    label, value = line2.split()
    particle_num = int(value) # This saves the particle number as an integer.
    
    # This line closes the data file.
    file.close
    
    # This line generates a big NumPy array from the data after the data file's 3rd line.
    data = np.genfromtxt(filename, dtype=None, names=True, skip_header=3)
    
    # This makes sure that the function returns the time, the particle number and the NumPy array.
    return time, particle_num, data 
