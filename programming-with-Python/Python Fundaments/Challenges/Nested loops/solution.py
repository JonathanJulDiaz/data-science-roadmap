# See this code if you want to compare this solution with yours
xTimes = [5,2,5,2,5]

# Solution
for x in xTimes: # We use a for loop to iterate through the list
    result = "" # Create a variable to store the result

    for y in range(x): # We use a for loop to iterate through the range of the current value of x
        result += "X" # Add "X" to the result
    
    print(result) # Print the result