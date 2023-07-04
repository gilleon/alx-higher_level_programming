#!/usr/bin/python3
"""text indentation module"""


def text_indentation(text):
    """funtion with one parameter parsed
    Args:
        text: The str ingtext
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for specialChar in ".?:":
        # print(specialChar, text.split(specialChar))
        text = (specialChar + "\n\n").join(
            [line.strip(" ") for line in text.split(specialChar)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
