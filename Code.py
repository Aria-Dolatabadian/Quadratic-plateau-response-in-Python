import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Read data into Python
data = pd.read_csv('data.csv')

# Define Quadratic-Plateau model function
def quadratic_plateau(x, a, b, c, d):
    return np.where(x < c, a * x**2 + b * x, d)

# Fit the model to the data
popt, pcov = curve_fit(quadratic_plateau, data['x'], data['y'])

# Predictions using the fitted model
y_pred = quadratic_plateau(data['x'], *popt)

# Visualize the results
plt.figure(figsize=(10, 6))
plt.scatter(data['x'], data['y'], label='Original Data')
plt.plot(data['x'], y_pred, color='red', label='Fitted Quadratic-Plateau Model')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Quadratic-Plateau Response Analysis')
plt.legend()
plt.grid(True)
plt.show()
