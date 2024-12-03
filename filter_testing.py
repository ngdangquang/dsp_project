from fir_filter import design_fir_with_window
from iir_filter import design_chebyshev_filter
from signals import generate_signal
from scipy.signal import convolve, lfilter
import matplotlib.pyplot as plt

# Parameters for filter design
fs = 1000  # Sampling frequency in Hz
cutoff = 150  # Cutoff frequency in Hz for both FIR and IIR filters
N = 51  # FIR filter order (number of taps)
order = 4  # IIR filter order
ripple = 1.0  # Ripple factor for IIR filter (dB)

# Generate a noisy signal (sine wave + Gaussian noise)
t, noisy_signal = generate_signal(fs)

# Design FIR filter using windowing method
fir_coeff = design_fir_with_window(N, cutoff, fs)

# Design IIR filter using Chebyshev Type I method
b_cheby, a_cheby = design_chebyshev_filter(order, cutoff, fs, ripple)

# Apply FIR filter to the noisy signal
filtered_signal_fir = convolve(noisy_signal, fir_coeff, mode='same')

# Apply IIR filter to the noisy signal
filtered_signal_iir = lfilter(b_cheby, a_cheby, noisy_signal)

# Plotting the signals
plt.figure(figsize=(12, 6))

# Plot original noisy signal
plt.subplot(3, 1, 1)
plt.plot(t, noisy_signal, label='Noisy Signal', color='r')
plt.title('Noisy Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot FIR filtered signal
plt.subplot(3, 1, 2)
plt.plot(t, filtered_signal_fir, label='FIR Filtered Signal', color='g')
plt.title('FIR Filtered Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot IIR filtered signal
plt.subplot(3, 1, 3)
plt.plot(t, filtered_signal_iir, label='IIR Filtered Signal', color='b')
plt.title('IIR Filtered Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
