quit_keywords = ["Quit","quit","q"]
user_input = " "

while user_input not in quit_keywords:
    user_input = input("Please Enter Your String: ")
    if user_input not in quit_keywords:
        reversed_input = ''
        for i in range(len(user_input) - 1, -1, -1):
            reversed_input += user_input[i]
        print("Reversed:", reversed_input)
    

        