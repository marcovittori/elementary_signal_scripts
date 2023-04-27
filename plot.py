# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:25:11 2023

@author: luca
"""
import matplotlib.pyplot as plt
import numpy as np
import os


def plot_signal(signal, sample_rate=44100, title="signal", color="b", xl="Time[s]", yl="Amplitude", png_save=False, npy_save=False):
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

    # Save as PNG
    if png_save:
        # Create directory if it doesn't exist
        os.makedirs("Graphics", exist_ok=True)
        # Join the directory and file name using os.path.join()
        file_path = os.path.join("Graphics", f"{title}.png")
        plt.savefig(file_path)

    # Save as NPY
    if npy_save:
        # Create directory if it doesn't exist
        os.makedirs("Arrays", exist_ok=True)
        # Join the directory and file name using os.path.join()
        file_path = os.path.join("Arrays", f"{title}.npy")
        np.save(file_path, signal)


def stem_signal(samples, signal, title="signal", color="b", xl="Samples", yl="Amplitude", png_save=False, npy_save=False):
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
   
    # Save as PNG
    if png_save:
        # Create directory if it doesn't exist
        os.makedirs("Graphics", exist_ok=True)
        # Join the directory and file name using os.path.join()
        file_path = os.path.join("Graphics", f"{title}.png")
        plt.savefig(file_path)

    # Save as NPY
    if npy_save:
        # Create directory if it doesn't exist
        os.makedirs("Arrays", exist_ok=True)
        # Join the directory and file name using os.path.join()
        file_path = os.path.join("Arrays", f"{title}.npy")
        np.save(file_path, signal)

def load_plot(npy_file, sample_rate = 44100, title="signal", color="b", xl="Samples", yl="Amplitude", png_save=False):
    """
    Load a numpy array from an .npy file and plot the signal.

    Parameters
    ----------
    npy_file : str
        Path to the .npy file containing the signal data.
    sample_rate : int, optional
        Sampling rate of the signal in Hz (default is 44100).
    title : str, optional
        Title of the plot (default is "signal").
    color : str, optional
        Color of the plot (default is "b").
    xl : str, optional
        Label for the x-axis (default is "Time (s)").
    yl : str, optional
        Label for the y-axis (default is "Amplitude").
    png_save : bool, optional
        Whether to save the plot as a .png file (default is False).

    Notes
    -----
    The signal is assumed to be a mono audio signal, so the x-axis is labeled as "Time (s)" instead of "Samples".

    If `png_save` is True, the plot will be saved as a .png file in the "Graphics" directory with the title as the file name.

    Examples
    --------
    >>> load_plot("signal.npy", sample_rate=48000, title="My Signal", color="r", xl="Time (ms)", png_save=True)
    """
    signal = np.load(f"{npy_file}")
    time_array = np.linspace(0, len(signal) / sample_rate, len(signal))

    plt.figure()
    plt.plot(time_array, signal, f"{color}")
    plt.title(title)
    plt.xlabel(xl)
    plt.ylabel(yl)

    # Save as PNG
    if png_save:
        # Create directory if it doesn't exist
        os.makedirs("Graphics", exist_ok=True)
        # Join the directory and file name using os.path.join()
        file_path = os.path.join("Graphics", f"{title}.png")
        plt.savefig(file_path)
    
def load_stem(npy_file,start=0, title="signal", color="b", xl="Samples", yl="Amplitude", png_save=False):
    """
    Load a signal from a NPY file and plot it as a stem plot.

    Parameters:
    npy_file (str): path to the NPY file containing the signal.
    start (float, optional): starting point for the sample index. Defaults to 0.
    title (str, optional): title of the plot. Defaults to "signal".
    color (str, optional): color of the stems. Defaults to "b".
    xl (str, optional): label for the x-axis. Defaults to "Samples".
    yl (str, optional): label for the y-axis. Defaults to "Amplitude".
    png_save (bool, optional): whether to save the plot as a PNG file or not. Defaults to False.

    Returns:
    None
    
    Notes:
    The function loads a signal from a NPY file and plots it as a stem plot.
    The npy_file parameter is a required string indicating the path to the NPY file containing the signal to be loaded.
    The inicio parameter is an optional float indicating the starting point for the sample index. It defaults to 0.
    The title parameter is an optional string indicating the title of the plot. It defaults to "signal".
    The color parameter is an optional string indicating the color of the stems in the plot. It defaults to "b".
    The xl parameter is an optional string indicating the label for the x-axis of the plot. It defaults to "Samples".
    The yl parameter is an optional string indicating the label for the y-axis of the plot. It defaults to "Amplitude".
    The png_save parameter is an optional boolean indicating whether to save the plot as a PNG file or not. It defaults to False.
    """
    signal = np.load(f"{npy_file}")
    samples = np.linspace(start, len(signal)+inicio, 1)

    plt.figure()
    plt.stem(samples, signal, f"{color}")
    plt.title(title)
    plt.xlabel(xl)
    plt.ylabel(yl)

    # Save as PNG
    if png_save:
        # Create directory if it doesn't exist
        os.makedirs("Graphics", exist_ok=True)
        # Join the directory and file name using os.path.join()
        file_path = os.path.join("Graphics", f"{title}.png")
        plt.savefig(file_path)
