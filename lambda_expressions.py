# lambda expressions/ Anonymous functions


def last_digit(num):
    return num % 10


res = last_digit(432)   # print(last_digit(432))
# print(res)



last_digit = lambda num: num % 10
res = last_digit(60123) # print(last_digit(60123)
# print(res)


# lambda expression to return square of a number


squares = lambda num: num ** 2
print(squares(5))


# lambda expression to return last element of any seq

last_ = lambda sequence: sequence[-1]
print(last_("hello"))


# lambda expression to return last n elements of any seq

last_n = lambda seq, n: seq[-n:]
print(last_n("hai hello", 3))


# lambda expression to check if the given number is even or odd

even_odd = lambda num: f"{num} is even" if num % 2 == 0 else f"{num} is odd"
print(even_odd(4))


# lambda expression to return square and cube of a number

sq_cube = lambda num: (num ** 2, num ** 3)
print(sq_cube(4))

# lambda expression to check if the given string is palindrome or not

palindrome = lambda string: string == string[::-1]
print(palindrome("mommy"))


# ****************** map() *****************************

# write a program to create a list of square numbers of the
# numbers in the list
l = [1, 2, 3, 4, 5]
res = []

sq = lambda num: num ** 2

"""
for i in l:
    square = sq(i)
    res.append(square)

print(res)
"""

res = map(sq, l)
print(list(res))

# write a program to check if the numbers are even or odd in the given list using map


l = list(range(10))


even_odd = lambda num: "even" if num % 2 == 0 else "odd"
res = map(even_odd, l)
print(list(res))

even_odd = lambda num: num % 2 == 0
res = map(even_odd, l)
print(list(res))


# check if the string is palindrome or not in the given list

list_ = ["madam", "dad", "hello", "google", "level"]

palindrome = lambda s: s == s[::-1]
print(list(map(palindrome, list_)))


# to convert the strings to upper case
list_ = ["madam", "dad", "hello", "google", "level"]

upper_ = lambda word: word.upper()
print(list(map(upper_, list_)))

# or
print(list(map(str.upper, list_)))

# to swap case of the words in the given sentence
sentence = "This IS a BunCh of WORDS"
words = sentence.split()

res = list(map(str.swapcase, words))
print(" ".join(res))
#print(list(map(str.swapcase, sentence.split())))


# to convert the negative numbers into positive in the list

numbers = [-9, 2, 5, -4, 8, -2, 7, -12]
print(list(map(abs, numbers)))

# to return the pair of word and its length in the sentence
sentence = "This IS a BunCh of WORDS"

words = sentence.split()

# normal function
def word_len(word):
    return word, len(word)

# lambda function
word_len_pair = lambda word: (word, len(word))

print(list(map(word_len, words))) 
#print(list(map(word_len_pair, words)))

# to add the elements of two lists

l1 = [1, 2, 3, 4]
l2 = [9, 5, 4, 6]


def add_(num):
    return num[0] + num[1]

add_ = lambda num: num[0] + num[1]

map(add_, zip(l1, l2))
# [(1, 9), (2, 5), (3, 4), (4, 6)]


def add_(n1, n2):
    return n1 + n2

add_ = lambda n1, n2: n1 + n2

print(list(map(add_, l1, l2)))

# to raise the elements of the list to the power of their indices

numbers = [3, 6, 2, 7, 8]


# enumerate class

def power_(value):
    index, ele = value
    return ele ** index
    
lambda value: value[1] ** value[0]
map(power_, enumerate(numbers))
#[(0, 3), (1, 6), (2, 2), (3, 7), (4, 8)]


def power(value, index):
    return value ** index

lambda value, index: value ** index
print(list(map(power, numbers, range(len(numbers)))))
print()
print()

################### filter() ###################################

# extract only even numbers from the given list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def even_(num):
    if num % 2 == 0:
        return num ** 2


print(list(map(even_, numbers)))
print(list(filter(even_, numbers)))

##########################################################

# extract the names which have length > 4

names = ["greg", "steve", "bob", "alexa"]

def check_len(string):
    return len(string) > 4


print(list(filter(check_len, names)))


# Build a list with only even length strings using filter class
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram']

def even_len(string):
    return len(string) % 2 == 0


even = lambda string: len(string) % 2 == 0

print(list(filter(even_len, names)))

# Return the string if the string is starting with a vowel character"
names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']

vowels = lambda string: string[0].lower() in "aeiou"

print(list(filter(vowels, names)))


# Program to return only positive values in the list using filter class
numbers = [-2, -1, 0, 1, 2]

pos = lambda num: num > 0
print(list(filter(pos, numbers)))


















































































































