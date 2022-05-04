s1 = {2, 4, 6, 8, 10}
s2 = {3, 6, 9, 12}

# ********************* union() *****************************
s1.union(s2)
{2, 3, 4, 6, 8, 9, 10, 12}
s1
{2, 4, 6, 8, 10}
s2
{9, 3, 12, 6}

# ********************* intersection() *************************
s1.intersection(s2)
{6}
s1
{2, 4, 6, 8, 10}
s2
{9, 3, 12, 6}

# ****************** difference() ****************************
s1.difference(s2)
{8, 2, 10, 4}

s2.difference(s1)
{9, 3, 12}

s1 - s2
{8, 2, 10, 4}
s2 - s1
{9, 3, 12}

# **************** concatenation ***************************
"hai" + "hello"
'haihello'
[1, 2] + [3, 4]
[1, 2, 3, 4]
(1, 2) + (3, 4)
(1, 2, 3, 4)

s1 = {2, 4, 6, 8, 10}
s2 = {3, 6, 9, 12}
s1 + s2
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s1 + s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'

# ******************* update() ******************************
s1.union(s2)
{2, 3, 4, 6, 8, 9, 10, 12}
s1
{2, 4, 6, 8, 10}
s2
{9, 3, 12, 6}


s1.update(s2)
s1
{2, 3, 4, 6, 8, 9, 10, 12}
s2
{9, 3, 12, 6}

a = {"google", "gmail"}
b = {"fb", "insta", "google"}

a.update(b)
a
{'gmail', 'google', 'fb', 'insta'}

a = {"google", "gmail"}
b = ("fb", "insta", "google")

a.update(b)
a
{'insta', 'gmail', 'google', 'fb'}


# ******************************** intersection_update() **************************
# intersection_update
a = {"google", "gmail"}
b = {"fb", "insta", "google"}

a.intersection_update(b)
a
{'google'}

# difference_update
a = {"google", "gmail"}
b = {"fb", "insta", "google"}

# ********************************** difference_update() *****************************
a.difference_update(b)
a
{'gmail'}

a = {"google", "gmail"}
b = {"fb", "insta", "google"}
b.difference_update(a)
b
{'insta', 'fb'}
a
{'gmail', 'google'}

# ********************************* symmetric_difference() ***************************
a = {"google", "gmail"}
b = {"fb", "insta", "google"}

a.symmetric_difference(b)
{'insta', 'gmail', 'fb'}

# ************************* symmetric_difference_update() ***************************
a = {"google", "gmail"}
b = {"fb", "insta", "google"}

a.symmetric_difference_update(b)
a
{'insta', 'gmail', 'fb'}

# ************************* hash values ********************************************
hash(10)
10
hash(1.2)
461168601842738689
hash("hai")
-7009278248679551178
hash([1, 2, 3])
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    hash([1, 2, 3])
TypeError: unhashable type: 'list'
hash({1, 2})
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    hash({1, 2})
TypeError: unhashable type: 'set'
hash((1, 2))
-3550055125485641917


# ***************************** empty datatypes ********************************
l = list(), []
s = str(), ""
t = tuple(), ()
s = set()

s1 = {}
type(s1)
<class 'dict'>


# *********************************** tuple activity *************************************

a = (1, )

t1 = (1, 2)
t2 = (3, 4)

t1 + t2
(1, 2, 3, 4)
(*t1, *t2)
(1, 2, 3, 4)

t = (1, 2, 3, 4, ["hai", "hello", 23], "python")
t[4]
['hai', 'hello', 23]
t[4][0]
'hai'
t[4][0][-1]
'i'
t[4][0][-1] = "y"
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    t[4][0][-1] = "y"
TypeError: 'str' object does not support item assignment

t = (1, 2, 3, 4, ["hai", "hello", 23], "python")
t[1:3]
(2, 3)
t[1:3] = ["hai", 10]
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    t[1:3] = ["hai", 10]
TypeError: 'tuple' object does not support item assignment

t1 = (1, 2)
t2 = (3, 4)

l1 = [1, 2]
l2 = [3, 4]
[l1, l2]
[[1, 2], [3, 4]]

t1 = (1, 2)
t2 = (3, 4)
[t1, t2]
[(1, 2), (3, 4)]

(t1, t2)
((1, 2), (3, 4))

(*t1, *t2)
(1, 2, 3, 4)
print((t1, t2))
((1, 2), (3, 4))


# ******************************** adding elements to a set **********************************

b = {"fb", "insta", "google"}
b.update("gmail")
b
{'google', 'm', 'a', 'fb', 'insta', 'i', 'g', 'l'}
b.update(["gmail"])
b
{'gmail', 'google', 'm', 'a', 'fb', 'insta', 'i', 'g', 'l'}

b = {"fb", "insta", "google"}
b.add(10)
b
{'insta', 10, 'google', 'fb'}

b.add("gmail")
b
{'gmail', 'google', 10, 'fb', 'insta'}

b.update("gmail")
b
{'gmail', 'google', 10, 'm', 'a', 'fb', 'insta', 'i', 'g', 'l'}

b.update(1.25)
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    b.update(1.25)
TypeError: 'float' object is not iterable

b.add(1.25)
b
{1.25, 'gmail', 'google', 10, 'm', 'a', 'fb', 'insta', 'i', 'g', 'l'}

b = {"fb", "insta", "google"}
b.add(1)
b
{'insta', 'google', 1, 'fb'}
b.add(True)
b
{'insta', 'google', 1, 'fb'}
b.add(False)
b
{False, 1, 'google', 'fb', 'insta'}
b.add(0)
b
{False, 1, 'google', 'fb', 'insta'}

b.add("fb")
b
{False, 1, 'google', 'fb', 'insta'}

b.add([1, 2])
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    b.add([1, 2])
TypeError: unhashable type: 'list'


# ****************************** removing elements from a set ***********************************
b
{False, 1, 'google', 'fb', 'insta'}
b.remove(False)
b
{1, 'google', 'fb', 'insta'}
b.remove(False)
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    b.remove(False)
KeyError: False

b.discard(False)
b.discard(1)
b
{'google', 'fb', 'insta'}

b.pop()
'google'
b.pop()
'fb'
b.pop()
'insta'

b = {'google', 'fb', 'insta'}
b.clear()
b
set()
id(b)
2595722448896

del b
b
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    b
NameError: name 'b' is not defined

# ************************** boolean methods ****************************
s1 = {2, 4, 6, 8, 10}
s2 = {1, 3, 5}
s1.intersection(s2)
set()

s1.isdisjoint(s2)
True
s2 = {2, 3}
s1.isdisjoint(s2)
False

s1 = {2, 4, 6, 8, 10}
s2 = {2, 4, 10}

s1.issuperset(s2)
True
s2.issuperset(s1)
False

s2.issubset(s1)
True
s1.issubset(s2)
False
