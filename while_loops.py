"""
# even numbers from 1 - 10
start = 1
end = 10


while start <= end:
    if start % 2 == 0:
        print(start)

    start += 1

##############################################

# odd numbers from 1 - 10
start = 1
end = 10


while start <= end:
    if start % 2 == 1:
        print(start)

    start += 1

################################################

# numbers from -10 to -1

start = -10
end = -1

while start <= end:
    print(start)
    start += 1

################################################

# check if the givemn number is prime or not

number = 9
i = 2

while i < num:
    if num % i == 0:
        print("not prime")
        break
    i += 1

else:
    print('prime')

    

###################################################

# prime numbers from 1 to 10

num = 1

while num <= 10:
    if num > 1:
        i = 2
        while i <= num // 2:
            if num % i == 0:
                break
            i += 1
            
        else:
            print(num)
            
    num += 1



##########################################################

# fibonacci series from 0 to 10

a, b = 0, 1

while a <= 10:
    print(a)
    c = a + b
    a = b
    b = c


###########################################################

# fibonacci series upto 10 numbers

a = 0
b = 1
count = 0

while count <= 10:
    print(a)
    c = a + b
    a, b = b, c
    count += 1


###########################################################
# traversing through a sequence(str, list, tuple)

string = "hello world"
i = 0

while i < len(string):
    print(i, string[i])
    i += 1

""



















































    
