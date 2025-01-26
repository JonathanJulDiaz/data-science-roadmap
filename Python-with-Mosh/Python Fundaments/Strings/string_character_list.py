# A string is a list of characters,
# so we can access each character of the string using its index,
# and if we want to access a specific group of characters,
# we can use slicing
course = 'Python for Beginners'

# Here is how we can use slicing to access a specific group of characters
print(course[0:3]) # This will print from the first character of the string, to the 4th character of the string

# We can also use slicing from -1 to -length to access the last characters of the string
print(course[-2:-1]) # This will print from the second last character of the string to the last character of the string

# Another way to use slicing is to specify from where to start, and
# leave the end empty to get to the end of the string
print(course[0:])

# It works at the end too
print(course[:5]) # This will print from the first character of the string to the 6th character of the string

# You can also try it out with negative numbers
print(course[-5:])

# If you leave blank both start and end, it will print the whole string
print(course[:])