sum_of_money= int(input("Please enter a number of cents: "))

n_quaters= sum_of_money // 25
sum_of_money= sum_of_money % 25

n_dimes= sum_of_money // 10
sum_of_money= sum_of_money % 10

n_nickles= sum_of_money // 5
sum_of_money= sum_of_money % 5

n_pennies= sum_of_money // 1
#sum_of_money= sum_of_money % 1

print(f"Coins: {n_quaters} quaters, {n_dimes} dimes, {n_nickles} nickles, {n_pennies} pennies")