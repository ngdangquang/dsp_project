# Theory of FIR and IIR Filters

## 1. FIR Filters (Finite Impulse Response)
### Overview:
FIR filters are characterized by a finite number of filter taps or coefficients. They are called "non-recursive" filters because they do not use feedback, meaning the output depends only on the current and past input values.

### Design Methods:
FIR filters are typically designed using windowing methods, where the filter coefficients are computed by taking the inverse Fourier transform of the desired frequency response and applying a window function (e.g., Hamming, Hanning, Blackman-Harris, etc.) to reduce sidelobes.

#### Windowing Method:
1. **Ideal Filter Response**: Define the ideal frequency response based on the cutoff frequency.
2. **Inverse Fourier Transform**: Take the inverse Fourier transform of the ideal filter response to get the impulse response.
3. **Windowing**: Apply a window function (e.g., Hamming or Hanning) to the impulse response to reduce side lobes and improve performance.

### Advantages:
- Stable and easy to implement.
- Linear phase response, which makes them suitable for applications requiring minimal phase distortion.

### Disadvantages:
- Requires a higher number of coefficients (larger order) for sharp cutoff frequencies.

## 2. IIR Filters (Infinite Impulse Response)
### Overview:
IIR filters are recursive filters that use feedback. The output depends on both the current and previous input values, as well as the previous output values.

### Design Methods:
IIR filters can be designed using various methods, including:
- **Butterworth Filter**: Provides a flat frequency response in the passband.
- **Chebyshev Filters**: Provide a steeper roll-off than Butterworth filters but allow ripple in either the passband or the stopband.

#### Chebyshev Type I Filter Design:
- The filter coefficients are designed to achieve a desired level of ripple in the passband while ensuring that the stopband attenuation meets the specified requirements.

### Advantages:
- More efficient than FIR filters for achieving a sharp cutoff.
- Requires fewer coefficients for the same performance compared to FIR.

### Disadvantages:
- Potential for instability if not designed properly.
- Non-linear phase response, which can cause phase distortion in some applications.

## Conclusion:
FIR filters are simple, stable, and suitable for applications requiring linear phase response, while IIR filters are more computationally efficient and suitable for applications that can tolerate phase distortion. The choice between FIR and IIR depends on the specific requirements of the application.
