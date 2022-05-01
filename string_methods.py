# Type casting

#******************************** integer **************************************
a = 10

float(a)
10.0
complex(a)
(10+0j)
bool(a)
True

#******************************** float **************************************
a = 12.75

int(a)
12
complex(a)
(12.75+0j)
bool(a)
True

#******************************** complex **************************************
a = 1+2j

int(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

float(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'

a = 1+0j
int(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
a
(1+0j)

bool(a)
True

bool(0j)
False

bool(j)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    bool(j)
NameError: name 'j' is not defined

#******************************** boolean **************************************

a = True

int(a)
1
b = False
int(b)
0

float(a)
1.0
float(b)
0.0

complex(a)
(1+0j)
complex(b)
0j

#****************************************** slicing ***************************************************
s = "hello world"
s[0:len(s):1]
'hello world'
s[::]
'hello world'

s[0:5]
'hello'
s[:5]
'hello'

s[6:len(s):1]
'world'
s[6::]
'world'

s[1:len(s):2]
'el ol'
s[::2]
'hlowrd'

s[::3]
'hlwl'

s
'hello world'
s[-1:len(s):1]
'd'
s[-1:-len(s):1]
''
s[-1:-11:1]
''
s[-1::-1]
'dlrow olleh'
s[::-1]
'dlrow olleh'
s == s[::-1]
False


s
'hello world'
s[3:19]
'lo world'

#************************************************** format strings ********************************************************
enter the name:John
string
'My name is John'

enter the name:Khan
string
'My name is Khan'


#***************************************************** Activity *************************************************************
s = "hello world"
s[::2]
'hlowrd'

s[::-2]
'drwolh'

s[::-1]
'dlrow olleh'

filename = "youtube.txt"
filename[7:]
'.txt'
filename[8:]
'txt'
filename[-3:]
'txt'

filename[:7]
'youtube'
filename[:-4]
'youtube'

url = 'https://google.com'
url[:5]
'https'
url[9:15]
'oogle.'
url[8:14]
'google'

#*********************************************** Strings **************************************************************
s
'hello world'
s[1]
'e'

s[1] = "z"
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    s[1] = "z"
TypeError: 'str' object does not support item assignment

dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 
'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 
'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


#********************************** string methods *********************************************

#************** upper(), lower() and swapcase() ***************
s
'hello world'
s.upper()
'HELLO WORLD'
s
'hello world'
b = s.upper()
b
'HELLO WORLD'
id(s)
2871000450160
id(b)
2870959834480
b
'HELLO WORLD'
b.upper()
'HELLO WORLD'

b.lower()
'hello world'

s = "Hello World"
s.swapcase()
'hELLO wORLD'

#******************* count() ********************
s
'Hello World'
s.count("o")
2
s.count("o", 5)
1
s.count("o", 5, 7)
0

#****************** index(), find(), rindex(), rfind() **********************
s.index("e")
1
s.index("l")
2
s.index("World")
6
s.index("l", 5, 9)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    s.index("l", 5, 9)
ValueError: substring not found

s.find("l", 5, 9)
-1
s.rindex("l")
9
s.rfind("o")
7
s.rfind("iu")
-1

#*********************** replace() ************************
s
'Hello World'
s.replace("e", "z")
'Hzllo World'
s
'Hello World'
s.replace("l", "z", 1)
'Hezlo World'
s.replace("l", "z")
'Hezzo Worzd'
s.replace("l", "z", 2)
'Hezzo World'

#*********************** startswith(), endswith() *********************
s
'Hello World'
s.startswith("h")
False
s.startswith("H")
True

s.endswith("o")
False
s.endswith("ld")
True

#******************************** split() *****************************

sentence = "python is a programming language"
sentence.split(" ")
['python', 'is', 'a', 'programming', 'language']
sentence.split()
['python', 'is', 'a', 'programming', 'language']
sentence.split("z")
['python is a programming language']
sentence.split(" ", 2)
['python', 'is', 'a programming language']
sentence.rsplit(" ", 2)
['python is a', 'programming', 'language']
sentence.split(" ")
['python', 'is', 'a', 'programming', 'language']
len(_)
5
len(sentence.split(" "))
5
sentence.split(" ", 2)
['python', 'is', 'a programming language']
sentence.rsplit(" ", 2)
['python is a', 'programming', 'language']
sentence.split()
['python', 'is', 'a', 'programming', 'language']
sentence.rsplit()
['python', 'is', 'a', 'programming', 'language']


#*************************** join() ******************************
s = "hello"
"-".join(s)
'h-e-l-l-o'
"%".join(s)
'h%e%l%l%o'
"ABC".join(s)
'hABCeABClABClABCo'

l = sentence.split()
l
['python', 'is', 'a', 'programming', 'language']
" ".join(l)
'python is a programming language'
s
'hello'
sentence
'python is a programming language'
s = 'python,is,a,programming,language'
s.split(",")
['python', 'is', 'a', 'programming', 'language']

#**************************** strip() *******************************
s = "      hello     "
s.strip()
'hello'

s = "****#hai*****"
s.strip("*#")
'hai'
s.strip("#")
'****#hai*****'
