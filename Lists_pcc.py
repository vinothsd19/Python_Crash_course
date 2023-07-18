# best practice is to keep the list names as plurals
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0])  # print 1st element in list
print(bicycles[0].title())  # capitalize the first letter

# modify the list values
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles[0] = "ducati"
# print(motorcycles)

# adding the name to the list
motorcycles.append("honda")
print(motorcycles)

# create a empty list and append the values
motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
# print(motorcycles)


# inserting an element to this list
motorcycles.insert(0, "ducati")


# remove an element from the list
del motorcycles[0]
print(motorcycles)

# removing an element using pop
# pop removes the last element in this list
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# inorder to pop any element instead of last element use index
first_owned = motorcycles.pop(1)
print(f"The {first_owned.title()} is not better than Royal Enfield")


# Organizing a list
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()  # sort the list
cars.sort(reverse=True)  # reverse sort the list
print(cars)

# to sort a list temporarily use "sorted"
cars = ["bmw", "audi", "toyota", "subaru"]

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print(len(cars))


# Looping through the list:
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician.title())


# we can print a complete line with loop
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was great")
    # the "\n" in the line creates a empty next line so there is gap between the sentences
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Any line that are printed outside the loop will be executed once , after the loop is completed
print("Thank you, everyone. That was a great magic show!")
# if the line is intended then the above line also prints along the loop


# Range function
for value in range(1, 5):
    print(value)

# to print the range in list
numbers = list(range(1, 6))
print(numbers)

# print the even numbers in the range
even_numbers = list(range(2, 11, 2))
print(even_numbers)

numbers = []
for number in range(1, 11):
    if number % 2 == 0:
        numbers.append(number)

print(numbers)


# Simple statistics with list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehensions
squares = [value**2 for value in range(1, 11)]
# here the sqaure bracket indicates it a list and for is used for loop , do not use colon
print(squares)


# Slicing a list
players = ["charles", "martina", "michael", "florence", "eli"]
players.sort()
print(players[:4])


# Looping Through a Slice
players = ["charles", "martina", "michael", "florence", "eli"]
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


# Copying a list
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
my_foods.append("cannoli")
friend_foods.append("ice cream")
# [:] selects all the elemets in the list and adds them to another variable
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
