# Let's say that we have to classes, one called Dog and another called Cat

class Dog:
    def walk(self):
        print("I'm walking")


class Cat:
    def walk(self):
        print("I'm walking")

# Note that each class has a method called walk, this is a bad to our code,
# because if we have an error about a method in one of the classes,
# we will have to fix it in both classes

# To solve this problem, we can use inheritance