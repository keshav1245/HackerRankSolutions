def minion_game(string):
    # your code goes here
    
    l = len(string)
    
    kevin = 0
    stuart = 0
    vow = ['A','E','I','O','U']
    
    for i in range(l):
        if string[i] in vow:
            kevin += (l-i)
        else:
            stuart += (l-i)
    
    if kevin == stuart:
        print("Draw")
    elif kevin > stuart:
        print("Kevin {}".format(kevin))
    else:
        print("Stuart {}".format(stuart))
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
