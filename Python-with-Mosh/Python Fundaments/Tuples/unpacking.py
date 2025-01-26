# Imagine that we have coordinates that we want to use in our code
# we can use a tuple to store the coordinates

coordinates = (1, 2, 3) # In this case let's say that the coordinates are (x, y, z)

# If we would use this coordinates in many places in our code
# we would have to use the following syntax
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

# But in Python we can use the following syntax to unpack
# the coordinates using the following syntax
x, y, z = coordinates

print(f"x: {x}, y: {y}, z: {z}")

# And we can use unpacking in lists too
list = [1, 2, 3, 4, 5]

first, second, third, *last = list

# Note that we can use * to unpack the rest of the list

print(f"First: {first}, Second: {second}, Third: {third}, Last: {last}")