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

# And we can also define explicit arguments passed to the function
print_hello(30, name="John")

# But note that we can't pass them in the wrong order,
# always must pass the positional arguments first

#print_hello(age = 30, "John") this will give an error