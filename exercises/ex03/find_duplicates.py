"""Finding duplicate letters in a word."""

__author__ = "730530311"

word: str = str(input("Enter a word: "))
dup: bool = False
i: int = 0

while i < len(word):
    j: int = i + 1
    l: str = word[i]
    # variable to hold the character at i
    while j < len(word):
        if word[i] and word[j] == l:
            dup = True
            j = j + 1
        else:
            j = j + 1       
    i += 1

print(dup)