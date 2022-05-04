# ***************************************** Indexing ****************************************************

l = [10, 1.25, "Hello", [1, 2, "hai"], 1+2j]

l[2]
'Hello'
l[2][0]
'H'
l[2][-1]
'o'

l[3][1]
2

l[3][-1]
'hai'
l[3][-1][1]
'a'
l[-1]
(1+2j)

# ************************************** concatenation **********************************************************
a = "hello"
b = "world"

c = f"{a}{b}"
c
'helloworld'
d = a + b
d
'helloworld'

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l1 + l2
[1, 2, 3, 4, 5, 6, 7, 8]

l3 = [l1, l2]
l3
[[1, 2, 3, 4], [5, 6, 7, 8]]
l3 = [*l1, *l2]
l3
[1, 2, 3, 4, 5, 6, 7, 8]

# *************************************** slicing ************************************************

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

names[::-1]
['microsoft', 'instagram', 'facebook', 'amazon', 'yahoo', 'google', 'apple']

names[2][3]
'o'

names[:2]
['apple', 'google']

# *************************** modyfying elements in the list **************************************
names
['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

names[:2] = ["unkown", "unknown"]
names
['unkown', 'unknown', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names[:3] = ["unkown", "unknown"]
names
['unkown', 'unknown', 'amazon', 'facebook', 'instagram', 'microsoft']

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names[:2] = ["unkown", "unknown", "unknown", "unknown"]
names
['unkown', 'unknown', 'unknown', 'unknown', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names[3:5] = "unknown"
names
['apple', 'google', 'yahoo', 'u', 'n', 'k', 'n', 'o', 'w', 'n', 'instagram', 'microsoft']

names[3:5] = ["unknown"]
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

names[3:5] = ["unknown"]
names
['apple', 'google', 'yahoo', 'unknown', 'instagram', 'microsoft']

dir(names)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# **************************** list methods ********************************

# *********************** adding elements to a list - append(), extend(), insert() ***************************

names
['apple', 'google', 'yahoo', 'unknown', 'instagram', 'microsoft']

names.append(10)
names
['apple', 'google', 'yahoo', 'unknown', 'instagram', 'microsoft', 10]

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names.append("hai")
names
['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'hai']

names.append([1, 2, 3])
names
['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'hai', [1, 2, 3]]

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names.append("gmail")
names
['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'gmail']

# ****************** extend() *********************
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names.extend("gmail")
names
['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'g', 'm', 'a', 'i', 'l']

names.extend(10)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    names.extend(10)
TypeError: 'int' object is not iterable

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

names.append(["gmail", "amazon"])
names
['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', ['gmail', 'amazon']]

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names.extend("gmail", "amazon")
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    names.extend("gmail", "amazon")
TypeError: list.extend() takes exactly one argument (2 given)

names.extend(["gmail", "amazon"])
names
['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'gmail', 'amazon']

# ************************* insert() ***********************************
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names.insert(0, 10)
names
[10, 'apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names.insert(2, "facebook")
names
[10, 'apple', 'facebook', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names.insert(2, [1.24, "facebook"])
names
[10, 'apple', [1.24, 'facebook'], 'facebook', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names.insert(-2, [1.24, "facebook"])
names
[10, 'apple', [1.24, 'facebook'], 'facebook', 'google', 'yahoo', 'amazon', 'facebook', [1.24, 'facebook'], 'instagram', 'microsoft']


# ************************** Removing elements from a list ***************************************

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names.pop(-1)
'microsoft'
names
['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram']

names.remove("amazon")
names
['apple', 'google', 'yahoo', 'facebook', 'instagram']
names.remove("amazon")
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    names.remove("amazon")
ValueError: list.remove(x): x not in list

names.pop(10)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    names.pop(10)
IndexError: pop index out of range

names.pop()
'instagram'

names.remove()
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    names.remove()
TypeError: list.remove() takes exactly one argument (0 given)

names.clear()
names
[]

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

names[:3]
['apple', 'google', 'yahoo']

del names[:3]
names
['amazon', 'facebook', 'instagram', 'microsoft']

del names
names
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    names
NameError: name 'names' is not defined

# ****************************** copy ************************************
# copy()
s = "hai"
s1 = s
id(s)
1527009550256
id(s1)
1527009550256

l = [1, 2, 3]
l1 = l
id(l)
1527009714368
id(l1)
1527009714368

s = "hai"
s1 = s[:]
id(s)
1527009550256
id(s1)
1527009550256

l = [1, 2, 3]
l1 = l[:]
id(l)
1527009549568
id(l1)
1526973679168

l = [1, 2, 3, [10, 20]]
l1 = l[:]
id(l)
1527008907328
id(l1)
1527009602176
id(l[-1])
1527009714368
id(l1[-1])
1527009714368

# ************************************* deepcopy() ************************************
from copy import deepcopy
l = [1, 2, 3, [10, 20]]
l1 = deepcopy(l)
l1
[1, 2, 3, [10, 20]]
id(l1)
2179933902144
id(l)
2179933959744
id(l[-1])
2179933960064
id(l1[-1])
2179933959424

# *************************************** sorting ****************************************

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names.sort()
names
['amazon', 'apple', 'facebook', 'google', 'instagram', 'microsoft', 'yahoo']

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names.sort(reverse=True)
names
['yahoo', 'microsoft', 'instagram', 'google', 'facebook', 'apple', 'amazon']

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 10, 4, 7, 2]
names.sort()
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    names.sort()
TypeError: '<' not supported between instances of 'int' and 'str'

names = ['microsoft', 'apple', 'google', 'instagram', 'yahoo', 'amazon', 'facebook']
names.sort(key=len)
names
['apple', 'yahoo', 'google', 'amazon', 'facebook', 'microsoft', 'instagram']

# ****************************** index(), count() *************************************
names.index("amazon")
3
names.count("google")
1


# ***************************** typecasting ***************************************

s = "hello"
list(s)
['h', 'e', 'l', 'l', 'o']

s.split()
['hello']

l = ['h', 'e', 'l', 'l', 'o']
str(l)
"['h', 'e', 'l', 'l', 'o']"

"".join(l)
'hello'
