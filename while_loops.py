"""
the while loop runs as long as, or 
while, a certain condition is true

"""

# print number from 1 to 5 using while
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)


# setting flags in the python.
# Basically flags is similar to fame where the levelis finshed or a game is over after an condition is met
# during this time , you code will loop or work until you type quit (While loop concept)
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)


# Break Statment
# You can use the break statement in any of Python’s loops

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")


# using continue in the loop

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        # if the number matches the condition , then the loop stops , so continue function exexutes the loop
        continue

    print(current_number)


# Moving Items from One List to Another
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# Removing All Instances of Specific Values from a List
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)

# Filling a Dictionary with User Input

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response  # adds the name and response to the empty dictonary

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

print(responses)
