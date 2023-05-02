import numpy as np

def unit_impulse(start=-10, end=10, amplitude=1, shift=0):
    """
    Creates a unit impulse signal.

    Parameters:
        start (int, optional): the starting value of the signal (default=-10)
        end (int, optional): the ending value of the signal (default=10)
        amplitude (float, optional): the amplitude of the impulse (default=1)
        shift (int, optional): the shift of the impulse (default=0)

    Returns:
        tuple: A tuple containing two numpy arrays. The first array contains the
        sample values and the second array contains the signal values.
    """
    # Creates a sample array
    samples = np.arange(start, end+1, 1)
    # Creates the signal with zeros
    signal = np.zeros(len(samples))
    # Makes the amplitude 1 on the origin to make the signal
    mask = samples == shift
    signal[mask] = amplitude
    
    return samples, signal


def heavy_side(start=-10, end=10, amplitude=1, shift=0):
    """
    Creates a Heaviside step function.

    Parameters:
        start (int, optional): the starting value of the signal (default=-10)
        end (int, optional): the ending value of the signal (default=10)
        amplitude (float, optional): the amplitude of the Heaviside function (default=1)
        shift (int, optional): the shift of the Heaviside function (default=0)

    Returns:
        tuple: A tuple containing two numpy arrays. The first array contains the
        sample values and the second array contains the signal values.
    """
    # Create a sample array
    samples = np.arange(start, end+1, 1)
    # Create the signal with zeros
    signal = np.zeros(len(samples))
    # Change the amplitude to generate the given signal
    mask = samples >= shift
    signal[mask] = amplitude
    
    return samples, signal


def rectangular_pulse(start=-5, end=5, width=4, amplitude=1, shift=0):
    """
    Creates a rectangular pulse signal.

    Parameters:
        start (int, optional): the starting value of the signal (default=-5)
        end (int, optional): the ending value of the signal (default=5)
        width (int): the width of the pulse
        amplitude (float, optional): the amplitude of the pulse (default=1)
        shift (int, optional): the shift of the pulse (default=0)

    Returns:
        tuple: A tuple containing two numpy arrays. The first array contains the
        sample values and the second array contains the signal values.
    """
    # Create a sample array
    samples = np.arange(start, end+1, 1)
    # Create the signal
    signal = np.zeros(len(samples))
    # Change the amplitude following the parameters
    mask = (samples > shift-(width/2)-1) & (samples < shift+(width/2)+1)
    signal[mask] = amplitude
    
    return samples, signal

def triangular_pulse(start=-10, end=10, amplitude=1, width=1, shift=0):
    """
    Creates a triangular pulse signal.

    Parameters:
        start (int, optional): the starting value of the signal (default=-10)
        end (int, optional): the ending value of the signal (default=10)
        amplitude (float, optional): the amplitude of the pulse (default=1)
        width (int, optional): the width of the pulse (default=1)
        shift (int, optional): the shift of the pulse (default=0)

    Returns:
        tuple: A tuple containing two numpy arrays. The first array contains the
        sample values and the second array contains the signal values.
    """
    # Create a sample array
    samples = np.arange(start, end+1, 1) 
    # Concatenate two lines to make the triangle
    n1 = np.linspace(0, 1, num=width//2, endpoint=False)
    n2 = np.linspace(1, 0, num=width//2+1)
    signal = np.concatenate((np.zeros(shift-start-width//2), n1, n2, np.zeros(shift+end-width//2)))
    
    return samples, amplitude * signal 

def exponential_signal(start=0, end=10, amplitude=1, base=2, rate=-1):
    """
    Creates an exponential signal.

    Parameters:
        start (int, optional): the starting value of the signal (default=0)
        end (int, optional): the ending value of the signal (default=10)
        amplitude (float, optional): the amplitude of the exponential signal (default=1)
        base (float, optional): the base of the exponential function (default=2)
        rate (float, optional): the decay rate of the exponential function (default=-1)

    Returns:
        tuple: A tuple containing two numpy arrays. The first array contains the
        sample values and the second array contains the signal values.
    """
    # Create a sample array
    samples = np.arange(start, end+1, 1)
    # Create the signal
    signal = amplitude * np.power(base, -samples*rate)

    return samples, signal

def normal_signal(start=0, end=10, mean=0, std_dev=1):
    """
    Creates a signal with values sampled from a normal distribution.

    Parameters:
        start (int, optional): the starting value of the signal (default=0)
        end (int, optional): the ending value of the signal (default=10)
        mean (float, optional): the mean of the normal distribution (default=0)
        std_dev (float, optional): the standard deviation of the normal distribution (default=1)

    Returns:
        tuple: A tuple containing two numpy arrays. The first array contains the
        sample values and the second array contains the signal values.
    """
    # Create a sample array
    samples = np.arange(start,end+1,1)
    # Create the signal
    signal = np.random.normal(mean, std_dev, size=end-start+1)

    return samples, signal