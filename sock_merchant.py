#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # if there's only one sock, you can't sell a pair

    # increment a counter every time we make a pair / hit even
    sock_count = set()
    num_pairs = 0

    for sock_color in ar:

        if sock_color in sock_count:
            num_pairs += 1
            sock_count.remove(sock_color)

        else:
            sock_count.add(sock_color)

    return num_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
