#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    final = 0
    val = 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for ret in reversed(roman_string):
        val = dict[ret]
        final += val if final < val * 5 else -val
    return final
