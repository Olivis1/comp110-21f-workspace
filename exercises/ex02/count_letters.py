"""Counting letters in a string."""

__author__ = "730530311"

# from typing import Sequence
# Begin your solution here...
# python -m exercises.ex02.count_letters
letter: str = str(input("What letter do you want to search for?: "))
word: str = str(input("Enter a word: "))
i: int = 0
count: int = int(word * len(letter))


while i < len(word):
    print(word[i])
    i = i + 1
  