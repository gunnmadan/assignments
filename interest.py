principal= int(input("Please enter the loan principal: "))
term= int(input("Please enter the loan term in months: "))
rate= float(input("Please enter the annual interest rate of the loan in decimal: "))
amount= principal*(1+(rate/12))**term
print(f"\nThe amount of interest in this loan is ${amount-principal:.2f}")