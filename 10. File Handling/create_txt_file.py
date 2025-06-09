# Create 10 text files with different names and write some content in each file

# x = [".pdf", ".txt", ".docx", ".xlsx", ".csv", ".js", ".html", ".css", ".py"]


for i in range(1,11):
    filename = f"file_{i}.txt"
    myfile = open(f'/Users/siddharth/Documents/GitHub/python-notebook/10. File Handling/experiment/{filename}', "w")
    myfile.write(f"This is the content of {filename}\n")
    myfile.close()

'''using lambda and map'''

# folder = "/Users/siddharth/Documents/GitHub/python-notebook/10. File Handling/experiment/"
# list(map(lambda i: open(f"{folder}{i}.txt", "w").close(), range(1, 11)))