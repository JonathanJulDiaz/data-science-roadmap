# Type conversion
# Let's convert a string to an integer

# The input() function returns a string
birth_year = input("Birth year: ")

# Let's print the type of the variable
print(type(birth_year)) # It will print a <class 'str'> which means it is a string

# Now that we know the type is a string, we must convert the string to
# an integer to do numeric operations.
# To do this, we use the int() function to convert the string to an integer
age = 2025 - int(birth_year)

# And print the result
print(age) # It will print a number

# Also exists float() and bool() functions to convert