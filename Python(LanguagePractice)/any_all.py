n, lst = int(input()),list(map(int,input().split()))
def checkint(x): return str(x) == (str(x))[::-1]
print(any(list(map(checkint,lst)))) if all(list(map(lambda x: x>=0,lst))) else print(False)
