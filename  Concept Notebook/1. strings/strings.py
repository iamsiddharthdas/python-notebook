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




