from pathlib import Path

path = Path("filesandexceptions/pi_digits.txt")
# contents = path.read_text()
# contents = contents.rstrip() # remove the extra blank line

#also the above line can be written as 
contents = path.read_text()

lines = contents.splitlines()
#for line in lines:
#    print(line)

#print(contents)


# to convert mutiple lines into single line
pi_string = ""
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))