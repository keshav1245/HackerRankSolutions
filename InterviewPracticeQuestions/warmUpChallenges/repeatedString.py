
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    los = len(s)
    if los == 0:
        return 0
    elif los == 1:
        if s == 'a':
            return n
        else:
            return 0
    elif los >= n:
        return s[:n].count("a")    
    elif s.find('a') == -1:
        return 0
    else:
        num_a_in_s = s.count('a')
        s_to_be_rep_completely, chars_left = divmod(n,los)
        return (num_a_in_s * s_to_be_rep_completely) + s[:chars_left].count("a")
        
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

