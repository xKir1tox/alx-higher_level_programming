#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_lest = []
    for i in range(len(my_list)):
        if my_list[i] == 0:
            new_lest.append(True)
        else:
            new_lest.append(False)
    return new_lest
