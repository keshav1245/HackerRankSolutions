# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
k,m = list(map(int,input().split()))

mat = []

for i in range(k):
    mat.append(list(map(lambda x: int(x)*int(x),input().split()[1:])))

all_combo = list(product(*mat))
def func(nums):
    return sum(x for x in nums) % m

print(max(list(map(func, all_combo))))
