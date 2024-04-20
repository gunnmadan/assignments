highway_num = int(input("Please enter an interstate number: "))
if highway_num < 1 or highway_num > 999: 
    print("Invalid highway number")   
elif highway_num < 100: 
    direction = "north/south"
    if highway_num % 2 == 1: 
        direction = "north/south"
    else: 
        direction = "east/west"
    print("Primary U.S. interstate highway", highway_num, "which runs", direction)
else: 
    primary_num = highway_num % 100
    if primary_num == 0: 
        print("Invalid highway number")
    else: 
        direction = "north/south"
        if primary_num % 2 == 1: 
            direction = "north/south"
        else: 
            direction = "east/west"
        print("Auxiliary highway servicing Interstate", primary_num, "which runs", direction)
        
    


    







        
     

