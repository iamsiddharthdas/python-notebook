'''
File is of two types:

1. Text File 
2. Binary File 

Create/ Delete/ Read/ Write/ Append/ Copy/ Move - Operations in File Handling


'''

'''
abc.txt 

Hello, How are you?
Kal mein ghumne gaya tha

'''
# Read

myfile = open("abc.txt","r")
print(myfile.read())
myfile.close

'''
Output:

Hello, How are you?
Kal mein ghumne gaya tha

'''

# readline() - reads a single line from the file

myfile = open("abc.txt","r")
print(myfile.readline())
myfile.close

'''
Output:

Hello, How are you?

'''

# readlines() - reads all lines from the file and returns a list of lines

myfile = open("abc.txt","r")
print(myfile.readlines())
myfile.close()

'''Output: 

['Hello, How are you?\n', 'Kal mein ghumne gaya tha\n']

'''
# Write

myfile = open("abc.txt", "w")
myfile.write("Jai Mata di") # overwrites the existing content of the file
myfile.close()

'''
Output: No output, but the file is updated with the new content

The file now contains:
Jai Mata di 

'''

# Append

myfile = open("abc.txt", "a")
myfile.write("\nJai Mata di")
myfile.close()

'''
Output: No output, but the file is updated with the new line

The file now contains:
Hello, How are you?
Kal mein ghumne gaya tha
Jai Mata di


'''

# Read and Write (r+)

myfile = open("abc.txt", "r+")
print(myfile.read())
myfile.write("Jai Mata di")
myfile.close()

'''
Output and Text file:

Hello, How are you?
Kal mein ghumne gaya tha
Jai Mata di


'''

# Read and Write (w+)
myfile = open("abc.txt", "w+")
myfile.write("Jai Mata di")
myfile.seek(0)  # Move the cursor to the beginning of the file
print(myfile.read())
myfile.close()

'''
Output and Text file:

Jai Mata di

'''

# Append and Read (a+)
myfile = open("abc.txt", "a+")
myfile.write("Jai Mata di")
myfile.seek(0)  # Move the cursor to the beginning of the file
print(myfile.read())
myfile.close()

'''
Output and Text file:

Hello, How are you?
Kal mein ghumne gaya tha
Jai Mata di


'''


# r --> File only read
# w --> Write into a file if file not exist then create a new file
# a --> Append to a file if file not exist then create a new file
# r+ --> Read and Write into a file - File pointer at 0 index by default
# w+ --> Read and Write into a file but if file not exist then create a new file (overwrites existing content) - File pointer at last index by default
# a+ --> Append and Read into a file (not overwriting existing content, just appending to it) - File pointer at last index by default