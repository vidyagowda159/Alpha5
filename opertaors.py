Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

s = "hello"

s * 3
'hellohellohello'

l = [1, 2, 3]
l * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]

t = (1, 2, 3)
t * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 2, 3)


s1 = "hai"
s2 = "hello"

s1 > s2
False
s2 > s1
True

s1 = "apple"
s2 = "hello"
s1 < s2
True

l1 = [1, 2, 3]
l2 = [2, 3, 4]
l1 > l2
False
l1 = [1, 2, 3]
l2 = [1, 2, 3, 4]
l2 > l1
True

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 > s2
False
s2 > s1
False
s1 == s2
False

s1 = {1, 2, 3}
s2 = {2, 3, 1}
s1 == s2
True

s1 = {1, 2, 3}
s2 = {2, 3, 1, 4}
s1 > s2
False
s2 > s1
True

dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

# logical operators

a = 1
b = 10

a and b
10
0 and 1
0
str() and [1, 2]
''
# list(), []/ str(), ""/ tuple(), ()/ set()/ dict(), {}


() and {}
()

() or {}
{}

not 0
True
not str()
True
not [1, 2]
False

a = 10
a = a + 2
a
12
a += 2
a += 1
a -= 1


d = {"a": 1, "b": 2, "c": 3}
d["a"]
1
value = d["a"]
value
1
value + 1
2

d["a"] + 1
2
d
{'a': 1, 'b': 2, 'c': 3}
d["a"] = d["a"] + 1
d
{'a': 2, 'b': 2, 'c': 3}

d["a"] = d["a"] + 10
d
{'a': 12, 'b': 2, 'c': 3}

dict_ = {"flower": ["rose", "lily", "lotus"], "animals": ["cat", "dog"]}

dict_["flower"]
['rose', 'lily', 'lotus']
dict_["flower"].append("sunflower")
dict_
{'flower': ['rose', 'lily', 'lotus', 'sunflower'], 'animals': ['cat', 'dog']}

dict_["animals"] = dict_["animals"] + ["lion"]
dict_
{'flower': ['rose', 'lily', 'lotus', 'sunflower'], 'animals': ['cat', 'dog', 'lion']}


# identity operator

a = [1, 2, 3]
b = [1, 2, 3]

a == b
True

id(a) == id(b)
False

a is b
False

a is not b
True


a = [1, 2, 3, 4, 5]

4 in a
True
"a" in a
False

"n" not in a
True
1 in 10
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    1 in 10
TypeError: argument of type 'int' is not iterable

a = [1, 2, 3, 4, 5]
(1, 2) in a
False
1, 2 in a
(1, True)

6, 2 in a
(6, True)
