# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:42:50 2023

@author: luca
"""

import numpy as np
from scipy.signal import fftconvolve

def invert_time(signal):
    return np.flip(signal)

def invert_amplitude(signal):
    return -1*signal

def shift_time(samples, shift):
    for i in range(len(samples)):
        samples[i]=samples[i]+shift
    return samples

def shift_amplitude(signal, shift):
    signal += shift
    return signal

def match_dimentions(samples_1, signal_1, samples_2, signal_2):
    
    # Check for the min and max values for both sample arrays
    min_val = min(min(samples_1), min(samples_2))
    max_val = max(max(samples_1), max(samples_2))
    samples = np.arange(min_val, max_val+1)
    
    # Define two new signals to be an array of zeros
    signal_1_new = np.zeros(len(samples))
    signal_2_new = np.zeros(len(samples))
    
    for i in range(len(samples)):
        if samples[i] == min(samples_1):
            for j in range(len(signal_1)):
                signal_1_new[j+i] = signal_1[j]
    
    for i in range(len(samples)):
        if samples[i] == min(samples_2):
            for j in range(len(signal_2)):
                signal_2_new[j+i] = signal_2[j]
                
    return samples, signal_1_new, signal_2_new

def addition(samples_1, signal_1, samples_2, signal_2):
    
    y, x1, x2 = match_dimentions(samples_1, signal_1, samples_2, signal_2)
    out = x1 + x2
    return y, out

def multiplication(samples_1, signal_1, samples_2, signal_2):
    
    y, x1, x2 = match_dimentions(samples_1, signal_1, samples_2, signal_2)
    out = x1 * x2
    return y, out

def convolution(signal_1, signal_2):
    return fftconvolve(signal_1, signal_2)
