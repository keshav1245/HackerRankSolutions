#!/bin/python3

import os
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    c_all = Counter(ar)
    pairs = 0
    for color,num in c_all.items():
        pairs += num // 2
    else:
        return pairs
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
