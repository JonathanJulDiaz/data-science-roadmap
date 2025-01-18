# We saw the differents data structures in python, such as strings, lists, tuples, dictionaries.
# But in many cases, we need to code concepts more complicated.

# For example a person, a person has a name and an age, but also has a job and a salary,
# and things get a little more complex, that's where classes come into play.

# A class is a blueprint for creating objects, which are instances of the class.
# A class is defined using the class keyword, followed by the class name.

# For example, if we want to create a class called Person, we can do the following:
class Person: # Note that if a class name have more than one word, we use CamelCase
    
    # Now a person can talk, so we can create a method called talk
    def talk(self): # And note that if a method name have more than one word, we use snake_case
        print("I'm talking")


# Then if we want to create a person, we can do the following:
person = Person() # This will create a new instance of the Person class and store it in person variable

# And we can use the methods from the Person class
person.talk() # This will print "I'm talking"

# We also can add new atributes to the Person class
person.name = "John Doe" # This will add the name John Doe to the person object
print(person.name) # This will print John Doe

# And every new Person class instances, is a different object from each other

person2 = Person()

print(person2.name) # This will raise a error, because the object person2 doesn't have a name atribute