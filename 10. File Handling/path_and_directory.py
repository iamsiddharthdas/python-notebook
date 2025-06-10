
import os 

print (os.getcwd())  # Get the current working directory

'''
Output:
/Users/siddharth/Documents/GitHub/python-notebook/10. File Handling

'''
os.chdir("/Users/siddharth/Documents/GitHub/python-notebook/10. File Handling/experiment")  
# Change the current working directory


os.mkdir("Python Class") 
# Create a new directory

# Create 100 directory in a folder 'experiment'

for i in range(100):
    mkdir_name = f"random{i}"
'''
Output: random0, random1, ..., random99

'''

os.remove("abc.txt") # Remove a file not folder
os.rmdir("Python Class")  # Remove a directory (must be empty)

'''
arr = os.listdir()  # List all files and directories in the current directory
for i in arr:
    os.remove(i)  # Remove each file in the directory
    os.rmdir(i)  # Remove each directory in the directory

'''
os.makedirs("Python Class/Folder/Subfolder") # Create a nested directory structure
os.rename("abc.txt", "new_abc.txt") # Rename a file from abc.txt to new_abc.txt

print (os.listdir())  
# List all files and directories in the current directory

print (os.path.exists("abc.txt")) 
# Check if a file exists

print (os.path.isfile("abc.txt"))
# Check if a path is a file

print (os.path.isdir("abc.txt"))  
# Check if a path is a directory

print (os.path.getsize("abc.txt"))  
# Get the size of a file in bytes

print (os.path.abspath("abc.txt"))  
# Get the absolute path of a file

print (os.path.dirname("abc.txt"))  
# Get the directory name of a file  

'''

Absolute Path: Full path from the root directory to the file (e.g., /Users/siddharth/Documents/GitHub/python-notebook/10. File Handling/experiment/abc.txt).
Relative Path: Path relative to the current working directory (e.g., abc.txt if in the same directory).

os.path.abspath("abc.txt") -> /Users/siddharth/Documents/GitHub/python-notebook/10. File Handling/experiment/abc.txt

'''

