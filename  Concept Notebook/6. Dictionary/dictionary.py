'''
Dictionary -> {"key":"value"}
Key -> Unique, Immutable
Value -> Mutable

x ={
    "a" : 100, 
    "b" : 200,
    "c" : 300,
}

print(x["a"]) # prints 100 i.e value of key "a"
print(x["b"]) # prints 200 i.e value of key "b"
print(x["c"]) # prints 300 i.e value of key "c"

print(x) # prints {"a" = 100, "b" = 200, "c" = 300}

a,b,c - key
100,200,300 - value


'''

# Vegetable and their colours

x = {
    "Tomato" : "Red",
    "Brinjal" : "Purple",
    "Cabbage" : "Green",
    "Potato" : "Yellow",
    "Carrot" : "Orange",
}
for i in x:
    print(i,x[i])
    # i -> key
    # x[i] -> value 
    
'''
Output:

Tomato Red
Brinjal Purple
Cabbage Green
Potato Yellow
Carrot Orange


'''

print(x) # prints {"Tomato" : "Red", "Brinjal" : "Purple", "Cabbage" : "Green", "Potato" : "Yellow", "Carrot" : "Orange"}
print (x["Tomato"]) # prints Red
print (x["Cabbage"]) # prints Green
print (x["Carrot"]) # prints Orange
print (x["Potato"]) # prints Yellow
print (x["Brinjal"]) # prints Purple

print(x.keys()) # prints dict_keys(['Tomato', 'Brinjal', 'Cabbage', 'Potato', 'Carrot'])
print(x.values()) # prints dict_values(['Red', 'Purple', 'Green', 'Yellow', 'Orange'])
print(x.items()) # prints dict_items([('Tomato', 'Red'), ('Brinjal', 'Purple'), ('Cabbage', 'Green'), ('Potato', 'Yellow'), ('Carrot', 'Orange')])


# Dictionary inside dictionary

x ={
    "Lokesh" : 100,
    "dict" :{
        "a" : 100,
        "b" : 200,
    }
}

for i in x["dict"]:
    print(x["dict"][i])

'''
Output:
a 100
b 200

'''

print(x["dict"]["a"]) # prints 100
print(x["dict"]["b"]) # prints 200



# Printing with/without a specific key

x={
    "id": 1,
    "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
    "price": 109.95,
    "description": "Your perfect pack for everyday use and walks in the forest",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
    "rating": {
        "rate": 3.9,
        "count": 120
    }
}


for i in x:
    if i != "rating":
        print(i,x[i])
        # i -> key
        # x[i] -> value
'''
Output:

id 1
title Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops
price 109.95
description Your perfect pack for everyday use and walks in the forest
category men's clothing
image https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg

'''

for i in x:
    if i == "rating":
        print(i,x[i])
        
'''
Output:
rating {'rate': 3.9, 'count': 120}

'''


# Dictionary in a List - JSON data

x=[
    {
        "id": 1,
        "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "price": 109.95,
        "description": "Your perfect pack for everyday use and walks in the forest",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
        "rating": {
            "rate": 3.9,
            "count": 120
        }
    },
    {
        "id": 2,
        "title": "Mens Casual Premium Slim Fit T-Shirts ",
        "price": 22.3,
        "description": "Slim-fitting style, contrast raglan long sleeve",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/71-3HjOadlL._AC_UX679_.jpg",
        "rating": {
            "rate": 4.1,
            "count": 259
        }
    },
    {
        "id": 3,
        "title": "Mens Cotton Jacket",
        "price": 55.99,
        "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_.jpg",
        "rating": {
            "rate": 4.7,
            "count": 500
        }
    }
]




for i in x:
    print("Title -->",i["title"])
    print("Price -->",i["price"])

'''
Output:
Title --> Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops
Price --> 109.95
Title --> Mens Casual Premium Slim Fit T-Shirts 
Price --> 22.3
Title --> Mens Cotton Jacket
Price --> 55.99

'''

