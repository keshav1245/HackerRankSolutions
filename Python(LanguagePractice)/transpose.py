'''
Task

You are given a NXM integer array matrix with space separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.

Input Format

The first line contains the space separated values of N and M.
The next  lines contains the space separated elements of M columns.

Output Format

First, print the transpose array and then print the flatten.
'''

import numpy

n,m = input().split()
arr = []
for _ in range(int(n)):
    arr.append(list(map(int,input().split())))
    
mat = numpy.array(arr)
print(numpy.transpose(mat))
print(mat.flatten())

