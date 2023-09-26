# userinfo = {'name': 'BananaMann',
#             'job': 'Assassin',
#             'gender': ' Male'}

# # Calling the values using a key like this
# print(userinfo['name'])
# print(userinfo['job'])
# print("Your character is " + userinfo['name'] + " the job is " + userinfo['job'])



# for i in userinfo.keys():
#     print(i)


# for x in userinfo.values():
#     print(x)


# for k,v in userinfo.items():
#     print("Key: " + k + ", Value: " + v)
    
# groceries = {'apples': 10, 'orange': 21, 'grapes': 44}

# # print('There are ' + str(groceries.get('orange',0)) + "pcs of orange")

# groceries['apples'] = 12
# groceries['bananas'] = 16
# print(groceries)



# spam = {'name': 'Pooka', 'age': 5}
# if 'color' not in spam:
#     spam['color'] = 'black'

# message = "aa bb cc e f g"
# letter = {}

# for character in message:
#    letter.setdefault(character, 0) # letter.setdefault('a', 0) return 0
#    letter[character] = letter[character] + 1 

# print(letter)

spam = {'bar': 100}
print(spam['foo'])