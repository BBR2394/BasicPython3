#! /usr/bin/env python3
# ci desss on a le shebang a tiliser

import sys
import json

def openFile(filename):
    fd = open(filename, "r")
    text = fd.read()
    print(text)

def start(av):
    print("here we work")
    print(av)
    if (len(av) > 1 ):
        openFile(av[1])

def main(av):
    xjsonData =  '[{ "name":"John", "age":30, "city":"New York"}, { "name":"titi", "age":24, "city":"Los Angeles"}]'
    res = json.loads(xjsonData)
    print(res[1]['name'])

if __name__ == '__main__':
    main(sys.argv)
