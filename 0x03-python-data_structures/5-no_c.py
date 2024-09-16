#!/usr/bin/python3
def no_c(my_string):
    """Function that removes all characters c and C from a string."""
    length = len(my_string)
    l = 0
    new_string = my_string[:]

    for index in range(length):
        if (my_string[index] == 'c' or my_string[index] == 'C'):
            new_string = new_string[:(index - l)] + my_string[(index + 1):]
            l += 1

    return (new_string)
