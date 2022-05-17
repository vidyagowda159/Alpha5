numbers = [9, 3, 6, 2, 8, 5, 7, 12, 4, 19, 10]

names = ["google", "amazon", "gmail", "walmart", "flipkart", "microsoft", "apple"]

values1 = [10, 1.2, "python", 12, 1, 9]

values2 = [10, 1.2, 12, 1, 9]

values3 = [10, 1.2, True, 12, 1, 9]

values4 = [10, 1.2, 1+2j, True, 12, 1, 9]

################################################

# *** string ****
word = "python"
sorted_word = sorted(word)      # list
sorted_word = sorted(word, reverse=True)

# *** list ***
names = ["google", "amazon", "gmail", "walmart", "flipkart", "microsoft", "apple"]
s_names = sorted(names)
s_names = sorted(names, reverse=True)
s_names = sorted(names, reverse=True, key=len)

# *** set ***
names = {"google", "amazon", "gmail", "walmart", "flipkart", "microsoft", "apple"}
s_names = sorted(names)
s_names = sorted(names, reverse=True)
s_names = sorted(names, reverse=True, key=len)

# *** tuple ***
names = ("google", "amazon", "gmail", "walmart", "flipkart", "microsoft", "apple")
s_names = sorted(names)
s_names = sorted(names, reverse=True)
s_names = sorted(names, reverse=True, key=len)

# *** dictionary ***
name_len = {"google": 6, "apple": 8, "walmart": 7}
sorted_len = sorted(name_len)   # only keys
sort_ = sorted(name_len.items())

#****************************************************************************************

# sort the list in reversed order
names = ["google", "amazon", "gmail", "walmart", "flipkart", "microsoft", "apple"]
s_names = sorted(names, reverse=True)


# custom sorting

# sort the list based on the length of the elements
names = ["google", "amazon", "gmail", "walmart", "flipkart", "microsoft", "apple"]
s_names = sorted(names, key=len)

# ******** sort the list based on the first character of each element ***************
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'zomato']

# default sorting
s_names = sorted(names)

# custom sorting
def first_char(string):     # normal function for key
    return string[0]

f_char = lambda string: string[0]   # lambda expression for key

s_names = sorted(names, key=f_char)

# ******** sort the list based on the last character of each element ***************
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'zomato']

sorted_names = sorted(names, key=lambda string: string[-1])


# ******** sort the list based on the first element of each tuple ***************
names = [('facebook', 8),('apple', 5), ('instagram', 9), ('google', 6), ('yahoo', 5)]

s1 = sorted(names)

s = sorted(names, key=lambda element: element[0])

# ******* sort the dictionary based on the key ********************
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }

sorted(prices)   # only keys list
sorted(prices.items())
sorted(prices.items(), key=lambda item: item[0])


# ******* sort the dictionary based on the values ********************
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }

sorted(prices.values())
sorted(prices.items(), key=lambda item: item[-1])


# ******* sort the dictionary based on the length of the key *****************
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }

s = sorted(prices.items(), key=lambda item: len(item[0]))


# ******* sort the dictionary based on the length of the value **************
dial_codes = {86: 'China', 91: 'India', 1: 'United States', 62: 'Indonesia', 55: 'Brazil'}
   
s = sorted(dial_codes.items(), key=lambda item: len(item[-1]))

# ******* sort the dictionary based on the last character of the value **************
dial_codes = {86: 'China', 91: 'India', 1: 'United States', 62: 'Indonesia', 55: 'Brazil'}

s = sorted(dial_codes.items(), key=lambda item: item[-1][-1])

# ********** longest word in the sentence ***************
sentence = "python is a programming language and programming is fun"

words = sentence.split()
s_words = sorted(words, key=len)
shortest, *rest, longest = s_words

# ********** longest non repeated word and its length pair in the sentence ***************

sentence = "python is a programming language and programming is fun"

words = sentence.split()
d = {word: len(word) for word in words if words.count(word) == 1}
s_words = sorted(d.items(), key=lambda item: item[-1])
min_, *rest, max_ = s_words

# ********** print all the maximum values in the list ******************
numbers = [7, 4, 9, 2, 8, 9, 6, 4, 5, 9]
largest = max(numbers)

max_nums = []
for num in numbers:
    if largest == num :
        max_nums.append(num)

# ********** print all the shortest words in the sentence ******************

sentence = "hai, how are you doing today"
min_, *rest, max_ = sorted(sentence.split(), key=len)

for word in sentence.split():
    if len(min_) == len(word):
        print(word)


# Grouping anagrams.
words = ['eat', 'silent', 'ate', 'hello',  'listen', 'tea']

d = {}
for word in words:
    key = "".join(sorted(word))
    if key not in d:
        d[key] = [word]
    else:
        d[key].append(word) # d[key] += [word]
        
























        

































































