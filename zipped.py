N,x = input().split()
marks = []
for i in range(int(x)):
    marks += list(map(float,input().split()))

for i in range(int(N)):
    print("{:.1f}".format(sum(marks[i::int(N)]) / int(x) ))
