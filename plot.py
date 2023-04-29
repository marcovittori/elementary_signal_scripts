# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:25:11 2023

@author: luca
"""
import matplotlib.pyplot as plt
import numpy as np
import os

def npy_load(name):

    # Create directory if it doesn't exist
    os.makedirs("Arrays", exist_ok=True)

    # Join the directory and file name using os.path.join()
    file_path = os.path.join("Arrays", f"{name}.npy")
    signal = np.load(file_path)

    return signal 

def npy_save(signal, name ="Signal"):

    # Create directory if it doesn't exist
    os.makedirs("Arrays", exist_ok=True)
    # Join the directory and file name using os.path.join()
    file_path = os.path.join("Arrays", f"{name}.npy")
    np.save(file_path, signal)

def plot_signal(signal, sample_rate=44100, title="signal", color="b", xl="Time[s]", yl="Amplitude", log_scale=False, png_save=False, npy_saves=False):
    """
    Plots a signal and optionally saves it as a PNG or a NPY file.
    Args:
        signal (ndarray): 1D array of audio signal data.
        sample_rate (int): The sample rate of the audio signal. Default is 44100.
        title (str): The title of the plot. Default is "signal".
        color (str): The color of the plot. Default is "b" (blue).
        xl (str): The label for the x-axis. Default is "Time[s]".
        yl (str): The label for the y-axis. Default is "Amplitude".
        png_save (bool): If True, saves the plot as a PNG file in the "Graphics" folder. Default is False.
        npy_save (bool): If True, saves the signal as a NPY file in the "Arrays" folder. Default is False.
    """

    time_array = np.linspace(0, len(signal) / sample_rate, len(signal))

    # Plot the signal
    plt.figure()
    plt.plot(time_array, signal, color)
    plt.title(title)
    plt.xlabel(xl)
    plt.ylabel(yl)

    if log_scale == True:
        plt.yscale("symlog")

    # Save as PNG
    if png_save:
        # Create directory if it doesn't exist
        os.makedirs("Graphics", exist_ok=True)
        # Join the directory and file name using os.path.join()
        file_path = os.path.join("Graphics", f"{title}.png")
        plt.savefig(file_path)

    # Save as NPY
    if npy_saves:
        npy_save(signal,title)


def stem_signal(samples, signal, title="signal", color="b", xl="Samples", yl="Amplitude", log_scale=False, png_save=False, npy_saves=False):
    """
    Plot the discrete signal using a stem plot and save it as PNG and/or NPY file.
    Parameters
    ----------
    samples : numpy.ndarray
        1D array containing the time samples of the signal.
    signal : numpy.ndarray
        1D array containing the amplitude samples of the signal.
    title : str, optional
        Title of the plot (default is "signal").
    color : str, optional
        Color of the stem plot (default is "b").
    xl : str, optional
        Label for the x-axis (default is "Samples").
    yl : str, optional
        Label for the y-axis (default is "Amplitude").
    png_save : bool, optional
        If True, save the plot as a PNG file in the "Graphics" folder (default is False).
    npy_save : bool, optional
        If True, save the signal as a NPY file in the "Arrays" folder (default is False).
    Returns
    -------
    None
    
    Notes
    -------
    This function takes two arrays samples and signal, representing the time samples and the amplitude samples of a discrete signal, and plots it using a stem plot. The title, color, xl and yl parameters are used to customize the plot.
    The png_save and npy_save parameters, if set to True, will save the plot as a PNG file and the signal as a NPY file respectively. These files will be saved in the "Graphics" and "Arrays" folders (created if they don't exist) and will have the same name as the title parameter.    
    """
    plt.figure()
    plt.stem(samples, signal, f"{color}")
    plt.title(title)
    plt.xlabel(xl)
    plt.ylabel(yl)
   
    if log_scale == True:
        plt.yscale("symlog")

    # Save as PNG
    if png_save:
        # Create directory if it doesn't exist
        os.makedirs("Graphics", exist_ok=True)
        # Join the directory and file name using os.path.join()
        file_path = os.path.join("Graphics", f"{title}.png")
        plt.savefig(file_path)

    # Save as NPY
    if npy_saves:
        npy_save(signal,title)

