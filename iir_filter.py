import numpy as np
from scipy.signal import cheby1, firwin

# --- FIR Filter Design ---
def design_fir(N, cutoff, fs):
    """
    Design a basic FIR low-pass filter using the windowing method.
    
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
    normal_cutoff = cutoff / (0.5 * fs)  # Normalize the cutoff frequency to Nyquist
    fir_coeff = firwin(N, normal_cutoff)  # Use a Hamming window by default
    return fir_coeff

# --- IIR Chebyshev Filter Design ---
def design_chebyshev_filter(order, cutoff, fs, ripple=1.0):
    """
    Design an IIR Chebyshev Type I low-pass filter.
    
    Parameters:
    order : int
        The order of the filter (number of poles)
    cutoff : float
        The cutoff frequency (Hz) of the filter
    fs : float
        The sampling frequency (Hz)
    ripple : float
        The maximum ripple allowed in the passband (default 1.0 dB)
    
    Returns:
    b, a : numpy arrays
        The numerator (b) and denominator (a) coefficients of the filter.
    """
    nyquist = 0.5 * fs  # Nyquist frequency (half the sampling frequency)
    normal_cutoff = cutoff / nyquist  # Normalize the cutoff frequency
    b, a = cheby1(order, ripple, normal_cutoff, btype='low', analog=False)  # Chebyshev filter design
    return b, a
