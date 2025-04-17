
num = int(input("Enter a number "))
i=1
count=0
while i <= num:
    if num % i == 0:
        count = count + 1
    i+=1

if count == 2:
    print("its prime")
else:
    print("its composite")
    
'''
let num = 7
when num divided by i leaves 0 as remainder, count increments

so,
i = 1 ->  7 % 1 = 0, count increments -> count = 0+1 = 1
i = 2 ->  7 % 2 != 0, count remains the same
i = 3 ->  7 % 3 != 0, count remains the same
i = 4 ->  7 % 4 != 0, count remains the same
i = 5 ->  7 % 5 != 0, count remains the same
i = 6 ->  7 % 6 != 0, count remains the same
i = 7 ->  7 % 7 = 0, count increments -> count = 1+1 = 2

i = 8 (greater than num) -> exits loop and checks for 'count == 2' condition
if count  = 2, prints: its prime
if count != 2, prints: its composite

'''