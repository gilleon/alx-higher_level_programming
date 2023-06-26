#!/usr/bin/python3
from __future__ import print_function
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
    except BaseException as e:
        result = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return
