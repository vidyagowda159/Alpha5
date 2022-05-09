"""
# print even numbers from 1 - 50

for i in range(1, 50, 1):
    if i % 2 == 0:
        print(i)

######################################################

# prime numbers

num = 12
i = 2

while i <= num ** 0.5:
    if num % i == 0:
        print("not a prime")
        break
    i += 1

else:
    print("prime")

#####################################
# prime series from 1 - 10

for num in range(1, 10):
    if num > 1:
        for i in range(2, num // 2):
            if num % i == 0:
                break

        else:
            print(num)



###########################################

# traversing through an iterable

# string


s = "hello"

i = 0

while i < len(s):
    print(i, s[i])
    i += 1
print()

for i in range(len(s)):
    print(i, s[i])
print()    

for char in s:
    print(char)


# set

s = {"hello", "hai", "world"}


for element in s:
    print(element)


# dictionary

d = {"a": 1, "b": 2, "c": 3}
# d[key] or d.get(key)

for key in d:
    print(key, d[key])
    

###########################################

string = "hello world"

for char in string:
    print(char, ord(char))


#############################################

s = "hAi goOd mornIng"
res = ""

for char in s:
    if char in "aeiouAEIOU":
        if ord("a") <= ord(char) <= ord("z"):
            res = res + chr(ord(char) - 32)

        elif ord("A") <= ord(char) <= ord("Z"):
            res = res + chr(ord(char) + 32)

    else:
        res = res + char
            
print(res)

##################################

s = "hello world"
d = {}

for ch in s:
    d[ch] = ord(ch)
print(d)


########################


s = "hello hi"
count = 0
for ch in s:
    count += 1
print(count)

#######################

s = "hello hi"
d = {}

for ch in s:
    d[ch] = s.count(ch)
print(d)

"""
###without using inbuilt func

s = "hello hi"
d = {}

for ch in s:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] += 1
print(d)


















































