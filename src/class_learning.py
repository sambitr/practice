class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
    def get_grade(self):
        return self.grade
    
class course:
    def __init__(self, course_name, max_students: int):
        self.course_name = course_name
        self.max_students = max_students
        self.students = [] ## list to hold enrolled students for the course.

    def course_details(self):
        return f"Course: {self.course_name}, has a maximum student capacity of: {self.max_students}\n"
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return f"student: {student.name} is added to the course {self.course_name}"
        else:
            return f"maximum student capacity of {self.course_name} has reached. Student: {student.name} can't be added to the course: {self.course_name}"
    
    def average_grade(self):
        value = 0
        for i in self.students:
            value += i.get_grade()
        return value / len(self.students) if self.students else 0
            

# if __name__ == "__main__":
#     s1 = Student("Alice", 20, 80)
#     s2 = Student("Bob", 22, 90)
#     s3 = Student("Charlie", 23, 40)
#     s4 = Student("Sam", 23, 40)
#     c1 = course("Mathematics", 3)
#     c1.add_student(s1)
#     c1.add_student(s2)
#     c1.add_student(s3)  
#     c1.add_student(s4)  # This should indicate that the max capacity has been reached

#     print(f"Average for the course: {c1.course_name} is: {c1.average_grade()}")
# # print(s1.get_details())

# # print(c1.course_details())