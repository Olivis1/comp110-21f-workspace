"""Numeric Operator Task."""

__author__: str = "730530311"

left: str = str(input("Left-hand side:"))
right: str = str(input("Right-hand side:"))
stars: str = "** "

print((left + stars + right) + "is " + (int(left ** right)))
print(right / left)
print(right // left)
print(right % left)
