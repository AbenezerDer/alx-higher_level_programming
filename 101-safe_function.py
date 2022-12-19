#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        x = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e.args[0]))
        return None
    else:
        return x