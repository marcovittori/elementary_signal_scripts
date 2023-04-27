# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 23:52:16 2023

@author: luca
"""
import numpy as np

import numpy as np

def unit_impulse(start=-10, end=10, amplitude=1):
    """
    Creates a unit impulse signal.

    Parameters:
    start (int): the starting value of the signal (default=-10)
    end (int): the ending value of the signal (default=10)
    amplitude (float): the amplitude of the impulse (default=1)

    Returns:
    tuple: A tuple containing two numpy arrays. The first array contains the
    sample values and the second array contains the signal values.
    """
    # Creates a sample array
    samples = np.arange(start,end+1,1)
    # Creates the signal with zeros
    signal = np.zeros(len(samples))
    # Makes the amplitude 1 on the origin to make the signal
    mask = samples == 0
    signal[mask] = amplitude
    
    return samples, signal


def heavy_side(start=-10, end=10, amplitude=1):
    """
    Creates a Heaviside step function.

    Parameters:
    start (int): the starting value of the signal (default=-10)
    end (int): the ending value of the signal (default=10)
    amplitude (float): the amplitude of the Heaviside function (default=1)

    Returns:
    tuple: A tuple containing two numpy arrays. The first array contains the
    sample values and the second array contains the signal values.
    """
    # Create a sample array
    samples = np.arange(start,end+1,1)
    # Create the signal with zeros
    signal = np.zeros(len(samples))
    # Change the amplitude to generate the given signal
    mask = samples > 0
    signal[mask] = amplitude
    
    return samples, signal


def rectangular_pulse(width, start=-5, end=5, amplitude=1):
    """
    Creates a rectangular pulse signal.

    Parameters:
    width (int): the width of the pulse
    start (int): the starting value of the signal (default=-5)
    end (int): the ending value of the signal (default=5)
    amplitude (float): the amplitude of the pulse (default=1)

    Returns:
    tuple: A tuple containing two numpy arrays. The first array contains the
    sample values and the second array contains the signal values.
    """
    # Create a sample array
    samples = np.arange(start, end+1, 1)
    # Create the signal
    signal = np.zeros(len(samples))
    # Change the amplitude following the parameters
    mask = (samples > 0-width-1) & (samples < width+1)
    signal[mask] = amplitude
    
    return samples, signal

def triangular_pulse(start, end, amplitude=1, width=1):
    """
    Creates a triangular pulse signal.

    Parameters:
    start (int): the starting value of the signal
    end (int): the ending value of the signal
    amplitude (float): the amplitude of the pulse (default=1)
    width (int): the width of the pulse (default=1)

    Returns:
    tuple: A tuple containing two numpy arrays. The first array contains the
    sample values and the second array contains the signal values.
    """
    # Create a sample array
    samples = np.arange(start, end+1, 1) 
    # Concatenate two lines to make the triangle
    n1 = np.linspace(0, 1, num=width//2, endpoint=False)
    n2 = np.linspace(1, 0, num=width//2+1)
    signal = np.concatenate((np.zeros(-start-width//2), n1, n2, np.zeros(end-width//2)))
    
    return samples, amplitude * signal 

def exponential_signal(start, end, amplitude = 1, rate = 1):
    """
    Creates an exponential signal.

    Parameters:
    start (int): the starting value of the signal
    end (int): the ending value of the signal
    amplitude (float): the amplitude of the exponential signal (default=1)
    rate (float): the decay rate of the exponential function (default=1)

    Returns:
    tuple: A tuple containing two numpy arrays. The first array contains the
    sample values and the second array contains the signal values.
    """
    # Create a sample array
    samples = np.arange(start, end+1, 1)
    # Create the signal
    signal = amplitude * np.exp(rate * samples)

    return samples, signal

def normal_signal(start, end, mean, std_dev):
    """
    Creates a signal with values sampled from a normal distribution.

    Parameters:
    start (int): the starting value of the signal
    end (int): the ending value of the signal
    mean (float): the mean of the normal distribution
    std_dev (float): the standard deviation of the normal distribution

    Returns:
    tuple: A tuple containing two numpy arrays. The first array contains the
    sample values and the second array contains the signal values.
    """
    # Create a sample array
    samples = np.arange(start,end+1,1)
    # Create the signal
    signal = np.random.normal(mean, std_dev, size=end-start+1)

    return samples, signal
