import matplotlib.pyplot as plt
import numpy as np
import os

def npy_load(name):
    """
    Load two .npy file from the 'Arrays' folder and returns its content as two numpy array.

    Parameters:
        name (str): Name of the file to be loaded (without the .npy extension).

    Returns:
        Tuple: Array of samples loaded and an array of the loaded data.

    Notes:
        The array with the name.npy have to exist. If you want to load your own signal
        you must create a samples array named name_samples.npy
    """
    # Create directory if it doesn't exist
    os.makedirs("Arrays", exist_ok=True)

    # Join the directory and file name using os.path.join()
    file_path_samples =os.path.join("Arrays", f"{name}_samples.npy")
    file_path = os.path.join("Arrays", f"{name}.npy")

    signal = np.load(file_path)
    samples = np.load(file_path_samples)

    return samples, signal 

def npy_save(samples, signal, name ="Signal"):
    """
    Save a numpy signal array with its samples array as a .npy file in the 'Arrays' folder.

    Parameters:
        samples(ndarray): Array of samples to be saved
        signal (ndarray): Array to be saved.
        name (str, optional): Name of the file to be saved (without the .npy extension). Default is 'Signal'.

    Returns:
        None
    """
    # Create directory if it doesn't exist
    os.makedirs("Arrays", exist_ok=True)

    # Join the directory and file name using os.path.join()
    file_path = os.path.join("Arrays", f"{name}.npy")
    file_path_samples =os.path.join("Arrays", f"{name}_samples.npy")
    np.save(file_path, signal)
    np.save(file_path_samples, samples)

def plot_signal(signal, sample_rate=44100, title="Signal", color="b", xl="Time[s]", yl="Amplitude", log_scale_y=False, log_scale_x=False, png_save=False, npy_saves=False):
    """
    Plots a signal and optionally saves it as a PNG or a NPY file.

    Parameters:
        signal (ndarray): 1D array of audio signal data.
        sample_rate (int, optional): The sample rate of the audio signal. Default is 44100.
        title (str, optional): The title of the plot. Default is "Signal".
        color (str, optional): The color of the plot. Default is "b" (blue).
        xl (str, optional): The label for the x-axis. Default is "Time[s]".
        yl (str, optional): The label for the y-axis. Default is "Amplitude".
        log_scale (bool, optional): If True, use logarithmic scale for the y-axis. Default is False.
        png_save (bool, optional): If True, saves the plot as a PNG file in the "Graphics" folder. Default is False.
        npy_save (bool, optional): If True, saves the signal as a NPY file in the "Arrays" folder. Default is False.

    Returns:
        None
    """
    time_array = np.linspace(0, len(signal) / sample_rate, len(signal))

    # Plot the signal
    plt.figure()
    plt.plot(time_array, signal, color)
    plt.title(title)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.grid()

    if log_scale_x == True:
        plt.xscale("symlog")

    if log_scale_y == True:
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
        npy_save(time_array, signal, title)


def stem_signal(samples, signal, title="Signal", color="b", xl="Samples", yl="Amplitude", log_scale_y=False, log_scale_x=False, png_save=False, npy_saves=False):
    """
    Plots a signal and optionally saves it as a PNG or a NPY file.

    Parameters:
        samples (ndarray): 1D array containing the time samples of the signal.
        signal (ndarray): 1D array containing the amplitude samples of the signal.
        title (str, optional): Title of the plot. Default is "Signal".
        color (str, optional): Color of the stem plot. Default is "b" (blue).
        xl (str, optional): Label for the x-axis. Default is "Samples".
        yl (str, optional): Label for the y-axis. Default is "Amplitude".
        log_scale (bool, optional): If True, use logarithmic scale for the y-axis. Default is False.
        png_save (bool, optional): If True, saves the plot as a PNG file in the "Graphics" folder. Default is False.
        npy_save (bool, optional): If True, saves the signal as a NPY file in the "Arrays" folder. Default is False.

    Returns:
        None
    """
    plt.figure()
    plt.stem(samples, signal, f"{color}")
    plt.title(title)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.grid()
   
    if log_scale_x == True:
        plt.xscale("symlog")

    if log_scale_y == True:
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
        npy_save(samples, signal, title)

