# Excercise 1: Rewrite your pay computation to give the employee 1.5 times
#       the hourly rate for hours worked above 40 hours
try:
    # Hours employee works
    workhours = float(input("Enter hour of work: "))

    # Rate per hour
    workrates = float(input("Enter work rate: "))


    if workhours > 40:

        extrahour = workhours - 40
        extrapay = extrahour * workrates/2

        salary = (workhours * workrates) + extrapay
        
    else:
        salary = workhours * workrates
        
    print("Pay: " + str(salary))
except ValueError:
    print('Error: You must enter a number.')