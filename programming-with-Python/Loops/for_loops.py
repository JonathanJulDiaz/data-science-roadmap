# We mentioned before that we can use a for loop to iterate over a list,
# that list can be a list of numbers or a list of strings
my_numbers = [1, 2, 3, 4, 5]

for number in my_numbers: # Here we are using the for loop to iterate over the list my_numbers
    print(number) # And we are printing every number in the list

# Let's try out with a list of strings
my_names = ['John', 'Jane', 'Bob', 'Alice', 'Charlie']

for name in my_names: # Here we are using the for loop to iterate over the list my_names
    print(name) # And we are printing every name in the list

# There is a python function to doesn't have to create a list of numbers from 1 to 10 for example
# It's called range()
serie = range(1, 11) # Here we are creating a range of numbers from 1 to 10(because the last number is exclusive)

for number in serie:
    print(number)

# We can also put a step inside the range() function to make it go from 1 to 10 in steps of 2(for example)

for number in range(1, 11, 2):
    print(number) # This will print the numbers from 1 to 10 in steps of 2