"""
Your name, Date
basics.py
Describe what this script will do?
"""
# the first section is used to import the modules and libraries
import math
import sys


# define your functions here
def myfunction(x, y):
    """
    This function will just add x and y
    """
    return x + y


def mycalculation(x, y):
    """
    This function will do some crazy caluclation.
    """
    return math.log(myfunction(x, y)) ** y


if __name__ == "__main__":
    print('You are running {script}'.format(script=sys.argv[0]))
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(mycalculation(a, b))
