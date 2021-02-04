#MySolution
K = int(input())
r_list = input().split()

vals = {}

for i in r_list:
    if i in vals:
        vals[i] += 1
    else:
        vals[i] = 1
        
for k,v in vals.items():
    if v == 1:
        print(int(k))
        break
        
#optimal solution in discusions
#k,arr = int(input()),list(map(int, input().split()))
#myset = set(arr)
#print(((sum(myset)*k)-(sum(arr)))//(k-1))
