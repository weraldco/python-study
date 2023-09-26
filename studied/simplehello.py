#Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is
#stored in spam, and prints Greetings! if anything else is stored in spam.

print("Put any number: ")
num = int(input())

if num == 1:
    print("Hello!")
elif num == 2:
    print("Howdy!")
else:
    print("Greetings!")

