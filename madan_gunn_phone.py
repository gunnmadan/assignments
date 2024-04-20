number= int(input("Please enter your phone number: "))

first_three = number // pow(10,7)
last_four = number % pow(10,4)
middle_three = number // pow(10,4) % pow(10,3)

print(f"\n({first_three}) {middle_three}-{last_four}")