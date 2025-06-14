'''
API - Application Programming Interface 
API is kind of URL which can be used to get data from or send data to other website or server.

URL -> hit(request) -> response -> data -> process -> display -> UI -> end user 

pip install requests -> to download requests module

https://fakestoreapi.com/products - Fake API

Four types of requests:

GET - fetch data (unencrypted method - prone to SQL injection)
POST - send data (encrypted method - secure)
PUT - update data
DELETE - delete data


'''

'''fakestoreapi'''

import requests

data = requests.get("https://fakestoreapi.com/products")

jsonData = data.json()

for i in jsonData:
    print(i["title"], i["price"]) # iteration

'''newsapi'''

import requests

data = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=77019ae0920b45d7896833a078b0ee7d")

jsonData = data.json()

for i in jsonData["articles"]:
    print(i["author"])


'''

https://www.google.com/?name="sid"&class="10th"

? and & are called query parameters. 
name="lokesh" and class="10th" are called query strings.
They are used to send data to the server.

'''

# Search for a book using API and fetch book details

'''booksindya'''

import requests

search_query = input("Enter the book name: ")
body = {"search": search_query}
data = requests.post("https://api.booksindya.in/booksindya/getmy", json=body)
jsonData = data.json()

if jsonData:
    for i in jsonData["data"]:
        print("Title:", i["booktitle"])
        print("Author:", i["auther"])
        print("MRP:", i["mrp"])
        print("Discount:", i["discount"])
        print("Actual Price:", i["actualprice"])
else:
    print("Book not found")
    
'''
Output:

Enter the book name: antim
Title: Antim Prahar By Sankalan karta & Manoj Kumar
Author: Sankalan karta & Manoj Kumar
MRP: 450
Discount: 45
Actual Price: 248

'''