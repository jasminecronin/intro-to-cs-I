# Chapter 20, exercise 1

# Prints a frequency table of unique letters from an input                         

import sys

lettercounts = {}

for line in sys.stdin.readlines() :
    lowercase = line.lower()
    for letter in lowercase :
        if letter.isalpha() :
            lettercounts[letter] = lettercounts.get(letter, 0) + 1
        
for key in sorted(lettercounts.keys()) :
    print( key, lettercounts[key] )
        
    
