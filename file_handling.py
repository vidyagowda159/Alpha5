import os
from collections import defaultdict, Counter, deque
from itertools import islice

# directories

#print(os.getcwd())
#os.chdir(r"C:\Users\Vidyashree M C\Desktop\Python_practice\files")
#print(os.getcwd())
#os.mkdir("Demo")
#os.rmdir("Demo")

#os.chdir(r"C:\Users\Vidyashree M C\Desktop\Python_practice")
#print(os.getcwd())
#os.mkdir(r"C:\Users\Vidyashree M C\Desktop\Python_practice\files\Demo")
#os.rmdir(r"basics.py")
#print(os.listdir())


# files

#os.popen(r"C:\Users\Vidyashree M C\Desktop\Python_practice\basics.py")
#os.remove(r"C:\Users\Vidyashree M C\Desktop\Python_practice\files\spam.txt")
#os.rename("old", "new")

# path

#print(os.path.exists(r"C:\Users\Vidyashree M C\Desktop\Python_practice\files\spam.txt"))

#print(os.path.getsize(r"C:\Users\Vidyashree M C\Desktop\Python_practice\files\sample.txt"))

#############################################################################################

# opening a file

f_path = r"C:\Users\Vidyashree M C\Desktop\Python_practice\files\sample.txt"

"""
# without context manager
f_obj = open(f_path)
print(f_obj.closed)     # False
f_obj.close()
print(f_obj.closed)     # True

# with context manager
with open(f_path) as f:
    print("inside with block", f.closed)     # False

print("outside with block", f.closed)         # True
"""

#******************************************************************************************

# modes
"""
with open(f_path) as f:     # read mode
    print(f)


#with open(f_path, "w") as f:     # write mode
#    print(f)


with open(f_path, "a") as f:     # write mode
    print(f)

with open("spam.txt", "x") as f:     # write mode
    print(f)


with open(f_path, "r+") as f:     # read mode
    print(f)

"""




# reading from a file


with open(f_path) as file:
    #print(file.read())  # entire file as a string
    #print(file.readline()) # one line at a time as a string
    #print(file.readlines()) # entire file in list where lines will be separte elements

    #print(file.read(4))         # hell
    #print(file.readline(5))    # o
    #print(file.readline(3))     # hel
    #print(file.readline(11))    # lo world
    #print(file.readlines(50))    # App
    pass

"""
with open(f_path) as file:
    # traversing through a file by loading one line into memory
    for line in file:
        print(line)


with open(f_path) as file:
    # traversing through one line at a time in an iterator(lazy iterable)
    print(next(file))
"""

# *****************************************************************************************

# read the contents of a file(sample.txt) without loading file into memory

os.chdir(r"C:\Users\Vidyashree M C\Desktop\Python_practice\files")
"""
with open("sample.txt") as file:
    for line in file:
        print(line)


# print line number along with line in sample.txt file

with open("sample.txt") as file:
    for line_no, line in enumerate(file, start=1):
        print(line_no, line, sep="--")

# print only non blank lines in the file sample.txt

with open("sample.txt") as file:
    for line in file:
        if line.strip():    # check empty lines
            print(line)


# read the file in reversed order

with open("sample.txt") as file:
    for line in reversed(list(file)):
        print(line)

# count the number of lines in the file sample.txt

with open("sample.txt") as file:
    count = 0
    for _ in file:
        count += 1
    print(count)

# count the number of words in the file sample.txt

with open("sample.txt") as file:
    word_count = 0
    for line in file:
        if line.strip():
            words = line.split()
            for word in words:
                word_count += 1
    print(word_count)
    

with open("sample.txt") as file:
    word_count = 0
    for line in file:
        if line.strip():
            words = line.split()
            word_count += len(words)
    print(word_count)

# length of line and line
with open("sample.txt") as file:
    for line in file:
        if line.strip():
            print( len(line), line)

# create a dictionary with word and its count pair in the file

with open("sample.txt") as file:
    word_count = {}
    # traversing through each line
    for line in file:
        if line.strip():
            words = line.split()

            # traversing through the words in a line
            for word in words:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
            
    print(word_count)
    


with open("sample.txt") as file:
    d = defaultdict(int)
    for line in file:
        if line.strip():
            for word in line.split():
                d[word] += 1
    print(d)

# extract ip addresses from access-log file

with open("access-log.txt") as file:
    for line in file:
        if line.strip():
            words = line.split()
            print(words[0])

# create a dictionary with ip addresses and their count pair

# normal dictionary

with open("access-log.txt") as file:
    d = {}
    for line in file:
        if line.strip():
            words = line.split()

            if words[0] not in d:
                d[words[0]] = 1
            else:
                d[words[0]] += 1
    print(d)


# default dictionary

with open("access-log.txt") as file:
    dd = defaultdict(int)
    for line in file:
        if line.strip():
            words = line.split()
            dd[words[0]] += 1
    print(dd)



# most occurred ip address in the access-log file

# using normal dictionary
with open("access-log.txt") as file:
    d = {}
    for line in file:
        if line.strip():
            words = line.split()
            if words[0] not in d:
                d[words[0]] = 1
            else:
                d[words[0]] += 1

min_, *rest, max_ = sorted(d.items(), key=lambda item: item[-1])
#print(max_)

# using Counter class
with open("access-log.txt") as file:
    l = []
    for line in file:
        if line.strip():
            words = line.split()
            l.append(words[0])
c = Counter(l)
print(c)        # counter object -> dictionary of element of its count pair in descending order
print(c.most_common())  # list of tuples of element and its count pair
print(c.most_common(n)) # list of tuple of the n maximum repeated elements (n -> integer)
"""

# ******** read nth line from a file ************
n = 15
with open("access-log.txt") as file:
    for line_no, line in enumerate(file, start=1):
        if line_no == n:
            print(line)

# islice
with open("access-log.txt") as file:
    lines = islice(file, n-1, n)
    print(list(lines))


# ********* read first n lines *************
n = 6
with open("access-log.txt") as file:
    for line_no, line in enumerate(file, start=1):
        if line_no <= n:
            print(line)

# using islice
with open("access-log.txt") as file:
    lines = islice(file, n)
    print(list(lines))


# ********* read 10th to 15th lines **************
start = 10
end = 15

# islice
with open("access-log.txt") as file:
    lines = islice(file, start-1, end)
    for line in lines:
        print(line)


# enumerate
with open("access-log.txt") as file:
    for line_no, line in enumerate(file, start=1):
        if 10 <= line_no <= 15:
            print(line)


# ********* read last n lines from a file **********

n = 4
with open("sample.txt") as file:
    lines_count = 0
    
    for _ in file:
        lines_count += 1
    
    file.seek(0)
    res = islice(file, lines_count - n, lines_count)
    print(list(res))
    

# deque

with open("sample.txt") as file:
    lines = deque(file, n)
    print(list(lines))













        































































    







































        
























































































































