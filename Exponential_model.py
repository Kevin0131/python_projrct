from scipy.optimize import curve_fit
import numpy as np

# Data from Table \ref{tab:expanded_data}
x = data[:, 0]  # temperatures
y = data[:, 1]  # humidities
T = data[:, 2]  # actual times

# Define exponential model
def exponential(xy, a, b, c, d):
    x, y = xy
    return a * np.exp(b*x + c*y) + d

# Fit model
coeffs, _ = curve_fit(exponential, (x, y), T, p0=[1, 0, 0, 0])
