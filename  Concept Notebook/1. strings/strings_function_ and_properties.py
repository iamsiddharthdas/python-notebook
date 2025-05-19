message = """Bobby's World is a 
good cartoon in 1990s"""

# three apostrophe (""") to print multiple lines in the string

print(message)
print(len(message)) #length of string

print(message[0]) # [] -> index, starts at 0. [0] -> first character i.e "B"
print(message[0:5]) # 0th index is included & 5th index is excluded. so it will print "Bobby"
print(message[:5]) # prints same thing as [0:5]
print(message[8:]) #starts from 8th index i.e W and prints "World is a good cartoon in 1990s". 

print(message.lower()) # print the string in lowercase
print(message.upper()) # print the string in uppercase
print(message.count('oo')) #print the no of 'oo's in the string i.e 2
print(message.find('World')) #prints the index i.e 8
print(message.find('Universe')) #prints -1 as that string is not present in 'message'

# Character by Character printing

x = 'Lokesh is a good boy'

for i in range(len(x)):
    print(x[i]) # prints each character in the string

'''
Output:
L
o
k
e
s
h
 
i
s
 
a
 
g
o
o
d
 
b
o
y

'''
# Finding no. of vowels in a string

x="Lokesh is the Good Boy. Is he a Developer"

count=0
for i in range(len(x)):
    if x[i]=="a" or x[i]=="e" or x[i]=="i" or x[i]=="o" or x[i]=="u" or x[i]=="A" or x[i]=="E" or x[i]=="I" or x[i]=="O" or x[i]=="U":
        count=count+1
print(count)



'''
Mutable - can be modified
example: list, dict

Immutable - cannot be modified
example: str, tuple, int, float

'''

# Separators

print('ABC','DEF','GHI',sep='####')
print('ABC','DEF','GHI',end='*')
print("Hello world")

# Replacing a string

message='Hello World'

new_message= message.replace('World','Universe')

print(new_message) # prints Hello 'Universe' instead of Hello 'World'


# Endswith and Startswith

x = 'Lokesh is a good boy, he is a full stack developer'
print(x.endswith('er')) # prints True
print(x.endswith('ER')) # prints False

print(x.startswith('L')) # prints True
print(x.startswith('l')) # prints False

# Splitting a string

'''String to list'''

x = 'Lokesh is a good boy, he is a full stack developer'
y = x.split(' ') # splits the string into a list of words
print(y) # prints the list of words


'''

Output:

['Lokesh', 'is', 'a', 'good', 'boy,', 'he', 'is', 'a', 'full', 'stack', 'developer']

'''

'''List to String'''

x = ['Lokesh', 'is', 'a', 'good', 'boy,', 'he', 'is', 'a', 'full', 'stack', 'developer']
z = ' '.join(x) # joins the list of words into a string
print(z) 

'''
Output:
Lokesh is a good boy, he is a full stack developer

'''

# Difference between sort() and sorted()

'''
sort()

Used on: Lists only (in-place sorting).
Modifies the original list.
Returns: None (it modifies the list directly).

Syntax:

my_list.sort()

sorted()

Used on: Any iterable (lists, tuples, dictionaries, etc.).
Does not modify the original iterable.
Returns: A new sorted list.

Syntax:

sorted_list = sorted(my_iterable)

'''

# Using sort()
a = [3, 1, 4]
a.sort()
print(a)  # [1, 3, 4]

# Using sorted()
b = [3, 1, 4]
c = sorted(b)
print(b)  # [3, 1, 4] (original remains unchanged)
print(c)  # [1, 3, 4]

'''For sorting strings'''

b = 'str1'
c = ''.join(sorted(b))

print(c)

# Reverse a string

x = "Lokesh is a good boy, he is a full stack developer"

y = []


for i in range(len(x)):
    y.append(x[i])

y.reverse()

x = "".join(y) 

print(x)


'''Without using append() and reverse()'''


text = "Lokesh is a good boy, he is a full stack developer"
reverse = ""

for i in text:
    reverse = i + reverse

print(reverse)

'''
Output:

repoleved kcats lluf a si eh ,yob doog a si hsekoL

'''

# Palindrome

x="NitiN"
temp=x
y=[]
for i in range(len(x)):
    y.append(x[i])

y.reverse()
x="".join(y)
if x==temp:
    print("It is A pallindrome")
else:
    print("No it is not a pallindrome")
    


# Anagram

def anagram(str1,str2):
    str1="".join(sorted(str1))
    str2="".join(sorted(str2))
    if str1==str2:
        print("yes it is anagram")
    else:
        print("No it is anagram")

anagram("Lokesh","Mukesh")  # Output: Yes it is anagram
anagram("listen", "silent") # Output: Yes it is anagram
anagram("elbow", "below")   # Output: No it is not anagram

# Remove duplicate strings

x = 'Lokesh is a good boy'
y = ''  
for i in range(0, len(x)):
    found = False  
    for j in range(0, len(y)):
        if x[i] == y[j]:
            found = True
            break
    if not found:
        y = y + x[i]

print(y)

'''Another example'''

x = 'Lokesh is a good boy'
y = []

for i in range(len(x)):
    if x[i] not in y:
        y.append(x[i])

print(''.join(y))

# Count characters

def char_count(text):
    result = ""
    for char in text:
        if char not in result:
            count = text.count(char)
            result = result + (f"{char}:{count}  ")
    return result

print(char_count("Lokesh is a good boy"))

'''
Output:
L:1  o:4  k:1  e:1  s:2  h:1  i:1  a:1  g:1  d:1  b:1  y:1 

'''

'''Another method'''

x = 'Lokesh is a good boy'
y = []


for i in range(len(x)):
    if x[i] not in y:
        y.append(x[i])

print(y)

newString = ''.join(y)

print(newString)

for i in range(len(newString)):
    count = 0
    targetString = x[i]
    for j in range(len(x)):
        if x[j] == targetString:
            count = count+ 1

    print(f"Count of {x[i]} is {count}")

'''
Output:

Count of L is 1
Count of o is 4
Count of k is 1
Count of e is 1
Count of s is 2
Count of h is 1
Count of i is 1
Count of a is 1
Count of g is 1
Count of d is 1
Count of b is 1
Count of y is 1

'''

# Capitalize first letter of each word

def cap(text):
    return text.title()

print(cap("Lokesh is a good boy"))

'''
Output:
Lokesh Is A Good Boy

'''

'''Another method'''

x = "lokesh is a good boy"

y = x.split()
z =[]
for i in range(len(y)):
    z.append(y[i].capitalize)

x = " ".join(z)

print(x)

# Most frequent character

x = "Lokesh is the good boy"


x = x.replace(" ", "")

max_count = 0
max_char = ''
for char in x:
    count = x.count(char)
    if count > max_count:
        max_count = count
        max_char = char

print("Most frequent character:", max_char)

'''
Homework - 8,9,13


'''
# Check if substring exists
# Two strings are rotations of each other
# If string is pangram
# all substring of a string
# First non-repeating character
