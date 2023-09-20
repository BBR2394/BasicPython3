#! /usr/bin/env python3
# ci desss on a le shebang a tiliser

import sys

def main(av):
    print("here we work")

# ci dessous l'appel a faire si on n'utilise pas le fichier script comme une bibliotheque (library)
if __name__ == '__main__':
    main(sys.argv)
