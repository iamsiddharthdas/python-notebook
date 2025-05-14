x = ["Tomato", "Brinjal", "Okhra", "Cabbage", "Bottle Gourd", "Cauliflowerssss", "Snake Gourd", "Moringa"]

longest = x[0]
for i in x:
    if len(i) > len(longest):
        longest = i

print(f"The longest vegetable name is: {longest}")

