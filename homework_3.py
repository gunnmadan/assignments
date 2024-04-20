class Vector: 
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        new_x = self.x + other.x 
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)
    

try: 
    user_num = int(input(':> '))
    div_num = int(input(':> '))
    result = user_num / div_num
except ValueError as ve:
    print(f"Error: {ve}. Please enter valid integers.")
except ZeroDivisionError:
    print('Error: Division by zero is not allowed.')
else: 
    print(f"Result: {result}")

    