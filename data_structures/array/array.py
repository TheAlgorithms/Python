"""
Python does not have built-in support for Arrays, but Python Lists can be used instead.
"""

names = ["conor", "tyson", "tony", "joe"]

# Get the length of the array
x = len(names)
print(x)

# Append a new element
names.append("Honda")

# Delete the second element
names.pop(1)


# Print the array
for n in names:
  print(n)
