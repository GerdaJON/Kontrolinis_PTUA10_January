

# Task #1 - Fix Code
# OK Fix initializing in Student and Teacher classes (0.1t)
# OK Fix record_grade() function in Student class (0.1t)
# OK Implement performance_report() function in Student class (0.1t)
# OK Implement  list_courses() function in the Teacher class (0.1t)
# NOT generate_report() function returns attendance status as VIRUS VIRUS VIRUS, which is wrong. Fix it. (0.1t)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.enrolled_courses = []
        self.grades = {}  # Dictionary to store grades for courses

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)

    def performance_report(self, course):
        if course not in self.enrolled_courses:
            print(f"Student: {self.name}, Course: {course.name}, Status: Not enrolled.")
        else:
            print(f"Student: {self.name}, Course: {course.name}, Grade: {self.grades[course]}")

    def record_grade(self, course, grade):
        if course in self.enrolled_courses:
            self.grades[course] = grade
        else:
            print(f"Student: {self.name}, Course: {course.name}, Status: Not enrolled.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.courses = []

    def list_courses(self):
        course_names = []
        for course in self.courses:
            course_names.append(course.name)
        return course_names


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.attendance = {}
        teacher.courses.append(self)  # Add this course to the teacher's course list

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.attendance[student] = []

    def record_attendance(self, student, date, status):
        if student in self.students:
            self.attendance[student].append((date, status))

    def generate_report(self):
        for student in self.students:
            attendance_record = self.attendance.get(student, [])
            attendance_status = attendance_record
            print(f"Student: {student.name}, Attendance: {attendance_status}")


# Example usage
math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher)
alice = Student("Alice", 20)
bob = Student("Bob", 21)

alice.enroll(math_course)
bob.enroll(math_course)

# Recording attendance
math_course.record_attendance(alice, "2024-01-21", "Present")
math_course.record_attendance(bob, "2024-01-21", "Absent")

# Recording grades
alice.record_grade(math_course, "A")
bob.record_grade(math_course, "B")

# Generating reports
math_course.generate_report() # Student: Alice, Attendance: ['2024-01-21: Present'], Student: Bob, Attendance:
# ['2024-01-21: Absent']

# Testing implemented methods
alice.performance_report(math_course)  # Student: Alice, Course: Mathematics, Grade: A
print("Courses taught by Mr. Smith:", math_teacher.list_courses())  # Courses taught by Mr. Smith: ['Mathematics']

# Task #2 - Implement a Lesson class.
# Feel free to experiment with this task. This class can represent individual lessons within
# a course, containing details like the lesson topic, materials, date etc. Course class should be updated to include
# add_lesson() and get_lessons() function , example usage:
# lesson1 = Lesson("Algebra Basics", "2024-02-01", ["Algebra Textbook Chapter 1"])
# lesson2 = Lesson("Introduction to Geometry", "2024-02-08", ["Geometry Workbook"])
# math_course.add_lesson(lesson1)
# math_course.add_lesson(lesson2)
# math_course.get_lessons()
# This task is worth 0.4t.


class Lesson:
    def __init__(self, topic, date, materials, classroom):
        self.topic = topic
        self.date = date
        self.materials = materials
        self.classroom = classroom

    def show_details(self):
        print(f'Topic: {self.topic}, Date: {self.date}, Materials: {self.materials}, Classroom: {self.classroom}')


class Course:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.lessons = []

    def add_lesson(self, lesson):
        if isinstance(lesson, Lesson):
            self.lessons.append(lesson)
        else:
            raise TypeError('Lesson must be an instance of Lesson')

    def get_lessons(self):
        return self.lessons


lesson1 = Lesson("Algebra Basics", "2024-02-01", ["Algebra Textbook Chapter 1"], 10)
lesson2 = Lesson("Introduction to Geometry", "2024-02-08", ["Geometry Workbook"], 12)
lesson3 = Lesson('English for Beginners', '2024-02-01', 'slides, video, coursebooks', 5)

course = Course('Maths', 'Basic course of Algebra and Geometry in English')
course.add_lesson(lesson1)
course.add_lesson(lesson2)
course.add_lesson(lesson3)
lessons = course.get_lessons()
print(lessons)
