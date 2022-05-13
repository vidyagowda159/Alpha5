from collections import defaultdict

"""
# print elements in a sequence in reversed order

sequence = "hello"

# slicing
for ele in sequence[::-1]:
    print(ele, end="")
print()

# range()
for index in range(-1, -len(sequence)-1, -1):
    print(sequence[index], end="")
print()

# concatenation
res = ""
for ele in sequence:
    res =  ele + res

print(res)

# reversed() - inbuilt class

for ele in reversed(sequence):
    print(ele, end="")


# throw away variable
s = "hello world"
for _ in range(5):
    print(s)



# print index and element of an iterable

iterable = ["apple", "google", "walmart", "flipkart", "gmail"]


#for i in range(len(iterable)):
#   print((i, iterable[i]))

for i in enumerate(iterable):
    print(i)


# print elements present in even indices

iterable = ["apple", "google", "walmart", "flipkart", "gmail"]

for i in iterable[::2]:
    print(i)

for i in range(len(iterable)):
    if i % 2 == 0:
        print(iterable[i])

for index, ele in enumerate(iterable):
    if index % 2 == 0:
        print(ele)


# create a dictionary of index and element pair where elements must be of odd length

iterable = ["apple", "google", "walmart", "flipkart", "gmail"]
d = {}

for index, ele in enumerate(iterable):
    if len(ele) % 2 == 1:
        d[index] = ele


print(d)


# traversing through multiple lists and creating a dictionary

l1 = [10, 20, 30]
l2 = ["apple", "google", "flipkart"]
d = {}


for i in range(len(l1)):
    d[l1[i]] = l2[i]

#print(d)

for ele1, ele2 in zip(l1, l2):
    d[ele1] = ele2
    

#print(d)


# word and its length

l = ["apple", "google", "flipkart"]

for element in l:
    print((element, len(element)))


# creating a dictionary with element and it's count pair in the given iterable

string = "hello world"

# {"h": 1, "e": 1, "l": 3, "o": 2, " ": 1, "w": 1, "r": 1, "d": 1}

# count()
d = {}

for char in string:
    d[char] = string.count(char)

print(d)

# without inbuilt method
d = {}

for char in string:
    if char not in d:
        d[char] = 1
        
    else:
        d[char] += 1

print(d)

# defaultdict()
from collections import defaultdict

dd = defaultdict(int)

for char in string:
    dd[char] += 1

print(dd)



# create a dictionary with word and its index pair

l = ["apple", "google", "gmail", "apple", "gmail", "flipkart", "apple"]
d = {}

# using normal dictionary
for index, element in enumerate(l):
    if element not in d:
        d[element] = [index]
    else:
        d[element] = d[element] + [index]   # d[element].append(index)


# using defaultdict()
dd = defaultdict(list)

for index, element in enumerate(l):
    dd[element].append(index)

"""

temperatures = {"Bangalore": (26, 32), "Chennai": (29, 35), "Delhi": (31, 36)}

# o/p:[("Bangalore", (26, 32)), ("Chennai",(29, 35)), ("Delhi", (31, 36))]

for element in temperatures.items():
    print(element)

print()
for city, temp in temperatures.items():
    print(city, temp)

print()
for city, (min_, max_) in temperatures.items():
    print(city, min_, max_)






    














