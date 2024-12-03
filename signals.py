import numpy as np

def generate_signal(fs, duration=1.0, frequency=50.0, noise_level=0.5):
    """
    Generate a noisy signal composed of a sine wave with added Gaussian noise.
    
    Parameters:
    fs : float
        The sampling frequency (Hz)
    duration : float
        The duration of the signal in seconds (default is 1 second)
    frequency : float
        The frequency of the sine wave (Hz)
    noise_level : float
        The standard deviation of the Gaussian noise added to the signal
    
    Returns:
    t : numpy array
        The time array
    noisy_signal : numpy array
        The generated noisy signal
    """
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    sine_wave = np.sin(2 * np.pi * frequency * t)
    noisy_signal = sine_wave + noise_level * np.random.randn(len(t))
    return t, noisy_signal
