"""Drawing forests in a loop."""

__author__ = "730530311"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: str = input("DEPTH: ")
dep: int = int(depth)
T: str = TREE

if dep == 0:
    dep = dep - 1


while dep >= 1:
    if dep == 1:
        print(TREE)
    else:
        if dep == 2:
            print(TREE)
            print(T * 2)
        else:
            if dep == 3:
                print(TREE)
                print(T * 2)
                print(T * 3)
            else:
                if dep == 4:
                    print(TREE)
                    print(T * 2)
                    print(T * 3)
                    print(T * 4)
                else:
                    if dep == 5:
                        print(TREE)
                        print(T * 2)
                        print(T * 3)
                        print(T * 4)
                        print(T * 5)
                    else:
                        if dep == 6:
                            print(TREE)
                            print(T * 2)
                            print(T * 3)
                            print(T * 4)
                            print(T * 5)
                            print(T * 6)
                        else:
                            if dep == 7:
                                print(TREE)
                                print(T * 2)
                                print(T * 3)
                                print(T * 4)
                                print(T * 5)
                                print(T * 6)
                                print(T * 7)
                            else:
                                if dep == 8:
                                    print(TREE)
                                    print(T * 2)
                                    print(T * 3)
                                    print(T * 4)
                                    print(T * 5)
                                    print(T * 6)
                                    print(T * 7)
                                    print(T * 8)
                                else:
                                    if dep == 9:
                                        print(TREE)
                                        print(T * 2)
                                        print(T * 3)
                                        print(T * 4)
                                        print(T * 5)
                                        print(T * 6)
                                        print(T * 7)
                                        print(T * 8)
                                        print(T * 9)
                                    else:
                                        if dep == 10:
                                            print(TREE)
                                            print(T * 2)
                                            print(T * 3)
                                            print(T * 4)
                                            print(T * 5)
                                            print(T * 6)
                                            print(T * 7)
                                            print(T * 8)
                                            print(T * 9)
                                            print(T * 10)
                                                                                                                              
    dep = dep - dep
