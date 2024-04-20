grade = [83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 80]

print(len(grade), "Students took the exam")
print("The highest grade was a" , max(grade))
print("The lowest grade was a" , min(grade))
print("The average grade was a" , sum(grade)/len(grade))

attendance_day1 = {"Mary", "Jake", "Sam", "Alex", "Percy", "Jessica", "Trent", "Mahmoud"}
attendance_day2 = {"Jake", "Sam", "Alex", "Percy", "Mahmoud", "Trent", "Caleb", "Zayne"}

print("\n" ,len(attendance_day1.union(attendance_day2)), "students attended the class")
print((attendance_day1.intersection(attendance_day2)), "attended both class days")
print((attendance_day1.symmetric_difference(attendance_day2)), "attended one class day")