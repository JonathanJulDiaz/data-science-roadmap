# Python and many programming languages have loops, which are used to repeat a block of code
# until a certain condition is met

# While loop

i = 0
while i < 10: # In this loop we will print the variable i while it is less than 10
    print(i) # First we print the value of i
    i += 1 # Then we add 1 to the value of i
# In that way we will print the numbers from 0 to 9

# For loop

for i in range(10): # The for loop is used to repeat a block of code a certain number of times
    print(i)
# And every time that the loop is repeated, the value of i will be increased by 1 automatically

# We must have careful when using loops because if we don't set the range,
# the loop will run forever the same block of code, and we don't want that

# Sometimes we want to repeat a block of code until inside the block code we have a condition
# that is true, that is when we use break, which will break the loop

# Example

i = 0
while i < 10:
    print(i)
    if i == 5:
        break # This will break the loop when the value of i is 5
    i += 1