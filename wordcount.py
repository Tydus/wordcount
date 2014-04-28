#!/usr/bin/python

import sys
import trie

def main():
    t = trie.Trie()
    for i in sys.stdin:
        t.insert(i.strip())

    print t

if __name__ == "__main__":
    main()

