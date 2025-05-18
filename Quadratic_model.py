from scipy.optimize import curve_fit
import numpy as np

# Data from Table \ref{tab:expanded_data}
x = data[:, 0]  # temperatures
y = data[:, 1]  # humidities
T = data[:, 2]  # actual times

# Define quadratic model
def quadratic(xy, a, b, c, d, e, f):
    x, y = xy
    return a*x**2 + b*y**2 + c*x*y + d*x + e*y + f

# Fit model
coeffs, _ = curve_fit(quadratic, (x, y), T, p0=[0, 0, 0, 0, 0, 0])
