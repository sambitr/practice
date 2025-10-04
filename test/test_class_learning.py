import pytest
from src.class_learning import Student, course


def test_student_details():
    s1 = Student("Alice", 20, 80)
    assert s1.get_details() == "Name: Alice, Age: 20, Grade: 80"
    assert s1.get_grade() == 80

def test_course_details():
    c1 = course("Mathematics", 3)
    assert c1.course_details() == "Course: Mathematics, has a maximum student capacity of: 3\n"
    assert c1.max_students == 3
    assert c1.course_name == "Mathematics"

def test_course_add_student():
    c1 = course("Mathematics", 3)
    s1 = Student("Alice", 20, 80)
    s2 = Student("Bob", 22, 90)
    s3 = Student("Charlie", 23, 40)
    s4 = Student("Sam", 23, 40)
    
    c1.add_student(s1)
    c1.add_student(s2)
    c1.add_student(s3)
    assert len(c1.students) == 3
    assert c1.course_details() == "Course: Mathematics, has a maximum student capacity of: 3\n"
    
    # Trying to add a third student should give us max student reached message
    c1.add_student(s4)
    assert c1.add_student(s4) == "maximum student capacity of Mathematics has reached. Student: Sam can't be added to the course: Mathematics"

def test_course_average_grade():
    s1 = Student("Alice", 20, 80)
    s2 = Student("Bob", 22, 90)
    s3 = Student("Charlie", 23, 40)
    c1 = course("Mathematics", 3)
    c1.add_student(s1)
    c1.add_student(s2)
    c1.add_student(s3)  

    assert c1.average_grade() == (80 + 90 + 40) / 3

    
