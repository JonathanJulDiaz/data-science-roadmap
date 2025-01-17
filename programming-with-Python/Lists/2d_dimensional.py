# Imagine a 2d matrix that has 3 rows and 3 columns
# | 1 2 3 |
# | 4 5 6 |
# | 7 8 9 |
# We can represent that matrix in Python using 2d lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Now we can access the elements of a 2d list using the index of the row and the index of the column
# For example, to access the element at row 1 and column 2 we can use
print(matrix[1][2]) # This will print 2 in this case

# You can change the elements inside the 2d list too
matrix[1][2] = 20
print(matrix[1][2]) # This will print 20

# If we want to print every single element inside the 2d list,
# we can use a nested for loop
for row in matrix:
    for element in row:
        print(element)