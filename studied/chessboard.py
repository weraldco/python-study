

hor = "abcdefgh"
ver = "12345678"
cheeseboard = {}

alphalist = [hor[i] for i in range(len(hor))]
numlist = [ver[i] for i in range(len(ver))]

numlist.reverse()

for x in range(len(numlist)):
    for n in range(len(alphalist)):
        cheeseboard[(alphalist[n] + numlist[x])] = " "
    
print(cheeseboard)
