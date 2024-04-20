num_values = int(input("Please enter the number of floating-point values: "))

values = []

for i in range(5):
    value = float(input("Please enter a floating-point value: "))
    values.append(value)

max_value = values[0]
for value in values:
    if value > max_value: 
        max_value = value

print("\nNormalized Floating-Point Values: ")
for value in values: 
    normalized_value = value / max_value 
    print(f'{normalized_value:.2f}')
