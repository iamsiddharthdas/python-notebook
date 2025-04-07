message = """Bobby's World is a 
good cartoon in 1990s"""

# three apostrophe (""") to print multiple lines in the string

print(message)
print(len(message)) #length of string

print(message[0]) # [] -> index, starts at 0. [0] -> first character i.e "B"
print(message[0:5]) # 0th index is included & 5th index is excluded. so it will print "Bobby"
print(message[:5]) # prints same thing as [0:5]
print(message[8:]) #strats from 8th index i.e W and prints "World is a good cartoon in 1990s". 

print(message.lower()) # print the string in lowercase
print(message.upper()) # print the string in uppercase
print(message.count('oo')) #print the no of 'oo's in the string i.e 2
print(message.find('World')) #prints the index i.e 8
print(message.find('Universe')) #prints -1 as that string is not present in 'message'








