alien_0 = {"color": "green", "points": 5}
# inroder to access the dict value , we need to pass the item in square brackets
# print(alien_0['color'])

# we can assign the value to a variable:
new_points = alien_0["points"]
# print(f"you earned {new_points} points!")

# we can add new items to the dict list just like pandas
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# inorder to modidy the existing values in a dictionary
alien_0["color"] = "yellow"

print(alien_0)

# using conditions in dicts
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original Position: {alien_0['x_position']}")

# add posistion based on speed
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment

print(f"New Position {alien_0['x_position']}")


# removing a key value pair from the dict list
alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["color"]  # just use del  before the item =
print(alien_0)


# Dictionary for similar objects:
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}")

# get option is used to check if the item or value is present in the list
alien_0 = {"color": "green", "speed": "slow"}
point_value = alien_0.get("points", "no value assigned")
# The get() method requires a key as a first argument. As a second optional
# argument, you can pass the value to be returned if the key doesn’t exist
print(point_value)


# Looping through the dictionary

user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

for key, value in user_0.items():
    # inorder to unpack the dict use ".items()"
    print(f"\nkey: {key}")
    print(f"value: {value}")


favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}")


# to loop just the keys we need to use "keys()" in the for statement
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for name in favorite_languages.keys():
    print(name.title())

#  getting the value by lopping the key.
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
friends = ["phil", "sarah"]

for name in favorite_languages.keys():
    print(f"Hi {name.title()}!")
    if name in friends:
        language = favorite_languages[name].title()
        # in-order to access the value of a key in loop , use for loop to get the key of dict and assign it to a variable
        print(f"\t{name.title()}, I see you love {language.title()}")

# Looping Through a Dictionary’s Keys in a Particular Order
# use sorted() after the variable in for loop

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the pole")

#  getting the value by lopping the value.
# to loop just the keys we need to use "keys()" in the for statement
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# inroder to remove the duplicatres use set function
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

print("The following languages have been mentioned:")
for language in sorted(set(favorite_languages.values())):
    print(language.title())


# Nesting
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

# adding all the dicts to the list
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# Make a emplty list and add them
aliens = []

# make 30 aliens with same specs
for alien in range(30):  # creates 30 aleins
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# pythoon considers each dict and each value as an object and we can change the value
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10


for alien in aliens[:5]:
    print(alien)
print(".....")

print(len(aliens))

# list in a dictionary :

pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

# Order summarize
print(f"You ordered a {pizza['crust']}-crust pizza " "with the following toppings:")

for topping in pizza["toppings"]:
    print(f"\t{topping.title()}")

# to print all the values in the list within a dictionary , you can loop the value as well

favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorute languages are")
    for language in languages:
        print(f"\t{language.title()}")


# A Dictionary in a Dictionary
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username.title()}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
