# Write a program to find the largest number in a list

# Solution

numbers = [1, 2, 3, 4, 5]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number


print(largest)