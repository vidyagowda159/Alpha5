# function to return dictionary with character and its ascii value pair

def char_ascii(string):
    d = {char: ord(char) for char in string}
    return d


# print(char_ascii("hello"))

# ********************************************
# function to return length of the iterable 

def len_(iterable):
    count = 0
    for _ in iterable:
        count += 1

    return count

#print(len_("hello world"))

# ***********************************************
# Write a program to search for a character in a given string and return the corresponding index.

# using inbuilt method


def linear_search(sequence, value):
    return sequence.index(value)


# without using inbuilt method

def linear_search(seq, value):

    for index, item in enumerate(seq):
        if value == item:
            return f"{value} is present in position {index}"

    else:
        return f"{value} is not present in {seq}"


#print(linear_search("hello", "z"))
            
#************************************************************

# Write a function to count the number of positional and keyword arguments passed to it.

def sample(*args, **kwargs):
    print(len(args))
    print(len(kwargs))


#sample(1, 2, 3, 4, a=10, b=20, c=30)

# ***********************************************************
# Write a function to print message “Hai Everyone” if the user input is not present and if the user input is present print the user input.

def greet(msg="hai everyone"):
    print(msg)


#greet()
#greet("Good morning")

# *******************************************************
#  Write a function that returns the last digit of an integer

def last_digit(num):
    return num % 10


# print(last_digit(123))

# ************************************************************
# Make a function named tail that takes a sequence (like a list, string, or tuple) and a
# number n and returns the last n elements from the given sequence, as a list.

def tail(sequence, n):
    return list(sequence[-n:])


# print(tail("hello", 2))

# ************************************************************
# Function to check if a given number is Fibonacci number


def fib(number):
    a = 0
    b = 1
    
    while a <= number:
        if a == number:
            return f"{number} is a fibonacci number"
        
        c = a + b
        a, b = b, c
        

    else:
        return f"{number} is not a fibonacci number"

#print(fib(19))
            
    
        




































