#!/usr/bin/python3
def no_c(my_string):
    no_c = my_string.translate({ord(i): None for i in 'cC'})
    return no_c
