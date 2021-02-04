#!/bin/python3

import math
import os
import random
import re
import sys

data = {}

if __name__ == '__main__':
    s = input()
    for c in s:
        if c in data.keys():
            data[c] += 1
        else:
            data[c] = 1
    
    sort_data =  sorted(data.items(), key=lambda kv:(-kv[1], kv[0]))
    for (k,v) in sort_data[:3]:
        print(k+" "+str(v))
