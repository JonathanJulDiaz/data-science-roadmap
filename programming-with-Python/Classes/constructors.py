# So we have tha class Person, which has a method talk
# class Person:
#     def talk(self):
#         print("I'm talking")

# But this class have a problem, every person must have a name
# but the class Person doesn't have a name atribute

# To solve this problem, we can add a constructor to the class Person
class Person:
    def __init__(self, name):
        self.name = name
        print("I'm created!")

    def talk(self):
        print(f"I'm {self.name}")

# Now, when we create a new person, we can pass the name to the constructor
person = Person("John Doe")
person.talk()