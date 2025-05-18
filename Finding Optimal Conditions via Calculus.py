from scipy.optimize import minimize
import numpy as np

# Define models
def linear(xy):
    x, y = xy
    return -1.23*x - 0.85*y + 145.67

def quadratic(xy):
    x, y = xy
    return 0.0251*x**2 + 0.0592*y**2 - 0.0398*x*y - 2.8134*x - 6.5123*y + 415.72

def exponential(xy):
    x, y = xy
    return 150.23 * np.exp(0.0124*x - 0.0456*y) + 45.78

# Find minimum time for each model
bounds = [(16, 30), (40, 92)]
x0 = [27, 92]
linear_result = minimize(linear, x0, bounds=bounds)
quad_result = minimize(quadratic, x0, bounds=bounds)
exp_result = minimize(exponential, x0, bounds=bounds)
