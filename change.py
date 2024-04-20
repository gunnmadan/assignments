quarters = 0
dimes = 0
nickels = 0
pennies = 0
cents = int(input("Please enter a number of cents: "))

if cents // 25 != 0:
    quarters = cents // 25
    cents = cents - quarters * 25
if cents // 10 != 0:
    dimes = cents // 10
    cents = cents - dimes * 10
if cents // 5 != 0:
    nickels = cents // 5
    cents = cents - nickels * 5
if cents // 1 != 0:
    pennies = cents // 1
    cents = cents - pennies * 1

    
print(f"Coins: {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")