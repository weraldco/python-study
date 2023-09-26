#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.


l1 =[2,4,3]
l2 = [5,6,4]
#Output: [8,9,9,9,0,0,0,1]

def addTwoNumbers(l1,l2):
    def reverselist(l):
        l.reverse()
        stringlist =""
        for i in range(len(l)):
            stringlist += str(l[i])

        return int(stringlist)
    
    l1 = reverselist(l1)
    l2 = reverselist(l2)

    total = l1 + l2
    total = str(total)
    newlist = [total[i] for i in range(len(total))]
    newlist.reverse()

    return newlist

print(addTwoNumbers(l1,l2))