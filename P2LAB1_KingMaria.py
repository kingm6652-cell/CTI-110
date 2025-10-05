# Maria King
#10/5/25
#P2LAB1
# Preforms mathmatical equations and displays information.

import math

# Get radius from user
radius = float(input('what is the radius of the circle: '))

# Calculate values
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display results with formatting
print(f'Diameter: {diameter:.1f}')
print(f'Circumference: {circumference:.2f}')
print(f'Area: {area:.3f}')

