class Number: 
    def __init__ (self, num):
        self.num = num
    def __str__(self):
        return str(self.num)
    def __add__(self, other):
        return Number(self.num + other.num)
    def __sub__(self, other):
        return Number(self.num - other.num)
    def __mul__(self, other):
        return Number(self.num * other.num)
    def __truediv__(self, other):
        return Number (self.num // other.num)
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: ")) 

a = Number(num1)
b = Number(num2)

add_result = a + b
print(f'{a} + {b} = {add_result}')

sub_result = a - b
print(f'{a} - {b} = {sub_result}')

mul_result = a * b
print(f'{a} / {b} = {mul_result}')

div_result = a / b
print(f'{a} / {b} = {div_result}')

final_result = (add_result + (sub_result * div_result)) / mul_result
print(f'({add_result} + {sub_result} * {div_result}) / {mul_result} = {final_result}')
