# Among the several modules that Python have,
# random is one of the most useful
# This module is used to generate random numbers

import random

random_number = random.random() # This will generate a random number between 0 and 1

print(random_number)

random_int = random.randint(1, 10) # This will generate a random number between 1 and 10

print(random_int)

# We can use this to choose randomly between many options
options = ["rock", "paper", "scissors"]
random_option = random.choice(options) # This will generate a random option from the list

print(random_option)