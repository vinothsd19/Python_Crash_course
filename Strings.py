# Changing Case in a String with Methods
name = "vinoth kumar dhandapani"
print(name.title())  # capitalize the first letter of first name and last name
print(name.upper())
print(name.lower())


# Combining or Concatenating Strings
first_name = "Vinoth Kumar"
last_name = "Dhandapani"
full_name = f"{first_name} {last_name}"
print(full_name)
print("Hello, " + full_name.title() + "!")
print(f"Hello, {full_name.title()}!")

## Removing space
favorite_language = " Python"
favorite_language = favorite_language.lstrip()  # Strips space in left side
favorite_language = favorite_language.rstrip()  # Strips space in right side
favorite_language = favorite_language.strip()  # Strips space on both side
print(favorite_language)


# inorder to print the text in next line use \n and for tab use \t , note \n\t is the right format when you want to enter the text with intendation
print("Languages:\n\tPython\n\tJava")


# Removing Prefixes
nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix("https://"))
