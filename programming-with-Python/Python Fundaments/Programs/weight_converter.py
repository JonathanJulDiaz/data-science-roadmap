# We will create a weight converter

# Ask the user if they want to convert from kilograms to pounds or vice versa
conversion_type = input("Enter 'kg' to convert from kilograms to pounds or 'lb' to vice versa: ")

# If they want to convert from kilograms to pounds
if conversion_type.lower() == 'kg': # lower() is used to convert the input to lowercase, so it is not case sensitive
    # We must convert the string input to a float first, because input() returns a string
    weight_kg = float(input("Enter your weight in kilograms: "))
    weight_lb = weight_kg * 2.2 # 2.2 is the conversion factor from kilograms to pounds
    # And print the result
    print(f"Your weight is {weight_lb} pounds")

# If they want to convert from pounds to kilograms
elif conversion_type.lower() == 'lb':
    weight_lb = float(input("Enter your weight in pounds: "))
    weight_kg = weight_lb / 2.2 # In this case we divide by the conversion factor from pounds to kilograms
    print(f"Your weight is {weight_kg} kilograms")
# If they enter an invalid input
else:
    print("Invalid input")