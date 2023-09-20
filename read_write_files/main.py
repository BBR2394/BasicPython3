#! /usr/bin/env python3
# ci desss on a le shebang a tiliser

import sys

def openFile(filename):
    fd = open(filename, "r")
    text = fd.read()
    print(text)

def main(av):
    print("here we work")
    print(av)
    if (len(av) > 1 ):
        openFile(av[1])

if __name__ == '__main__':
    main(sys.argv)
