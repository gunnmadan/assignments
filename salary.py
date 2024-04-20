hourly_wage= int(input("Please enter your hourly wage: "))
hours_worked= int(input("Please enter the number of hours worked per week: "))
weeks_worked= int(input("Please enter the number of weeks worked this year: "))
total_salary= hourly_wage*hours_worked*weeks_worked
print(f"\nYour salary so far this year is ${total_salary}")