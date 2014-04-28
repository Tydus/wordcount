#!/usr/bin/python

import sys
from operator import itemgetter

def main():
    t = {}
    for i in sys.stdin:
        i = i.strip().lower()
        if not t.has_key(i):
            t[i] = 0
        t[i] += 1

    print sorted(t.items(), key = itemgetter(0))

if __name__ == "__main__":
    main()

