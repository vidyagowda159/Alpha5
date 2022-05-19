# left justified triangle
"""
*
* *
* * *
* * * *
* * * * *
"""

for row in range(5):
    for col in range(row+1):
        print("*", end=" ")
    print()

print()
for row in range(1, 6):
    print("* " * row)

print()

# right justified triangle
"""
        *
      * *
    * * *
  * * * *
* * * * *

"""

for row in range(1, 6):
    print(f'{"* " * row:>10}')
print()

# centre justified triangle
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""


for row in range(1, 6):
    print(f'{"* " * row:^10}')

print()

"""
*
*
*
* *
*
* * *
*
* * * *
"""

for row in range(1, 5):
    print("*")
    print("* " * row)

print()

# inverted triangle pattern

"""
* * * * *
* * * *
* * *
* *
*
"""

for row in range(5, 0, -1):
    print("* " * row)
print()

"""
* * * * *
  * * * *
    * * *
      * *
        *
"""

for row in range(5, 0, -1):
    print(f'{"* " * row:>10}')
print()

"""
* * * * *
 * * * *
  * * *
   * *
    *
"""

for row in range(5, 0, -1):
    print(f'{"* " * row:^10}')
print()


"""
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
"""


for row in range(1, 6):
    print(f'{"* " * row:^10}')

for row in range(4, 0, -1):
    print(f'{"* " * row:^10}')

print()

# alphabet pattern printing

"""
a
a b
a b c
a b c d
"""

for row in range(5):
    x = 0
    for col in range(row+1):
        print(chr(ord("a") + x), end=" ")
        x += 1
    print()
    

pat = ""
start = "a"
for row in range(4):
    var = chr(ord(start) + row)   # 97 + 0 = 97 = "a"
    pat = pat + var + " "            # "" + "a" ==> "a", "a" + "b" = "ab", "ab" + "c" == "abc"
    print(pat)
    

pat = ""
start = "a"
end = "d"
for row in range(ord(start), ord(end)+1):
    pat = pat + chr(row) + " "
    print(pat)
































































