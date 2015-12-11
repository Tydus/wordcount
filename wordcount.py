#!/usr/bin/env python2

import sys
import trie

def main():
    t = trie.Trie()
    for i in sys.stdin:
        t.insert(i.strip().lower())

    print t

if __name__ == "__main__":
    main()

