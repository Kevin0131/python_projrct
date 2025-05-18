from scipy.optimize import curve_fit
import numpy as np

# Data from Table \ref{tab:expanded_data}
x = data[:, 0]  # temperatures
y = data[:, 1]  # humidities
T = data[:, 2]  # actual times

# Define linear model
def linear(xy, a, b, c):
    x, y = xy
    return a*x + b*y + c

# Fit model
coeffs, _ = curve_fit(linear, (x, y), T, p0=[0, 0, 0])
