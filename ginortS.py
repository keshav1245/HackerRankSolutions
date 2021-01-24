s = input()
low = ""
up = ""
dig_o = ""
dig_e = ""
for c in s:
    if c.islower():
        low += c
    elif c.isupper():
        up += c 
    elif c.isdigit():
        if int(c) % 2 == 0:
            dig_e += c
        else:
            dig_o += c
        
else:
    print("".join(sorted(low))+"".join(sorted(up))+"".join(sorted(dig_o))+"".join(sorted(dig_e)) )


# Better Method :

#import string
#order = string.ascii_letters+"1357902468"
#print(*(sorted(input(),key=order.index)),sep="" )
