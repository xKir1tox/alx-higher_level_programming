#!/usr/bin/env python3
def no_c(my_string):
    c_remover = my_string.translate({ord(i): None for i in 'cC'})
    return c_remover
