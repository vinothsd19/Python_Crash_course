# # working with classes and instances

# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self,make,model,year):
#         """"Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_descriptive_name(self):
#         """return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
# my_new_car = Car('audi','a4',2019)
# print(my_new_car.get_descriptive_name())


# # setting a default value for an attribute

# # working with classes and instances

# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self,make,model,year):
#         """"Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 # this is the default value for the odometer_reading attribute

#     def get_descriptive_name(self):
#         """return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
    
# my_new_car = Car('audi','a4',2019)
# print(my_new_car.get_descriptive_name())
# # we can also modify attributes values directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()


# # modify the vaue of an attribute using a method

# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self,make,model,year):
#         """"Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 # this is the default value for the odometer_reading attribute

#     def get_descriptive_name(self):
#         """return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self,mileage): # in the above example we have directly modified the attribute value. but here we are using a method to modify the attribute value
#         # def update_odometer(self,mileage): # this is the method used to update the odometer_reading attribute
#         """set the odometer reading to the given value."""
#         self.odometer_reading = mileage
    
# my_new_car = Car('audi','a4',2019)
# print(my_new_car.get_descriptive_name())
# # we can also modify attributes values directly
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()


# incrementing an attribute's value through a method

# modify the vaue of an attribute using a method

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
    
# my_new_car = Car('subaru', 'outback', 2019)
# print(my_new_car.get_descriptive_name())
# # we can also modify attributes values directly
# my_new_car.update_odometer(23_500)
# my_new_car.read_odometer()

# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()