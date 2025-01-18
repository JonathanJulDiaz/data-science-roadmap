# When working with big projects, we can use modules to separate the code into different files
# and import them into the main file

# For example, let's import the module conveter.py
import conveter

print(conveter.kg_to_lb(58.5))

# But we can also import specific functions from the module
from conveter import kg_to_lb

print(kg_to_lb(58.5))