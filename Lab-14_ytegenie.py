"""
Lab14_pcarswel_ytegenie_1.py
Author: Yalalem Tegenie
Purpose: Plot a spiral using math.sin() and math.cos() with 500 points.
Date: 2025-08-07
"""

import math
import matplotlib.pyplot as plt

# Create empty lists for x and y coordinates
x_values = []
y_values = []

# Generate points for the spiral
# Radius increases linearly, angle increases in radians
points = 500
for i in range(points):
    angle = math.radians(i * 5)  
    # Increase angle by 5 degrees converted to radians
    radius = 0.1 * i            
     # Radius increases by 0.1 units each step
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    x_values.append(x)
    y_values.append(y)

# Plot the spiral
plt.figure(figsize=(8, 8))
plt.plot(x_values, y_values, linewidth=2, color='blue')
plt.title('Spiral Plot Using math.sin() and math.cos()', color = 'green', fontsize = 24)
plt.xlabel('X axis', color = 'green', fontsize = 12)
plt.ylabel('Y axis', color = "green", fontsize= 12)
plt.axis('equal')  # Equal scaling for x and y axes
plt.grid(True)
plt.show()
print(plt.style())