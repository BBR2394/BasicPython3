#! /usr/bin/env python3

import sys
from tkinter import *
from tkinter import ttk

def main(av):
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
    return 0

# ci dessous l'appel a faire si on n'utilise pas le fichier script comme une bibliotheque (library)
if __name__ == '__main__':
    main(sys.argv)