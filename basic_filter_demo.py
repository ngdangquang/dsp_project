import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, cheby1

# 1. Theory: FIR and IIR Filter Basics
# -----------------------------------
print("FIR Filter:")
print("  - Finite Impulse Response (FIR) filters have a finite response to an impulse input signal.")
print("  - They are always stable and have a linear phase response, but they require a larger number of taps (coefficients) compared to IIR filters for similar performance.")
print("  - FIR filters are designed using techniques like windowing, frequency sampling, etc.\n")

print("IIR Filter:")
print("  - Infinite Impulse Response (IIR) filters have an infinite response to an impulse input signal.")
print("  - IIR filters are more efficient than FIR filters in terms of the number of coefficients required, but they may have stability issues and nonlinear phase response.")
print("  - IIR filters are commonly designed using methods like the Butterworth, Chebyshev, or elliptic filter designs.\n")

# 2. Design FIR Filter using the Windowing Method
# ----------------------------------------------
def design_fir(N, cutoff, fs):
    """
    Design a basic FIR filter using the windowing method.
    
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

# Design the FIR filter (example)
fs = 500.0  # Sampling frequency in Hz
cutoff = 50.0  # Cutoff frequency in Hz
order_fir = 31  # Filter order for FIR filter

fir_coeff = design_fir(order_fir, cutoff, fs)
print("FIR Filter Coefficients:", fir_coeff)

# 3. Design Chebyshev IIR Filter
# -----------------------------
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

# Design the IIR filter (Chebyshev)
order_cheby = 4  # Filter order for Chebyshev IIR filter
ripple = 1.0  # Ripple for Chebyshev filter
b, a = design_chebyshev_filter(order_cheby, cutoff, fs, ripple)
print("IIR Filter Coefficients (Chebyshev):")
print("b:", b)
print("a:", a)

# 4. Visualizing the FIR and IIR Filter Frequency Response (optional)
# ---------------------------------------------------------------
from scipy.signal import freqz

# FIR filter frequency response
w_fir, h_fir = freqz(fir_coeff, worN=8000)
plt.subplot(2, 1, 1)
plt.plot(0.5 * fs * w_fir / np.pi, np.abs(h_fir), 'b')
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5 * fs)
plt.title('FIR Filter Frequency Response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Gain')

# IIR filter frequency response
w_iir, h_iir = freqz(b, a, worN=8000)
plt.subplot(2, 1, 2)
plt.plot(0.5 * fs * w_iir / np.pi, np.abs(h_iir), 'r')
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5 * fs)
plt.title('IIR Filter Frequency Response (Chebyshev)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Gain')

plt.tight_layout()
plt.show()

# Conclusion
print("\nBasic FIR and IIR filter designs completed. Check the frequency response plots.")


#PLOT EXPLAIN:
"""
FIR Filter:
"The FIR filter allows frequencies below 50 Hz to pass with minimal attenuation, 
while attenuating frequencies above 50 Hz. The transition from pass to stop is gradual, 
which is typical of FIR filters. It has a flat passband (no ripples), and the gain decreases smoothly after the cutoff frequency."

Chebyshev IIR Filter:
"The Chebyshev filter has a ripple in the passband (a feature that allows it to achieve a sharper transition with fewer filter coefficients). 
The transition from the passband to the stopband is much steeper compared to the FIR filter. 
However, this comes at the cost of non-linear phase behavior, which may cause phase distortion in some applications. 
Despite this, the IIR filter is computationally more efficient and can achieve similar performance with fewer coefficients than an FIR filter."

"""