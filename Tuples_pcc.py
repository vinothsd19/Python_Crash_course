# tuples are prepresented by brackets
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


# using loop in dimensions
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# Writing over a tuple:
# the only way to change the tuple is to assign the variable to different values
dimensions = (200, 50)
print("Original Dimensions")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified Dimensions")
for dimension in dimensions:
    print(dimension)
