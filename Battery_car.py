# inheritnace
# turning describe_battery() into a class method
class Car:
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        """"Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # this is the default value for the odometer_reading attribute

    def get_descriptive_name(self):
        """return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage): # in the above example we have directly modified the attribute value. but here we are using a method to modify the attribute value
        # def update_odometer(self,mileage): # this is the method used to update the odometer_reading attribute
        """set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self,battery_size= 40):
        self.battery_size = battery_size
        
    def describe_battery(self):
        """print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 40:
            range = 140
        elif self.battery_size == 65:
            range = 200
        print(f"This car can go about {range} miles on a full charge.")
    
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self,make,model,year): # here we are using the same instance variables as the parent class
        """initialize attributes of the parent class."""
        super().__init__(make,model,year) # super() function is used to import the parent class attributes to the child class
        self.battery = Battery() # this is the attribute specific to the child class

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()
