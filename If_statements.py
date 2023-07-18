cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if len(car) == 3:
        print(car.upper())
    else:
        print(car.title())


# Checking for Inequality

requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the Anchovies")


# numerical comparison
answer = 17
if answer != 42:
    print("This is not the correct answer")


requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings)

# Checking Whether a Value Is Not in a List
banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response")


# simple if statements

age = 19
if age >= 18:
    print("you are old enough to vote")
    print("\n Do you have license?")

# if Else condition
age = 17
if age >= 18:
    print("you are old enough to vote")
    print("Do you have license?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


# comparing 2 different lists
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for toppings in requested_toppings:
    if toppings in available_toppings:
        print(f"Adding {toppings}")
    else:
        print(f"sorry we don't have {toppings}")
print("\nplease take your pizza")
