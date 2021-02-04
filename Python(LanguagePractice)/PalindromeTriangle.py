#The constrainsts were to not use str and more than 1 for loop and code should be at max 2 lines in side the for loop.
#The perfect solution for the same is the 3rd one, however the 1st two are another approaches that can be used to deal with the problem.

#Approach 1 
for i in range(1,int(input())+1):
    left = "".join(map(str,list(range(1,i))))
    print( left,str(i),left[::-1],sep="" )
    
#Approach 2
for i in range(1,int(input())+1):
    left = list(range(1,i))
    print( *left,i,*left[::-1],sep="" )
    
#Approach 3 - for hackerank solution 
for i in range(1,int(input())+1):
    print(((10**i-1)//9)**2)
