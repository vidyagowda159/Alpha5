def squares(list_):
    res = []
    for i in list_:
        res.append(i ** 2)
    return res

s = squares([1, 2, 3, 4, 5])
#print(s)

##############################################

def add(a, b):
    print( a + b)


#add(1, 2)       # 3
#print(add(1, 2))    # 3, None

#################################################

def add(a, b):
    c = a + b
    return c


#add(1, 2)       # nothing will be printed
#print(add(1, 2))    # 3


##################################################

def spam():
    return 1, "hai", True, [1, 2, 3]

#print(spam())

####################################################

# types of arguments

# positional arguments
def greet(name, age):
    print(f"My name is {name} and I am {age} years old")


#greet("John", 18)
#greet(18, "John")
print()

# keyword arguments

#greet(name="John", age=18)
#greet(age=18, name="John")
print()

###########################################################
# combination positional and keyword arguments

#greet("John", age=18)
#greet(name="John", 18) -> syntaxError
print()

########################################################
# positional only arguments

def greet(name, age, /):
    print(f"My name is {name} and I am {age} years old")


#greet("John", 20)
# greet(name="John", age=18)   TypeError 


def greet(name, /, age):
    print(f"My name is {name} and I am {age} years old")


#greet("steve", 23)
#greet("steve", age=23)
#greet(name="steve", age=23) # TypeError

###############################################################
# keyword only arguments

def greet(*, name, age):
    print(f"My name is {name} and I am {age} years old")


#greet("john", 23)   # TypeError

#greet(name="steve", age=23)

################################################################
# combination of positional only and keyword only arguments

def greet(name,/,*, age):
    print(f"My name is {name} and I am {age} years old")


#greet("steve", age=20)


######################################################
# variable number of positional arguments

def function1(*args):# packing
    print(args)
    print(*args)        # 1 2 3 "hello"


#function1(1, 2, 3, "hello") # (1, 2, 3, "hello")
#function1(1)                # (1, )
#function1()                 # ()

# variable number of keyword arguments
def function1(**kwargs): # packing
    print(kwargs)               # {'a': 1, 'b': 2, 'c': 3}      
    print(*kwargs)              # a b c
    print(**kwargs)             # TypeError


#function1(a=1, b=2, c=3)

##########################################################
# default parameter
    
def add(a, b, c=0):
    print(a + b + c)


#add(1, 2)       # 3
#add(1, 2, 3)    # 6



##############################################################
# function annotations

def add(a:int, b:int, c:int) -> list:
    print(a + b + c)



#print(add(1, 2, 3))   # 6
#add("hai", "hello", "world")

################ Variable scopes ############################################

# global scope variables

a = 1
b = 2

def add():
    global a
    a = a + b
    return a


#print(a)
#print(add())
#print(a)


# local scope variables


def spam():
    a = 2

    def wrapper():
        nonlocal a
        a = a + 10
        print(a)

    wrapper()

#spam()

#########################################################################



























    














