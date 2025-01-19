# Nested loops are loops inside a loop
# We can use a for loop inside a for loop, a for loop inside a while loop,
# a while loop inside a for loop, a while loop inside a while loop

# We use them when we want to repeat a block of code inside another block of code

# For example, if we want to generate a coordinates from a 2D plane
# We can use a for loop inside a for loop
for x in range(5):
    for y in range(5): # Note how we must put the for loop inside the for loop
        print(f"({x}, {y})") # This will print the coordinates