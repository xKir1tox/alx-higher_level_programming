#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''
    :param my_list:
    the main list to print
    :param x:
    store the values in my_list
    :return:
    elements numbers
    '''
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return ret
