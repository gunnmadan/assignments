road_speed= int(input("Please enter the speed limit for the road: "))
vehicle_speed= int(input("Please enter the vehicle's recorded speed: "))
lower_speed= road_speed - 10

if vehicle_speed <= lower_speed: 
    print("The speeding fine is $50.")
elif vehicle_speed > (road_speed +6) and vehicle_speed < (road_speed+20):
    print("The speeding fine is $75.")
elif vehicle_speed > (road_speed +21) and vehicle_speed < (road_speed +40): 
    print("The speeding fine is $150")
elif vehicle_speed > (road_speed + 40): 
    print("The speeding fine is $300")
else: 
    print("There is no fine.")
    