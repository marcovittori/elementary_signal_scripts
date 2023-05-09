import numpy as np
from scipy.signal import fftconvolve

def invert_time(signal):
    """Inverts the time axis of a given signal.

    Parameters:
        signal (array): The signal to invert.

    Returns:
        array: The inverted signal.
    """
    return np.flip(signal)

def invert_amplitude(signal):
    """Inverts the amplitude of a given signal.

    Parameters:
        signal (array): The signal to invert.

    Returns:
        array: The inverted signal.
    """
    return -1*signal

def shift_time(samples, shift):
    """Shifts the time axis of a given set of samples by a given amount.

    Parameters:
        samples (array): The samples to shift.
        shift (int): The amount to shift the samples by.

    Returns:
        array: The shifted samples.
    """
    samples += shift
    return samples

def shift_amplitude(signal, shift):
    """Shifts the amplitude of a given signal by a given amount.

    Parameters:
        signal (array): The signal to shift.
        shift (int): The amount to shift the amplitude by.

    Returns:
        array: The shifted signal.
    """
    signal += shift
    return signal

def match_dimentions(samples_1, signal_1, samples_2, signal_2):
    """Matches the dimensions of two signals by extending them with zeros.

    Parameters:
        samples_1 (array): The sample points of the first signal.
        signal_1 (array): The amplitude values of the first signal.
        samples_2 (array): The sample points of the second signal.
        signal_2 (array): The amplitude values of the second signal.

    Returns:
        tuple: A tuple containing the new sample points and the extended amplitude values for both signals.
    """
    # Check for the min and max values for both sample arrays
    min_val = min(min(samples_1), min(samples_2))
    max_val = max(max(samples_1), max(samples_2))
    samples = np.arange(min_val, max_val+1)
    
    # Define two new signals to be an array of zeros
    signal_1_new = np.zeros(len(samples))
    signal_2_new = np.zeros(len(samples))
    
    # Assign the original amplitudes on the respective places
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
    """Adds two signals together.

    Parameters:
        samples_1 (array): The sample points of the first signal.
        signal_1 (array): The amplitude values of the first signal.
        samples_2 (array): The sample points of the second signal.
        signal_2 (array): The amplitude values of the second signal.

    Returns:
        tuple: A tuple containing the new sample points and the sum of the two signals.
    """
    y, x1, x2 = match_dimentions(samples_1, signal_1, samples_2, signal_2)
    out = x1 + x2
    return y, out

def multiplication(samples_1, signal_1, samples_2, signal_2):
    """Multiplies two signals together using element-wise multiplication.

    Parameters:
        samples_1 (array): The sample points of the first signal.
        signal_1 (array): The amplitude values of the first signal.
        samples_2 (array): The sample points of the second signal.
        signal_2 (array): The amplitude values of the second signal.

    Returns:
        tuple: A tuple containing the new sample points and the product of the two signals.
    """
    y, x1, x2 = match_dimentions(samples_1, signal_1, samples_2, signal_2)
    out = x1 * x2
    return y, out


def convolution(signal_1, signal_2):
    """Computes the convolution of two signals using FFT.

    Parameters:
        signal_1 (array): The amplitude values of the first signal.
        signal_2 (array): The amplitude values of the second signal.

    Returns:
        array: The convolution of the two signals.
    """
    return fftconvolve(signal_1, signal_2)
