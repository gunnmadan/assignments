import random 

random_number = random.randint(1,100)

print("\nI have generated a random number between 1 and 100. You have 10 attempts to guess the number.")

for attempt in range(1, 11):
    guess = int(input(f"Guess {attempt}: "))
    if guess == random_number: 
        print("You correctly guessed my random number!")
    elif guess > random_number: 
        print("Your guess is greater than my random number. Try Again.")
    else: 
        print("Your guess is less than my random number. Try Again.")
else:  
    print(f"Sorry, you have run out of attempts. The correct number was {random_number}.")           