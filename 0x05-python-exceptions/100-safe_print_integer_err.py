#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e.args[0]))
        return False
    else:
        return True