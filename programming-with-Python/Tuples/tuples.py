# The tuples are like lists, but they are immutable
# they are used to store multiple items in a single variable that we don't want to change

names = ("John", "Bob", "Mosh", "Sarah", "Mary")

# Let's see the methods that we can use with tuples
print(names.count("John")) # This will print the number of times the name John appears in the tuple

print(names.index("Bob")) # This will print the index of the name Bob in the tuple

# You can access to every element from the tuple just like the lists:
print(names[0]) # This will print the first element in the tuple