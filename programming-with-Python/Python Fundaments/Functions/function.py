# In programming is very common to use the same code over and over again
# we can use functions to do that, which is very useful

# For example, if we want to print a message many times we can use a function
# to do that

# To create a function we use the def keyword and the function name,
# which usually starts with a lowercase letter, and in case that we want
# to use more than one word, we use underscores to separate them

# The function name must be unique, so we can't use the same name for two functions
# and finally we can use the () with a : to pass arguments to the function, which are optional
def print_hello():
    print("Hello")

# Note that all the code with an indentation after the function definition
# will be executed when the function is called, so you must be careful
# when defining functions

# Now we can call the function
print_hello()

# Something relevant to consider is that a function can't be called
# before it is defined

# For example, if we try to call the function before it is defined
# we will get an error

#print_test() # Here we are trying to call the function before it is defined

def print_test():
    print("Test")

