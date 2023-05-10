import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve

def sintetic_impulse(fs=44100, t60=1, sigma=0.1):
    """
    Generate a synthetic impulse response using an exponential decay envelope and Gaussian noise.

    Parameters:
        fs (int, optional): sampling rate in Hz (default 44100)
        t60 (float, optional): decay time in seconds for the impulse response (default 1)
        sigma (float, optional): standard deviation of the Gaussian noise (default 0.1)

    Returns:
        tuple: (t, synth_impulse), where t is an array of time values and synth_impulse is an array 
        of values for the synthetic impulse response.

    """
    # Create a time array with a length of 5 seconds
    t = np.linspace(0, 5, 5*fs)  
    
    # Generate noise
    noise = np.random.normal(0,1,t.size)
    noise_floor = sigma*np.random.normal(0,1,t.size)
    
    # Calculate the decay time constant
    tau = -t60/np.log(10**-3)  
    
    # Generate an exponential envelope with the given decay time constant
    envelope = np.exp(-t/tau)  
    
    # Apply the envelope to the noise, add noise floor
    synth_impulse = envelope*noise + noise_floor  
    synth_impulse = synth_impulse/np.max(np.abs(synth_impulse))  # normalize the synthetic impulse
    
    return t, synth_impulse
    

def reverb(signal, fs=44100, t60=2, sigma=0):
    """
    Apply a synthetic impulse response to a given audio signal, creating a reverberant signal.

    Parameters:
        signal (array): audio signal to be reverberated
        fs (int, optional): sampling rate in Hz (default 44100)
        t60 (float, optional): decay time in seconds for the impulse response (default 2)
        sigma (float, optional): standard deviation of the Gaussian noise (default 0)

    Returns:
        tuple: (t_rev, rev_signal, t_imp, synth_impulse), where t_rev is an array of time values for 
        the reverberant signal, rev_signal is an array of values for the reverberant signal, t_imp is 
        an array of time values for the synthetic impulse response, and synth_impulse is an array of 
        values for the synthetic impulse response.

    """
    # Normalize the input signal
    signal = signal/np.max(np.abs(signal))  

    # Generate synthetic impulse response
    t_imp, synth_impulse = sintetic_impulse(fs,t60,sigma)  

    # Convolve the input signal with the impulse response
    rev_signal = fftconvolve(signal, synth_impulse)

    # Normalize the reverberant signal
    rev_signal = rev_signal/np.max(np.abs(rev_signal)) 
    t_rev = np.linspace(0, len(rev_signal)/fs, rev_signal.size)  # create a time array for the reverberant signal

    return t_rev, rev_signal, t_imp, synth_impulse


if __name__ =="__main__":
    # Generate and plot a synthetic impulse response
    t, synth_impulse = sintetic_impulse()
    plt.plot(synth_impulse)
    plt.show()
