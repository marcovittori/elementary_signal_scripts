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
    new_samples = np.zeros(len(samples), dtype= np.int16)

    for i in range(len(samples)):
        new_samples[i] = int(samples[i]+shift)

    return new_samples

def shift_amplitude(signal, shift):
    signal += shift
    return signal

def match_dimentions(samples_1, signal_1, samples_2, signal_2):
    
    # Check for the min and max values for both sample arrays
    min_val = min(min(samples_1), min(samples_2))
    max_val = max(max(samples_1), max(samples_2))
    samples = np.arange(min_val, max_val+1, 1)
    
    # create arrays with zeros to be concatenated
    zeros_before_1 = np.zeros(abs(min_val) - abs(min(samples_1)))
    zeros_after_1 = np.zeros(abs(max_val) - abs(max(samples_1)))
    zeros_before_2 = np.zeros(abs(min_val) - abs(min(samples_2)))
    zeros_after_2 = np.zeros(abs(max_val) - abs(max(samples_2)))
    
    # Concatenate zeros for the new samples
    signal_1 = np.concatenate((zeros_before_1, signal_1, zeros_after_1))
    signal_2 = np.concatenate((zeros_before_2, signal_2, zeros_after_2))
    
    return samples, signal_1, signal_2

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