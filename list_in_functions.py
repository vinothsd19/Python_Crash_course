# passing a list in the function:
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello {name.title()} !"
        print(msg)

usernames = ["hannah", "ty", "margot"]
greet_users(usernames)


# Modify a list using using a function
# here we are using 2 functions , one for printing the model and another for showing the completed model
# we are using while loop to print the model and append the model to the completed model list
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

"""_summary_
    inorder to prevent a function from modifying a list, we can pass a copy of the list to the function
    instead of the original list "unprinted_design" we can pass the copy of the list "unprinted_design[:]"
    this will pass the copy of the list to the function and the original list will be unchanged """


# passing an Arbitrary number of arguments
"""you wont know ahead of time how many arguments a function 
needs to accept. Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement"""

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


# we can pass the toppings in a loop 

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}") # to print the toppings in a list format we can use a for loop

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

# mixing positional and arbitrary arguments
def make_pizza1(size, *toppings): 
    # here size is a positional argument and toppings is a arbitrary argument
    # so the first argument will be assigned to size and the rest of the arguments will be assigned to toppings
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza1(16, "pepperoni")
make_pizza1(12, "mushrooms", "green peppers", "extra cheese")

# Using Arbitrary Keyword Arguments
"""Sometimes you’ll want to accept an arbitrary number of arguments, but you 
won’t know ahead of time what kind of information will be passed to the 
function. In this case, you can write functions that accept as many key-value 
pairs as the calling statement provides"""

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info # this will return the dictionary

user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)


