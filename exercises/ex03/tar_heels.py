"""An exercise in remainders and boolean logic."""

__author__ = "730530311"


a: int = int(input("Enter an int: "))

b: int = int(a % 2)
c: int = int(a % 7)
d: int = int(c + b)
i: int = 1
# python -m exercises.ex03.tar_heels

while i >= 1:
    if d == 0:
        print("TAR HEELS")
    else:
        if b == 0:
            print("TAR")
        else:
            if c == 0:
                print("HEELS")
            else:
                if d >= 2:
                    print("CAROLINA")
    i = i - i