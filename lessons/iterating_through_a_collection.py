"""Example of looping through all characters in a str."""

user_string: str = input("Give me a string! ")

# The variable i is a common counter variable name
# in programming. i is short for iteration/iterator.
i: int = 0

while i < len(user_string):
    print(user_string[i])
    i = i + 1

# select with mouse and press tab to indent, shift tab to unident
print("Done!")