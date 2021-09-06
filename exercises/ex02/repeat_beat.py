"""Repeating a beat in a loop."""

__author__ = "730530311"

# python -m exercises.ex02.repeat_beat
# Begin your solution here...

from typing import Sequence


beat: str = str(input("What beat do you want me to repeat?" + " "))
repeat: int = int(input("How many times do you want me to repeat it? "))
beats: str = beat + " "
ya: int = len(beat)

if repeat <= 0:
    print("No beat...")

while repeat >= 1:
    print(ya + repeat)
    repeat = repeat - repeat
        
    