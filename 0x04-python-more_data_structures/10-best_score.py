#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxval = 0
    maxkey = None
    for keypair, val in a_dictionary.items():
        if val > maxval:
            maxval = val
            maxkey = keypair
    return maxkey
