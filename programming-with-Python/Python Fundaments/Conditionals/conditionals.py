# Now considering the conditions in the file condition.txt
# we will simulate this rules using Python

# First we must initialize the boolean variables is_hot and is_cold
is_hot = True
is_cold = False

# Now we have to use the conditional if, which is used to execute a block of code indenteded after it
# if the boolean variable next to it is true
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")

# Also exists elif, which works the same way as if, but it is used to check another boolean variable 
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")

# Finally, else, which is used to execute a block of code indenteded after it
# if all the previous conditions are false
else:
    print("It's a lovely day")