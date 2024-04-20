replacements = {'o': '0','i': '1','a': '@', 'e': '3', 'A': '4','B': '8','s': '$'} 

password = input("Please Enter Your Password: ")

new_password = " "
i = 0
while i < len(password): 
    char = password[i]
    if char in replacements: 
        new_password = new_password + replacements[char]
    else: 
        new_password = new_password + char 
    i += 1

new_password += "!" 

print("Your new strong password is:",new_password)     