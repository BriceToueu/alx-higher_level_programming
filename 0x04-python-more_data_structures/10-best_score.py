#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value
    ...

    Parameters
    ----------
    a_dictionary : dictionary
        the given dictionary

    Return:
        If no score found, return None
        Key with biggest integer value otherwise
    """

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    fin = list(a_dictionary.keys())[0]
    grand = a_dictionary[fin]

    for l, t in a_dictionary.items():
        if t > grand:
            grand = t
            fin = l

    return (fin)
