n = int(input())
s = set(map(int, input().split()))
n_com = int(input())
for _ in range(n_com):
    c_a = input().split()
    if len(c_a)>1:
        getattr(s,c_a[0])(*[int(c_a[1])])
    else:
        getattr(s,c_a[0])(*[])
else:
    print(sum(s))
