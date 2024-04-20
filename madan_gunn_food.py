menu_item = {"Hot Dog": 1.50 , "Slice of Pizza": 1.99, "Whole Pizza": 9.95, "Soft Drink": 0.59}
hot_dogs= int(input("\nPlease enter the number of Hot Dogs: "))
pizza_slices= int(input("\nPlease enter the number of Pizza Slices: "))
whole_pizzas= int(input("\nPlease enter the number of Whole Pizzas: "))
soft_drinks= int(input("\nPlease enter the number of Soft Drinks: "))
total = float(hot_dogs * menu_item["Hot Dog"] + pizza_slices * menu_item["Slice of Pizza"] + whole_pizzas * menu_item["Whole Pizza"] + soft_drinks * menu_item["Soft Drink"])
print(f"\nThe total cost of the order is ${total}")