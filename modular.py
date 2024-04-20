import math
import random 

radius= int(input("\n Please enter the radius of the sphere: "))
volume= round((4/3)*math.pi*(radius)**3,2)

integer= random.randint(1,10)
factorial= math.factorial(3)

print("The volume of the sphere with the radius of", radius, "is", "%.2f"% volume)
print("/n The factorial of", integer, "is", factorial)