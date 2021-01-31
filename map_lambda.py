cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    
    lst = [0,1]
    for i in range(2,n):
        lst.append(lst[i-1]+lst[i-2])
    else:
        return lst[0:n]

if __name__ == '__main__':
