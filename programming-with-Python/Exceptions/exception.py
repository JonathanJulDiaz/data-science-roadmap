# When we execute our code the first time, it usually doesn't work,
# it give us an error, and we need to fix it

# For example, if we try to divide by zero, we will get an error
print(10 / 0)

# But we can catch the error and handle it, using the try and except keywords

# First we must put the block of code inside of try:
try:
    print(10 / 0)

# Then we define which type of error we want to catch
except ZeroDivisionError: # In this case we want to catch a ZeroDivisionError
    
    # Finally if the error we want to catch is raised, we can print a message
    print("You can't divide by zero")