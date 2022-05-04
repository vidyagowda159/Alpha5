"""
a = int(input("enter a number:"))

if a % 2 == 0:
    print("even number")


####################################################################

if a % 2 == 0: print("even number")

#####################################################################

# if else

if a % 2 == 0:
    print("even numebr")

else:
    print("odd number")

# inline if-else

######################################################################

string = input("enter a string: ")

if string[::-1] == string:  # bool(string[::-1] == string)
    print("palindrome")
else:
    print("not a palindrome")

######################################################################
# string starting with vowel

string = input("enter a string: ")

if string[0] in "aeiouAEIOU":
    print("starts with vowel")
else:
    print("does not starts with vowel")

#######################################################################
# check if the integer is palindrome or not

num = 1221
a = str(num)

if a[::-1] == a:
    print(f"number {num} is a palindrome")

else:
    print(f"number {num} is not a palindrome")


#######################################################################
# check if the given character is a special character or not

a = input("enter a character:")

if not a.alnum():   # a.alnum() != True
    print("it is a special character")


#######################################################################
# check if the iterable is empty or not
    
l = [1, 2, 3]

if len(l) == 0:
    print("empty")

else:
    print("not empty")

#####################################
if bool(l):
    print(" not empty")

else:
    print("empty")


####################################
if l:       # bool(l)
    print("not empty")

else:
    print("empty")

####################################
# inline if-else

iterable = "hello"


# {True block} if condition else {false block}
 
print("not empty" if iterable else "empty")
"""

#####################################################################################
# check if the key is present in the dictionary

d = {"a": 1, "b": 2}
key = "c"
value = 2

if key in d:
    print("key is present")

else:
    print("not present")
    

# in line

print("key is present" if key in d else "not present")

# check if the value is present in the dictionary
print("value is present" if value in d.values()else "value is not present")
    























    
    
    










        




