import os
import sys
def func():
    print(os.getcwd())
    print(sys.argv[0])
    print(__file__)
func()