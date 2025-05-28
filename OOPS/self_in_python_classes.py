
# A simple explanation of 'self' in Python classes

class Car:
    # 'self' refers to the current object (like "me" or "this car")
    def set_color(self, color):
        self.color = color  # Assigns color to the specific object

    def show_color(self):
        print(f"My color is {self.color}")

# Creating objects from the class (like making real cars from a blueprint)
thar = Car()
creta = Car()

# Set different colors for each car
thar.set_color("Black")   # self = thar
creta.set_color("White")  # self = creta

# Each car remembers its own color
thar.show_color()   # Output: My color is Black
creta.show_color()  # Output: My color is White

# In summary:
# - 'self' is automatically passed as the first parameter
# - It refers to the specific object calling the method
# - Helps each object maintain its own state independently

