# create a class called dog
class Dog():
    """A simple attempt to model a dog."""
    # here we use the __init__() method
    # the __init__() method runs automatically whenever we create a new instance based on the Dog class
    # here the instances are name and age
    # so when we want to access the class , we can call it by the instance name eh., my_dog.name or my_dog.age
    def __init__(self, name, age):
       self.name = name
       self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6) # since you have passed the arguments here. you can call the instances directly using my_dog.name or my_dog.age
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nMy dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()
