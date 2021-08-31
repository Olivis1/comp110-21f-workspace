"""Relational Operators Task."""

__author__: str = "730530311"

left: str = str(input("Left-hand side:"))
right: str = str(input("Right-hand side:"))
left_bool: bool = bool(left)
right_bool: bool = bool(right)
arrow: bool = bool(left_bool < right_bool)
arrow_str: str = str(arrow)
at_least: bool = bool(left_bool >= right_bool)
at_least_str: str = str(at_least)
equal: bool = bool(left_bool == right_bool)
equal_str: str = str(equal)
not_equal: bool = bool(left_bool != right_bool)
not_equal_str: str = str(not_equal)

print(left + " < " + right + " is " + arrow_str)
print(left + " >= " + right + " is " + at_least_str)
print(left + " == " + right + " is " + equal_str)
print(left + " != " + right + " is " + not_equal_str)