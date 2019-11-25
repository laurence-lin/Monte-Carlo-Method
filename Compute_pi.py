import numpy as np
import random

# Monte Carlo used to estimate pi
# Assume I've a square with origin point (0, 0) with height 1, and a circle with radius 1 with same origin point inside the square.
# Sample N times in the square, Assume I've M points in the circle, then I got

iteration = 5000
x = random.uniform(-1, 1)
print(x)

circle = 0
for i in range(iteration):
  x = np.random.uniform(-1, 1)
  y = np.random.uniform(-1, 1)
  if (x**2 + y**2)**(1/2) <= 1:
     circle += 1
  
pi = 4*circle/iteration
print('Estimate pi:', pi)
