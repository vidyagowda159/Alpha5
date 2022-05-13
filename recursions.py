# print "hello" for 3 times
def greet(count = 0):
    if count == 3:
        return

    print("hello")
    count += 1
    greet(count)

#greet()

###############################################
# recursion program to print numbers from 1-10

def count_(number=1):
    if number > 10:
        return

    print(number)
    number += 1
    count_(number)

#count_()

##################################################
# factorial of a number

def factorial(n, fact=1, i=1):

    if i > n:
        return fact

    fact *= i
    i += 1
    return factorial(n, fact, i)

print(factorial(5))





















    
