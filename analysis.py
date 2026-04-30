import os
import sys


def analyze(data):
    result = os.path.join(sys.argv[0], str(data))
    return result  
