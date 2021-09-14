"""Finding duplicate letters in a word."""

__author__ = "730530311"

word: str = str(input("Enter a word: "))
dup: bool = 1 > 2
yup: bool = 1 < 3
i: int = 0
while i < len(word):
    j: int = i + 1
    letter: str = word[i]
    # variable to hold the character at i
    while j < len(word):
        j == letter
        # print(word[j])
        j += 1
    i += 1