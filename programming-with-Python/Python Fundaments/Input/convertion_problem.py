# Ask a user their weight (in pounds) and height (in inches)
# and convert to kilograms and meters, respectively, then print
# the user's weight and height

# Solution

weight_lb = float(input('Enter your weight in pounds: '))
height_inch = float(input('Enter your height in inches: '))

# Convert weight from pounds to kilograms
weight_kg = weight_lb * 0.45

# Convert height from inches to meters
height_m = height_inch * 0.0254

# Print the user's weight and height
print('Your weight is', weight_kg, 'kilograms')
print('Your height is', height_m, 'meters')