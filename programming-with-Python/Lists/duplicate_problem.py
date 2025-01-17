# You have to delete the duplicates from a list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solution

unique_list = [] # We created an empty list

for number in list: # We use a for loop to iterate through the list

    if number not in unique_list: # We check if the number is not in the unique list
        unique_list.append(number) # We add the number to the unique list

print(unique_list)