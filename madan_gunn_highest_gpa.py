"""
Gunn Madan

This program manages a course roster where students can be added with their first name, last name, and GPA. 
It includes funcionality to find the student with the highest GPA in course. 

"""

class EmptyRosterError(Exception):
    """Custom exception raised when trying to find the highest GPA student in an empty roster."""
    pass

class Student: 
    """Class representing a student with first name, last name , and GPA."""
    def __init__(self,first,last,gpa):
        self.first = first
        self.last = last
        self.gpa = gpa

    def get_first(self):
        return self.first
    def get_last(self):
        return self.last
    def get_gpa(self):
        return self.gpa
    
class Course: 
    """Class representing a course with a roster of students."""
    def __init__(self):
        self.roster = []
    def add_student(self,student):
        """add a student to the course roster."""
        self.roster.append(student)
    def course_size(self):
        return len(self.roster)
    def find_student_highest_gpa(self):
        if not self.roster:
            raise EmptyRosterError('Exception: Course Roster is Empty.')
        
        highest_gpa_student = max(self.roster, key = lambda student: student.get_gpa())
        return highest_gpa_student
    
def main():
    print("Welcome to DSCI 1301: Principles in DS 1")

    course = Course()

    while True: 
        try:
            first = input("Please Add Students to the Course: (quit or q to exit). \nEnter First Name: ")
            if first.lower() in ['quit', 'q']:
                break
            
            last = input("Enter Last Name: ")
            gpa = float(input("Enter GPA: ")) 

            if gpa < 0 or gpa > 4.0:
                print("Error: Enter a GPA between 0 and 4.") 
                continue

            student = Student(first, last, gpa)
            course.add_student(student)
        
        except ValueError:
            print("Error: Enter a Numeric GPA")

    if course.course_size() > 0:
        print(f"Course Size: {course.course_size()} students")
    
        try:
            highest_gpa_student = course.find_student_highest_gpa()
            print(f"Top Student: {highest_gpa_student.get_first()} {highest_gpa_student.get_last()} (GPA: {highest_gpa_student.get_gpa()}) ")

        except EmptyRosterError as e:
            print(e)
    
    else: 
        print("Course Size: 0 students")
        print("Exception: Course Roster is Empty.")
    
if __name__ == "__main__":
    main()

   