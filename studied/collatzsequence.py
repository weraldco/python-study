
def collatz(givenNumber):
    # If even then print number // 2
    # If odd then print 3 * number + 1
    
    if (int(givenNumber) % 2) == 0:
        return (int(givenNumber) // 2)

    elif (int(givenNumber) % 2) == 1:
        return (3 * int(givenNumber) + 1)


try:
    print("Enter a number: ")
    givenNumber = int(input())


    while True:
        if(givenNumber == 1):
            break
        else:
            if(collatz(givenNumber) == 1):
                print(collatz(givenNumber))
                break
                
            elif(collatz(givenNumber != 1)):
                print(collatz(givenNumber))
                givenNumber = collatz(givenNumber)
except ValueError:
    print("You need to type integer!")