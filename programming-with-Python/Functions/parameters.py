# Parameters are variables that are passed to a function
# When we call a function, we pass arguments to the function

# For example, if we want to print a message with a name
# we can use a parameter to pass the name to the function
def print_hello(name):
    print(f"Hello, {name}")

print_hello("John") # This will print Hello, John

# We can define as much parameters as we want

# For example, if we want to print a message with a name and an age
# we can use two parameters to pass the name and the age to the function
def print_hello(name, age):
    print(f"Hello, {name}. You are {age} years old.")


# We can use the function to return a value,
# to do that we use the return keyword before the value
def add(x, y):
    return x + y # Here we return the sum of x and y