#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the whatFlavors function below.
def whatFlavors(cost, money,n):
    i = 0
    while cost != []:
        e = cost.pop(0)
        try:
           ind = cost.index(money-e)
           print("{} {}".format(i+1,ind+(i+1)+1))
           break
        except:
            i += 1     
            
def whatFlavors(cost, money,n):
    c_dict = {}
    
    for ind,val in enumerate(cost):
        if str(val) not in c_dict.keys():
            c_dict[str(val)] = ind
        
    k = c_dict.keys()
    for c in cost:
        if str(money-c) in k:
            print("{} {}".format(c_dict[str(c)]+1,c_dict[str(money-c)]+1))
            break
            
def whatFlavors(cost, money,n):
    h = {}
    for i, num in enumerate(cost):
        n = money - num
        if n not in h:
            h[num] = i
        else:
            print(h[n]+1, i+1)
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money,n)
