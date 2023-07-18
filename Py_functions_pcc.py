def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello {username.title()} !")


greet_user("vinoth")


# Multiple Function Calls
# we can call the same function as many times as we want
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("hasmter", "harry ")
describe_pet("cat", "milo")

# Key word arguments , for a function the order should not be changed for variables , but if you want to change the order for variables
# then you can assign the value to the variable when calling the function
describe_pet(animal_type="hamster", pet_name="harry")

# Default Values
"""
When writing default values , you dont have to call the variable , the python will retrive the default value if the variable is not called

"""


def describe_pet(
    pet_name, animal_type="dog"
):  # Here animal_type = 'dog' is a default value
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name="willie")


# Return values


def get_formatted(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted("vinoth", "kumar")
print(musician)


# making an argument optional

"""
If one of the variable is not given then print the rest of the variable
"""


def get_formatted(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted("vinoth", "Dhandapani")
print(musician)


# returning a dictionary
def build_person(first_name, last_name):
    person = {
        "first": first_name,
        "last": last_name,
    }  # creats a dictionary under person
    return person


musician = build_person("vinoth", "kumar")
print(musician)


# using a function with a while loop
# this functionn is used in the below while loop
def get_formatted(first_name, last_name):
    """_summary_
    Return a full string
    Args:
        first_name (_type_): _description_
        last_name (_type_): _description_
    """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# this is an infinite loop and also it takes the input from the above function
while True:
    print('\nPlease tell me your name:')
    f_name = input('First name: ')
    l_name = input('Last name: ')

    formatted_name = get_formatted(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

    
# now to break the loop we can use a break statement
def get_formatted(first_name, last_name):
    """_summary_
    Return a full string
    Args:
        first_name (_type_): _description_
        last_name (_type_): _description_
    """
    full_name = f"{first_name} {last_name}"
    return full_name.title()
"""
So, in order for the loop to break and exit, both conditions (f_name == 'q' and l_name == 'q') need to be true simultaneously.
"""
while True:
    print('\nPlease tell me your name:')
    print("(enter 'q' at any time to quit)")
    f_name = input('First name: ')
    l_name = input('Last name: ')

    if f_name == 'q':
        break
    if l_name == 'q':
        break

    formatted_name = get_formatted(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
