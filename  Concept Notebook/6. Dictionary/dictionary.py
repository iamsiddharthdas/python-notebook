'''
Dictionary -> {"key":"value"} -> mutable

Key -> Unique, Immutable
Value -> Mutable

x ={
    "a" : 100, 
    "b" : 200,
    "c" : 300,
}

# a,b,c - key
# 100,200,300 - value

print(x["a"]) # prints 100 i.e value of key "a"
print(x["b"]) # prints 200 i.e value of key "b"
print(x["c"]) # prints 300 i.e value of key "c"

print(x) # prints {"a" = 100, "b" = 200, "c" = 300}

x.keys() # prints dict_keys(['a', 'b', 'c'])
x.values() # prints dict_values([100, 200, 300])
print(keys) # prints dict_keys(['a', 'b', 'c'])
print(values) # prints dict_values([100, 200, 300])

y ={
    1:100,
    2:200,
    3:300
}

print(y) # prints {1: 100, 2: 200, 3: 300}

z ={
    10.2:1
    22.4:2
    33.6:3
}

print(z) # prints {10.2: 1, 22.4: 2, 33.6: 3}

# key (allowed data types) -> str, int, float, bool

x.clear() # clears the dictionary


ko = {
    'a' : 100,
    'ab' : 200,
    'abc' : 300 # doesnt matter if the value is number or string, it will be overwritten
    'abc' : 400
    
}

print(ko) # prints {'a': 100, 'ab': 200, 'abc': 400} as 'abc' key is overwritten

# Append function for dictioanry
ko["abcd"] = True # adds key "abcd" with value True
ko["xyz"] = 88.99 # adds key "xyz" with value 88.99

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

# Iterating through Dictionary using for-zip loop

x = [10,20,30,40,50]
y = ["apple","mango","banana","grapes","orange"]

for i,j in zip(x,y):
    print(i,j)
    
'''
Output:

10 apple
20 mango
30 banana
40 grapes
50 orange


'''

x = [10, 20, 30, 40, 50]
y = ["apple", "mango", "banana", "grapes", "orange"]
z = [1.2, 1.5, 0.8, 2.0, 1.1]  # Price per unit

for i, j, k in zip(x, y, z):
    print(i, j, k)

'''
Output:
10 apple 1.2
20 mango 1.5
30 banana 0.8
40 grapes 2.0
50 orange 1.1


'''

# Without dict

''
x = ["apple", "mango", "kiwi", "banana", "orange"]
y = [10, 20, 30, 40, 50]

z = {}

for i,j in zip(x, y):
    z[i] = j

print(z)

'''
Output:

{'apple': 10, 'mango': 20, 'kiwi': 30, 'banana': 40, 'orange': 50}


'''

# With dict

x = ["apple", "mango", "kiwi", "banana", "orange"]
y = [10, 20, 30, 40, 50]

z = dict(zip(x, y))

print(z)

'''
Output:

{'apple': 10, 'mango': 20, 'kiwi': 30, 'banana': 40, 'orange': 50}


'''

# Turn it back into list

z = {'apple': 10, 'mango': 20, 'kiwi': 30, 'banana': 40, 'orange': 50}
x=[]
y=[]
for i in z:
    x.append(i)
    y.append(z[i])
print (x) 
print (y)

'''
Output:
['apple', 'mango', 'kiwi', 'banana', 'orange']
[10, 20, 30, 40, 50]

'''


# Make it into array and form keys and values

z = {'apple': 10, 'mango': 20, 'kiwi': 30, 'banana': 40, 'orange': 50}

x = []

for i in z:
    j = z[i]
    x.append([i, j])

print(x)


"""
Output:
[['apple', 10], ['mango', 20], ['kiwi', 30], ['banana', 40], ['orange', 50]]

"""

# Update function

x = {}

x.update({"Raju": "Men"})
x.update({"Sunita": "Women"})

print(x)

'''
Output:

{'Raju': 'Men', 'Sunita': 'Women'}


'''

# Delete a key

x = {}

x.update({"Raju": "Men"})
x.update({"Sunita": "Women"})


del x["Raju"]
print(x)

'''
Output:

{'Sunita': 'Women'}


'''

# pop function

x = {}

x.update({"Raju": "Men"})
x.update({"Sunita": "Women"})

x.pop("Raju")
print(x)

'''
Output:

{'Sunita': 'Women'}


'''

# pop item function - deletes the last item

x = {}

x.update({"Raju": "Men"})
x.update({"Sunita": "Women"})

x.popitem() # deletes the last item i.e. Sunita
print(x)

'''
Output:

{'Raju': 'Men'}

'''

# items function

x = {}

x.update({"Raju": "Men"})
x.update({"Sunita": "Women"})

print(x.items()) # converts the dictionary into a list by making keys and values into tuples

'''
Output:

dict_items([('Raju', 'Men'), ('Sunita', 'Women')]) 

'''

# Swap keys and values

x = {
    "a": 100,
    "b": 200,
    "c": 300,
    "d": 400
}

y = []

for i in x:
    j = x[i]
    y.append([j, i])

print(y)

'''
Output:

[[100, 'a'], [200, 'b'], [300, 'c'], [400, 'd']]


'''

'''Another method'''
x = {
    "a": 100,
    "b": 200,
    "c": 300,
    "d": 400
}

keys = x.keys()
values = x.values()

newDict = {}
for i, j in zip(keys, values):
    newDict[j] = i

print(newDict)

'''
Output:

[[100, 'a'], [200, 'b'], [300, 'c'], [400, 'd']]


'''

# Handles duplicates

x = {
    "a": 100,
    "b": 200,
    "c": 100
}

y = {}

for i in x:
    j = x[i]
    if j not in y:
        y[j] = [i]
    else:
        y[j].append(i)

print(y)

'''
Output:
{100: ['a', 'c'], 200: ['b']}



'''

'''Another way to handle duplication'''

x = {
    "a": 100,
    "b": 200,
    "c": 100
}

newDict = {}

for i, j in zip(x.keys(), x.values()):
    if j not in newDict:
        newDict[j] = [i]
    else:
        newDict[j].append(i)

print(newDict)

'''
Output:
{100: ['a', 'c'], 200: ['b']}

'''

# Dictionary comprehension

x = {i:i*2 for i in range(5)}

print(x)

'''
Output:

{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}


'''

# Dictionary comprehension with if condition

x = {i:i*2 for i in range(5) if i%2 == 0}

print(x)

'''
Output:

{0: 0, 2: 4, 4: 8}

'''

# making y as key and x as value using dictionary comprehension

y = ["apple", "mango", "grapes", "kiwi", "orange"]
x = [10, 20, 30, 40, 50]

z = {j: i for i, j in zip(x,y)}

print(z)

'''
Output:

{'apple': 10, 'mango': 20, 'grapes': 30, 'kiwi': 40, 'orange': 50}


'''

# Multiple conditions in dictionary comprehension

x = [i*j if i*j!=0 else False for i in range(3) for j in range(3)]

print(x)

'''

This is what it does under the hood

for i in range(3):
    for j in range(3):
        print(i,j)

Output:

[0, 0, 0, 0, 1, 2, 0, 2, 4]


'''