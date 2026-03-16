import numpy as np
import matplotlib.pyplot as plt

# Generate time points
t = np.linspace(0, 2 * np.pi, 100)  # 100 points from 0 to 2π

# Compute sine values
sine_values = np.sin(t)

# Create a plot
plt.figure(figsize=(10, 5))
plt.plot(t, sine_values, label='Sine Wave')
plt.title('Sine Wave from 0 to 2π')
plt.xlabel('Time (radians)')
plt.ylabel('Sine value')
plt.legend()
plt.grid(True)
plt.show()