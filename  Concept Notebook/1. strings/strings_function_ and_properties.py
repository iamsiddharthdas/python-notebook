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

# Reverse a string

text = "Lokesh is a good boy, he is a full stack developer"
reverse = ""

for i in text:
    reverse = i + reverse

print(reverse)

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

def is_anagram(x, y):
    # Step 1: If lengths are different, they can't be anagrams
    if len(x) != len(y):
        return False

    # This list keeps track of which characters in y have been matched
    used = []

    # Loop through each character in x
    for i in range(0, len(x)):
        found = False  # Flag to check if a matching character is found

        # Try to match x[i] with some character in y
        for j in range(0, len(y)):
            already_used = False

            # Check if this character in y was already used
            for k in range(0, len(used)):
                if used[k] == j:
                    already_used = True
                    break

            # If not used and characters match
            if not already_used and x[i] == y[j]:
                used.append(j)  # Mark this character in y as used
                found = True    # Mark that we found a match
                break

        # If no match was found for x[i], not an anagram
        if not found:
            return False

    # All characters matched, it's an anagram
    return True

# Test cases
print(is_anagram("listen", "silent"))  # True
print(is_anagram("elbow", "below"))    # True
print(is_anagram("hello", "world"))    # False

'''Another example of anagram'''

def anagram(str1,str2):
    str1="".join(sorted(str1))
    str2="".join(sorted(str2))
    if str1==str2:
        print("yes it is anagram")
    else:
        print("No it is anagram")

anagram("Lokesh","Mukesh")

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

