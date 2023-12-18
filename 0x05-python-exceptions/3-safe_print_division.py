#!/usr/bin/python3
def safe_print_division(a, b):
    '''
    :param a::param b:You can assume that a and b are integers
    :return:Returns the value of the division, otherwise: None
    '''

    try:
        res = a/b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
