class VendingMachine:
    def __init__(self, soda_quantity, coffee_quantity, water_quantity):
        self.soda_quantity = soda_quantity
        self.coffee_quantity = coffee_quantity
        self.water_quantity = water_quantity

    def buy(self, drink_type):
        if drink_type == 1:
            if self.soda_quantity > 0:
                self.soda_quantity -= 1
                return " "
            
        elif drink_type == 2:
            if self.coffee_quantity > 0:
                self.coffee_quantity -= 1
                return " "
            
        elif drink_type == 3:
            if self.water_quantity > 0:
                self.water_quantity -= 1
                return " "
            
    def restock(self, drink_type, quantity):
        if drink_type == 1:
            self.soda_quantity += quantity
        elif drink_type == 2:
            self.coffee_quantity += quantity
        elif drink_type == 3:
            self.water_quantity += quantity

    def inventory(self):
        return f"Inventory\nSoda: {self.soda_quantity} bottles\nCoffee: {self.coffee_quantity} bottles\nWater: {self.water_quantity} bottles"

vending_machine = VendingMachine(10, 10, 10)

while True:
    command = input(" ")

    if command.lower() == 'quit' or command.lower() == 'q':
        break

    if command.lower() == 'buy':
        drink_type = int(input("Please select a option:\n 1 - Soda\n 2 - Coffee\n 3 - Water\n "))
        print(vending_machine.buy(drink_type))
    elif command.lower() == 'restock':
        drink_type = int(input("Please select an option:\n 1 - Soda\n 2 - Coffee\n 3 - Water\n "))
        quantity = int(input("Please enter an amount:\n "))
        vending_machine.restock(drink_type, quantity)
    elif command.lower() == 'inventory':
        print(vending_machine.inventory())
    else:
        print("Invalid command. Please try again.")
