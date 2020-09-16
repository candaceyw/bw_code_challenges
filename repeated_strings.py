#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # I know how many times 'a' appears in s
    num_as_in_s = 0
    for char in s:
        if char == 'a':
            num_as_in_s += 1

    # I know the length of s, so I can figure out how many times s in repeated in the subtring
    full_repetitions_of_s = n // len(s)

    # multiply the number of times s is repeated * the number of times a appears in s
    remainder_length = n % len(s)
    num_as_in_remainder = 0
    remainder_string = s[0:remainder_length]
    for char in remainder_string:
        if char == "a":
            num_as_in_remainder += 1
    num_as_in_substring = full_repetitions_of_s * num_as_in_s + num_as_in_remainder
    # i need to handle the "remainder" that's left over
    return num_as_in_substring

    # Brute Force:
    # substring = ""
    # while len(substring) < n:
    #     substring += s
    # substring = substring[0:n] # chop off extra letters on substring so it's n characters long
    # print(len(substring), substring)

    # num_as = 0
    # for char in substring:
    #     if char == "a":
    #         num_as += 1

    # return num_as

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
