#!/bin/python3

def sort_athlete(arr,k):
    vals = sorted([(ind,row[k]) for ind, row in enumerate(arr)],key=lambda x: x[1])
    for v in vals:
        print(*arr[v[0]])
    
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    sort_athlete(arr,k)
