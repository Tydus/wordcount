#!/bin/bash

ppmd d -s enwik8-ascii.pmd

g++ -std=c++11 -O3 ./wordcount.cc -o ./wordcount-native

time (./wordcount.py         < enwik8-ascii.txt > /dev/null)
time (./wordcount-shipped.py < enwik8-ascii.txt > /dev/null)
time (./wordcount-native     < enwik8-ascii.txt > /dev/null)
