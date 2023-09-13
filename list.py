# animals = ['dogs', 'cats','cows', 'rats', 'snakes']

# animals = animals + ['tiger']
# print(animals[:])

# List of cats

# 1 add a new of a cat 
# 2 input user
# 3 add the input user in list 
# 4 print the list 
# 5 loop back



# listOfCats = []


# while True:
    
#     print("Add name of your cat?: ")
#     newCat = input()
#     listOfCats = listOfCats + [newCat]

#     for name in listOfCats:
#         print('Name of your cats:')
#         print(name)


# groceries = ['orange', 'juice', 'apple', 'chicken','pasta','cereal']

# # for i in range(len(groceries)):
# #     print (str([i+1]) + " " + groceries[i])

# while True:
#     print('Type the item name to check if its in the cart?: ')
#     finditem = input()

#     if finditem in groceries:
#         print(finditem + ' is in the cart')
#     else:
#         print(finditem +" is not in the cart")


# player1 = ['Sinx', 'Assassin', '99',]

# name, job, level = player1

# print(name)

groceries = ['orange', 'juice', 'apple', 'chicken','pasta','cereal']

# for index, item in enumerate(groceries):
#     print(str(index + 1) + " " + item)

# ADDING NEW ITEM

# print(groceries)
# groceries.append('soda')

# groceries.insert(1,'rice')
# print(groceries)

# groceries.remove('pasta')
# print(groceries)

print(groceries)
groceries.sort(reverse=True)
print(groceries)
# groceries.reverse()
# print(groceries)