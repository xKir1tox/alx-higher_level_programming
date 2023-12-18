#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''
    :param my_list:
    my_list can contain any type (integer, string, etc.)
    :param x:
    x represents the number of elements to access in my_list
    x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
    :return:
    Returns the real number of integers printed
    '''
    store = 0
    for i in range(0,x):
        try:
            print("{:d}".format(my_list[i]), end="")
            store += 1
        except(ValueError, TypeError):
            continue
    print("")
    return(store)
