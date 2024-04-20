import operator


def addition(num1, num2):
    result = num1 + num2 
    print("Result:", num1, '+', num2, '=', result)

def subtraction(num1, num2):
    result = num1 - num2
    print("Result:", num1, '-', num2, '=', result)
    
def multiplication(num1, num2):
    result = num1 * num2
    print("Result:", num1, '*', num2, '=', result)
        
def division(num1, num2):
    if num2 == 0: 
        print("Error: Division by zero")
    else:
        result = num1 / num2 
        print("Result:", num1, '/', num2, '=', result) 

def modulus(num1, num2):
    result = num1 % num2
    print("Result:", num1, '%', num2, '=', result)

def power(num1, num2):
    result = num1 ** num2
    print('Result:', num1, '**', num2, '=', result)

def floor_division(num1, num2):
    if num2 == 0:
        print("Error: Division by zero")     
    else:
        result = num1 // num2
        print("Result:", num1, '//', num2, '=', result)
        
def calculate(expression):
    if expression.lower() in ['quit', 'q']:
          return True
      
    components = expression.split()
    if len(components) < 3:
        print("Invalid expression - ", expression)
        return

    num1, operator, num2 = components
                
    num1 = float(num1)
    num2 = float(num2)
    if operator == '+':
        addition(num1, num2)
    elif operator == '-':
        subtraction(num1, num2)
    elif operator == '*':
        multiplication(num1, num2)
    elif operator == '/':
        division(num1, num2)
    elif operator == '%':
        modulus(num1, num2)
    elif operator == '**':
        power(num1, num2)
    elif operator == '//':
        floor_division(num1, num2)
    else: 
        print("Error: Invalid Operator - ", expression)

while True:
    print("Please enter an expression:")
    expression = input()
    if calculate(expression):
        break