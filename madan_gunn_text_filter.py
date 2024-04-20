banned_words = ["Turkey", "Dog", "Fox", "Cat", "Chicken"]

message = input("Input Message: ")

words = message.split()
filtered_message = " "

for word in words: 
    if word not in banned_words:
        filtered_message += word + ' '

filtered_message = filtered_message.strip()

print("Output Message:", filtered_message)