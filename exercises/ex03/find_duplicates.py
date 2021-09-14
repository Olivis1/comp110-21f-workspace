"""Finding duplicate letters in a word."""

__author__ = "730530311"

word: str = str(input("Enter a word: "))
dup: bool = False
yup: bool = True
i: int = 0

while i < len(word):
    j: int = i + 1
    l: str = word[i]
    # variable to hold the character at i
    while j < len(word):
        if i or j == l:
            print(yup)
        else:
            if i or j != l:
                print(dup)
        j += 1
    i += 1