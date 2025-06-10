# Create 10 text files with different names and write some content in each file

# x = [".pdf", ".txt", ".docx", ".xlsx", ".csv", ".js", ".html", ".css", ".py"]


for i in range(10):
    filename = f"file_{i}.txt"
    filepath = "/Users/siddharth/Documents/GitHub/python-notebook/10. File Handling/experiment/"
    myfile = open(f"{filepath}{filename}", "w")
    myfile.write(f"This is the content of {filename}\n")
    myfile.close()

'''using lambda and map'''

# filepath = "/Users/siddharth/Documents/GitHub/python-notebook/10. File Handling/experiment/"
# list(map(lambda i: open(f"{filepath}{i}.txt", "w").close(), range(1, 11)))

'''
# map() Function

map() applies a function to each item in an iterable (like a list or range).
Syntax: map(function, iterable)
Returns a map object (an iterator), which you often convert into a list.


# Why Wrap in list(...)?

map() returns a lazy iterator (i.e., it doesn't run until iterated).
Wrapping it in list() forces immediate execution:

list(map(...))  # forces all operations to execute

'''