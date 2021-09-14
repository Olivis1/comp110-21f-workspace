"""Drawing forests in a loop."""

__author__ = "730530311"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: str = input("DEPTH: ")
dep: int = int(depth)

if dep == 0:
    dep = dep - 1


while dep >= 1:
    if dep == 1:
        print(TREE)
    else:
        if dep == 2:
            print(TREE)
            print(TREE + TREE)
        else:
            if dep == 3:
                print(TREE)
                print(TREE + TREE)
                print(TREE + TREE + TREE)
            else:
                if dep == 4:
                    print(TREE)
                    print(TREE + TREE)
                    print(TREE + TREE + TREE)
                    print(TREE + TREE + TREE + TREE)
                else:
                    if dep == 5:
                        print(TREE)
                        print(TREE + TREE)
                        print(TREE + TREE + TREE)
                        print(TREE + TREE + TREE + TREE)
                        print(TREE + TREE + TREE + TREE + TREE)
                    else:
                        if dep == 6:
                            print(TREE)
                            print(TREE + TREE)
                            print(TREE + TREE + TREE)
                            print(TREE + TREE + TREE + TREE)
                            print(TREE + TREE + TREE + TREE + TREE)
                            print(TREE + TREE + TREE + TREE + TREE + TREE)
                        else:
                            if dep == 7:
                                print(TREE)
                                print(TREE + TREE)
                                print(TREE + TREE + TREE)
                                print(TREE + TREE + TREE + TREE)
                                print(TREE + TREE + TREE + TREE + TREE)
                                print(TREE + TREE + TREE + TREE + TREE + TREE)
                                print(TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                            else:
                                if dep == 8:
                                    print(TREE)
                                    print(TREE + TREE)
                                    print(TREE + TREE + TREE)
                                    print(TREE + TREE + TREE + TREE)
                                    print(TREE + TREE + TREE + TREE + TREE)
                                    print(TREE + TREE + TREE + TREE + TREE + TREE)
                                    print(TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                    print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                else:
                                    if dep == 9:
                                        print(TREE)
                                        print(TREE + TREE)
                                        print(TREE + TREE + TREE)
                                        print(TREE + TREE + TREE + TREE)
                                        print(TREE + TREE + TREE + TREE + TREE)
                                        print(TREE + TREE + TREE + TREE + TREE + TREE)
                                        print(TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                        print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                        print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                    else:
                                        if dep == 10:
                                            print(TREE)
                                            print(TREE + TREE)
                                            print(TREE + TREE + TREE)
                                            print(TREE + TREE + TREE + TREE)
                                            print(TREE + TREE + TREE + TREE + TREE)
                                            print(TREE + TREE + TREE + TREE + TREE + TREE)
                                            print(TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                            print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                            print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                            print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                        else:
                                            if dep == 11:
                                                print(TREE)
                                                print(TREE + TREE)
                                                print(TREE + TREE + TREE)
                                                print(TREE + TREE + TREE + TREE)
                                                print(TREE + TREE + TREE + TREE + TREE)
                                                print(TREE + TREE + TREE + TREE + TREE + TREE)
                                                print(TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                                print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                                print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                                print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                                print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                            else:
                                                if dep == 12:
                                                    print(TREE)
                                                    print(TREE + TREE)
                                                    print(TREE + TREE + TREE)
                                                    print(TREE + TREE + TREE + TREE)
                                                    print(TREE + TREE + TREE + TREE + TREE)
                                                    print(TREE + TREE + TREE + TREE + TREE + TREE)
                                                    print(TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                                    print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                                    print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                                    print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                                    print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                                    print(TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE + TREE)
                                                
    dep = dep - dep
