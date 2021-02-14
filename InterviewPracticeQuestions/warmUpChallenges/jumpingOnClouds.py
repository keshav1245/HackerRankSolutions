import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c,n):
    jumps = 0
    i = 0
    
    while i != n-1:
        if i+2 <= n-1 and c[i+2] == 0:
            jumps += 1
            i += 2
        elif i+1 <= n-1 and c[i+1] == 0:
            jumps += 1
            i += 1
    else:
        return jumps  
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c,n)

    fptr.write(str(result) + '\n')

    fptr.close()

