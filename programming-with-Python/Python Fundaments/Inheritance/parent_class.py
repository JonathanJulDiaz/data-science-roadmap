# So let's create a parent class named Mammal
class Mammal:
    def walk(self):
        print("I'm walking")

# Now let's create a child class named Dog and another called Cat
class Dog(Mammal):
    def bark(self): # Here we define a method exclusive to the Dog class
        print("Bark!")

# In the case of the Cat class, we don't want to do anything, so is basically empty
# and equal to the Mammal class
class Cat(Mammal):
    pass # We write pass because we don't want to do anything in the child class

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()