class Student:
    def __init__(self, name, student_id, age, university_degree, semester, average, email, phone, campus, is_active):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.university_degree = university_degree
        self.semester = semester
        self.average = average
        self.email = email
        self.phone = phone
        self.campus = campus
        self.is_active = is_active
        self.failed_courses = 0

    def displayData(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Major:", self.university_degree)
        print("Current GPA:", self.average)

    def updateAverage(self, new_average):
        self.average = new_average
        return f"GPA updated to: {self.average}"

    def advanceSemester(self):
        self.semester += 1
        return f"Congratulations! Advanced to semester {self.semester}"

    def registerFailedCourse(self):
        self.failed_courses += 1
        return f"Current failed courses: {self.failed_courses}"

    def changeCampus(self, new_campus):
        self.campus = new_campus
        return f"Student transferred to campus: {self.campus}"


student1 = Student("Carlos Gomez", "17251109", 20, "Systems Engineering", 4, 8.5, "carlos@utec.edu.mx", "7751234567", "Tulancingo", True)

student1.displayData()
print("-" * 30)
print(student1.updateAverage(9.1))
print(student1.advanceSemester())
print(student1.registerFailedCourse())
print(student1.changeCampus("Pachuca"))
