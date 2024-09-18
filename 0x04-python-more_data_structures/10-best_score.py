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

    if not isinstance(a_dictionary, dict) or not a_dictionary:
        return None

    return max(a_dictionary, key=a_dictionary.get, default=None)
