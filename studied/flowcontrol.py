## if statement

# name = input("Whats your name? ")
# age = int(input("How old are you? "))
# # AND
# if age >= 1 and age < 18:
#     print("You're a minor")
# else:
#     print("You're not a minor anymore!")



## elif


# print("Enter your average  grade this sem: ")
# grade = int(input())

# if grade >= 75 and grade <= 80:
#     print("Average!")
# elif grade >= 81 and grade <= 85:
#     print("Excellent!")
# elif grade >= 86 and grade <= 90:
#     print("Magnificent!")
# elif grade >= 91 and grade <= 100:
#     print("Great job, you did so well!")
# else:
#     print("You have failed this semester..")



## While loop


# while True: 
#     print("Enter you username: ")
#     username = input()
#     if username != "werald":
#         continue
#     while True:
#         print("Hello Werald, can you enter your password? ")
#         password = input()
#         if password == "wewe":
#             break
#     break

# print("Access granted!")


## For loop
# total = 0
# for i in range(101):
#     total = total + i

#     print( str(i) + " : " + str(total))

# print (total)
import random

for i in range(0, 10):
    print(random.randint(0,100))