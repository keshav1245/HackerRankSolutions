# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
elements = set(map(int,input().split()))
n_other = int(input())

for _ in range(n_other):
    c,n = input().split()
    ele = set(map(int,input().split()))
    getattr(elements,c)(ele if int(n) > 0 else set([]))
else:
    print(sum(elements))
