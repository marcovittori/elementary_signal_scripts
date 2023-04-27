# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 23:52:16 2023

@author: luca
"""
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
    samples = np.arange(start,end+1,1)
    signal = np.zeros(len(samples))
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
    samples = np.arange(start,end+1,1)
    signal = np.zeros(len(samples))
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
    samples = np.arange(start, end+1, 1)
    signal = np.zeros(len(samples))
    mask = (samples > 0-width-1) & (samples < width+1)
    signal[mask] = amplitude
    
    return samples, signal

