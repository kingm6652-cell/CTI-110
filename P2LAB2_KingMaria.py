# Maria King
# 10/5/25
# P2LAB2
# write a code using dictonary to store values and display output.

# Create dictionary with automobile MPG values
CarModels = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

# Get all keys from the dictionary
keys = CarModels.keys()

# Print the keys
print('Available vehicles:', list(keys))

# Prompt user to enter a vehicle
vehicle = input('Enter a vehicle from the list above: ')

# Display the mpg for the selected vehicle
if vehicle in CarModels:
    mpg = CarModels[vehicle]
    print(f'MPG for {vehicle}: {mpg}')
    # Prompt for miles to drive
    miles = float(input('Enter the number of miles you will drive: '))
    # Calculate gallons needed
    gallons_needed = miles / mpg
    print(f'Gallons of gas needed: {gallons_needed:.2f}')
else:
    print('Vehicle not found. Please enter the name exactly as shown.')

