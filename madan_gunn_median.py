first_number = int(input("Please enter the first number: "))
second_number = int(input("Please enter the second number: "))
third_number = int(input("Please enter the third number: "))
if first_number < second_number < third_number or third_number < second_number < first_number: 
    print("The median is: " , second_number)
elif second_number < first_number < third_number or third_number < first_number < second_number: 
    print("The median is: ", first_number)
else: 
    print("The median is", third_number )
    