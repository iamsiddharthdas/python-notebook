
i=8
x=100
y=95
while i>=3:
    x=x+i
    y=y-i
    i=i-1
print("Value of X is ",x)
print("Value of Y is ",y)
'''

    i = 8 → x = 100 + 8 = 108 → y = 95 - 8 = 87 → i = 7


    i = 7 → x = 108 + 7 = 115 → y = 87 - 7 = 80 → i = 6


    i = 6 → x = 115 + 6 = 121 → y = 80 - 6 = 74 → i = 5


    i = 5 → x = 121 + 5 = 126 → y = 74 - 5 = 69 → i = 4


    i = 4 → x = 126 + 4 = 130 → y = 69 - 4 = 65 → i = 3


    i = 3 → x = 130 + 3 = 133 → y = 65 - 3 = 62 → i = 2

Now i = 2, which is less than 3 → Exit the loop

Final Output:
    x = 133
    y = 62
    
'''
