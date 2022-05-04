d = {}
type(d)
<class 'dict'>
d = dict()
type(d)
<class 'dict'>

# ************************* initializing a dictionary *************************************
d = {"a": 1, "b": 2}
d = dict({"a": 1, "b": 2})
d = dict(a=1, b=2)
d
{'a': 1, 'b': 2}

d1 = dict([("a", 1), ("b", 2), ("c", 3)])
d1
{'a': 1, 'b': 2, 'c': 3}

len(d1)
3

d = {"a": 1, "b": 2, "a": 3}
d
{'a': 3, 'b': 2}


d1 = {10: "hai"}
d1
{10: 'hai'}

d2 = dict(10="hai")
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?

# ****************************** composite keys ********************************

d2 = {26, 1: "Republic day"}
SyntaxError: invalid syntax

d2 = {[26, 1]: "Republic day"}
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d2 = {[26, 1]: "Republic day"}
TypeError: unhashable type: 'list'

d2 = {(26, 1): "Republic day"}
d2
{(26, 1): 'Republic day'}


# ****************************** accessing values from a dictionary **********************************
places = {"bangalore": 25, "Mysore": 35, "chennai": 30}

places["bangalore"]
25
places["chennai"]
30
places["chennai_city"]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    places["chennai_city"]
KeyError: 'chennai_city'

places.get("chennai")
30
places.get("chennai_city")
places.get("chennai_city", "No key")
'No key'
places.get("chennai", "No key")
30

# ***************************** keys(), values(), items() *******************************
places.keys()
dict_keys(['bangalore', 'Mysore', 'chennai'])

places.values()
dict_values([25, 35, 30])

places.items()
dict_items([('bangalore', 25), ('Mysore', 35), ('chennai', 30)])

# ************************* adding key - value pairs to dictionary ***********************
places
{'bangalore': 25, 'Mysore': 35, 'chennai': 30}

places["Kolkata"] = 40
places
{'bangalore': 25, 'Mysore': 35, 'chennai': 30, 'Kolkata': 40}

places.update({"Punjab": 36})
places
{'bangalore': 25, 'Mysore': 35, 'chennai': 30, 'Kolkata': 40, 'Punjab': 36}

places.update(Punjab = 38)
places
{'bangalore': 25, 'Mysore': 35, 'chennai': 30, 'Kolkata': 40, 'Punjab': 38}

places.setdefault("kerala")
places
{'bangalore': 25, 'Mysore': 35, 'chennai': 30, 'Kolkata': 40, 'Punjab': 38, 'kerala': None}

places.setdefault("kerala", 10)
places
{'bangalore': 25, 'Mysore': 35, 'chennai': 30, 'Kolkata': 40, 'Punjab': 38, 'kerala': None}

places.setdefault("cochin", 10)
10
places
{'bangalore': 25, 'Mysore': 35, 'chennai': 30, 'Kolkata': 40, 'Punjab': 38, 'kerala': None, 'cochin': 10}


# ********************** creating keys from other iterables ******************************

l = ["a", "b", "c"]
tuple(l)
('a', 'b', 'c')
set(l)
{'a', 'c', 'b'}
dict(l)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    dict(l)
ValueError: dictionary update sequence element #0 has length 1; 2 is required

d = {}
d.fromkeys(l)
{'a': None, 'b': None, 'c': None}
d
{}
dict.fromkeys(l)
{'a': None, 'b': None, 'c': None}
dict.fromkeys(l, True)
{'a': True, 'b': True, 'c': True}

# *************************** removing values from a dictionary ************************************
places
{'bangalore': 25, 'Mysore': 35, 'chennai': 30, 'Kolkata': 40, 'Punjab': 38, 'kerala': None, 'cochin': 10}

places.pop("cochin")
10
places
{'bangalore': 25, 'Mysore': 35, 'chennai': 30, 'Kolkata': 40, 'Punjab': 38, 'kerala': None}

places.pop("cochin")
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    places.pop("cochin")
KeyError: 'cochin'

places.pop("cochin", "key is not present")
'key is not present'

places.popitem()
('kerala', None)

places.popitem()
('Punjab', 38)
places
{'bangalore': 25, 'Mysore': 35, 'chennai': 30, 'Kolkata': 40}

del places["Mysore"]
places
{'bangalore': 25, 'chennai': 30, 'Kolkata': 40}

# ******************** concatenating dictionaries ***************************
d1 = dict([("a", 1), ("b", 2), ("c", 3)])
d1
{'a': 1, 'b': 2, 'c': 3}

{*d1, *places}
{'chennai', 'Kolkata', 'a', 'c', 'bangalore', 'b'}

{**d1, **places}
{'a': 1, 'b': 2, 'c': 3, 'bangalore': 25, 'chennai': 30, 'Kolkata': 40}

d1 | places
{'a': 1, 'b': 2, 'c': 3, 'bangalore': 25, 'chennai': 30, 'Kolkata': 40}
