'''
Task

You are given two integer arrays of size NXP and MXP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.

Input Format

The first line contains space separated integers N,M  and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

Output Format

Print the concatenated array of size (N+M)XP.
'''

import numpy

n,m,p = input().split()
arr1 = []
arr2 = []
for _ in range(int(n)):
    arr1.append(list(map(int,input().split())))

for _ in range(int(m)):
    arr2.append(list(map(int,input().split())))

num1 = numpy.array(arr1)
num2 = numpy.array(arr2)

print(numpy.concatenate((num1,num2),axis=0))
