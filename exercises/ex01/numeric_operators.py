"""Numeric Operator Task."""

__author__: str = "730530311"

left: str = str(input("Left-hand side:"))
right: str = str(input("Right-hand side:"))
left_int: int = int(left)
right_int: int = int(right) 
exponent: int = int(left_int ** right_int)
exponent_str: str = str(exponent)
slash: float = float(left_int / right_int)
slash_str: str = str(slash)
two_slash: int = int(left_int // right_int)
two_slash_str: str = str(two_slash)
percent: int = int(left_int % right_int)
percent_str: str = str(percent)

print(left + " ** " + right + " is " + exponent_str)
print(left + " / " + right + " is " + slash_str)
print(left + " // " + right + " is " + two_slash_str)
print(left + " % " + right + " is " + percent_str)