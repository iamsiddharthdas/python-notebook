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
    