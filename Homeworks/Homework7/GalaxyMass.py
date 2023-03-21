#!/usr/bin/env python
# coding: utf-8

# In[3]:


# This imports the relevant modules: NumPy and AstroPy.

import numpy as np
import astropy.units as u
from ReadFile import Read # importing ReadFile.py, which is important to our work


# In[52]:


def ComponentMass(filename, particle_type):
    """
    This function goes through each specified data file to calculate the total component mass
    of each type of particle in a galaxy, including dark matter in the halo, stars in the disk
    and stars in the bulge.
    
    Inputs:
    - filename: string
            the name of the file we want to analyze.
    - particle_type: integer
            the type of particle whose composition we want to look at. 1 is for DM halo, 2 for disk, 3 for bulge.   
    
    Output:
    - tot_component_mass: float
            the total component mass of the desired type of particle in the galaxy, divided by 10**12 Msun.
    """
    
    # first, we call the Read function to help us analyze the data
    time, tot_no_particles, data = Read(filename)
    
    # next, we locate all the particles in the galaxy that are of the type we want.
    # we find the indices where the particle type listed in the data file matches our
    # desired type, then we sum up all the particle masses that correspond to these indices.
    # also, note that the masses are stored in the data file with units of 10^10 Msun.
    tot_component_mass = np.sum(data['m'][data['type'] == particle_type])*1e10*u.Msun
    
    return np.round((tot_component_mass / (10**12*u.Msun)), 3)