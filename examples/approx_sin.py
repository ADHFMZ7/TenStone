import numpy as np
import matplotlib.pyplot as plt

# Train and Test datasets

X_Train = np.arange(-2 * np.pi, 2 * np.pi, (4 * np.pi) / 1000)
Y_Train = np.sin(X_Train)

print(X_Train, Y_Train)
