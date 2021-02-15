
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):    
    bribes = 0
    
    Q = [k-1 for k in q]
    
    for i,v in enumerate(Q):
        if v - i > 2:
            print("Too chaotic")
            break
        
        for j in range(max(v-1,0),i):
            if Q[j] > v:
                bribes += 1
    else:
        print(bribes)
    
    

# def minimumBribes(q):
#     n = len(q)
#     Q = [k-1 for k in q]
#     bribe = 0
    
#     pos_val = {i:i for i in range(n) }
#     # print(pos_val)
    
#     for i in range(n):
#         if pos_val[i] == Q[i]:
#             continue
#         elif Q[i] - i > 0:
#             actual = Q[i]
#             diff = Q[i] - i
#             if diff > 2:
#                 print("Too chaotic")
#                 break
#             else:
#                 for j in range(diff):
#                     pos_val[actual-j] , pos_val[actual- j - 1] =  pos_val[actual- j - 1],pos_val[actual-j] 
#                 bribe += diff
#         else:
#             diff = abs(Q[i] - i)
#             actual = i + diff
#             if actual > n-1:
#                 continue
#             for j in range(diff):
#                     pos_val[actual-j] , pos_val[actual- j - 1] =  pos_val[actual- j - 1],pos_val[actual-j] 
#             bribe += diff
#     else:
#         print(str(bribe))
            
                    
    
            

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

