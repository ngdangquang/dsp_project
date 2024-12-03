import numpy as np
from scipy.signal import firwin

# Function to design an FIR filter using the windowing method (detailed version)
def design_fir_with_window(N, cutoff, fs, window_type='hann'):
    """
    Design an FIR filter using the windowing method. This function calculates the filter 
    coefficients based on the specified order, cutoff frequency, sampling frequency, 
    and window type.
    
    Parameters:
    N : int
        The order of the filter (number of taps)
    cutoff : float
        The cutoff frequency (Hz) of the filter
    fs : float
        The sampling frequency (Hz)
    window_type : str
        The window function to use (default 'hann'). Options include 'hamming', 'blackman', 'bartlett', etc.
    
    Returns:
    fir_coeff : numpy array
        The filter coefficients (taps) that define the FIR filter.
    """
    # Normalize the cutoff frequency to the Nyquist frequency (fs / 2)
    normal_cutoff = cutoff / (0.5 * fs)  # Normalized cutoff frequency
    fir_coeff = firwin(N, normal_cutoff, window=window_type)  # FIR filter design using window function
    return fir_coeff

# Simpler FIR filter design function without window option (for basic FIR design)
def design_fir(N, cutoff, fs):
    """
    Design a simple FIR filter without windowing, just based on the cutoff frequency and order.
    
    Parameters:
    N : int
        The order of the filter (number of taps)
    cutoff : float
        The cutoff frequency (Hz) of the filter
    fs : float
        The sampling frequency (Hz)
    
    Returns:
    fir_coeff : numpy array
        The filter coefficients (taps) that define the FIR filter.
    """
    # Normalize the cutoff frequency to the Nyquist frequency (fs / 2)
    normal_cutoff = cutoff / (0.5 * fs)  # Normalized cutoff frequency
    fir_coeff = firwin(N, normal_cutoff)  # FIR filter design without window function
    return fir_coeff
