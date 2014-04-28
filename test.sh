#!/bin/bash

ppmd d -s enwik8-ascii.pmd

time (./wordcount.py         < enwik8-ascii.txt > /dev/null)
time (./wordcount-shipped.py < enwik8-ascii.txt > /dev/null)

rm enwik8-ascii.txt
