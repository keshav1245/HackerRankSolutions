# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from collections import deque
num_tests = int(input())

for _ in range(num_tests):
    num_cubes = int(input())
    # list_cubes = list(map(int,input().split()))
    list_cubes = input().split()
    previous = math.inf
    while(list_cubes != []):
        if len(list_cubes) == 1:
            if int(list_cubes[0]) <= previous:
                previous = int(list_cubes.pop(0))
            else:
                print("No")
                break
        else:
            if int(list_cubes[0]) <= previous and int(list_cubes[-1]) <= previous:
                if int(list_cubes[0]) >= int(list_cubes[-1]):
                    previous = int(list_cubes.pop(0))
                else:
                    previous = int(list_cubes.pop(-1))            
            elif int(list_cubes[0]) <= previous:
                previous = int(list_cubes.pop(0))
                
            elif int(list_cubes[-1]) <= previous:
                previous = int(list_cubes.pop(-1))
                
            else:
                print("No")
                break
    if len(list_cubes) == 0:
        print("Yes")
