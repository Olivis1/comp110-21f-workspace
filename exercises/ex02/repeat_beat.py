"""Repeating a beat in a loop."""

__author__ = "730530311"

# python -m exercises.ex02.repeat_beat
# Begin your solution here...

# from typing import Sequence


beat: str = str(input("What beat do you want me to repeat?" + " "))
repeat: int = int(input("How many times do you want me to repeat it? "))

if repeat <= 0:
    print("No beat...")

while repeat >= 1:
    if repeat == 1:
        print(beat)

    else:
        if repeat == 2:
            print(beat + " " + beat)

        else:
            if repeat == 3:
                print(beat + " " + beat + " " + beat)

            else:
                if repeat == 4:
                    print(beat + " " + beat + " " + beat + " " + beat)
    repeat = repeat - repeat
        
    