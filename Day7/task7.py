


class Student:

    school_name = "Green Valley High School"

    def __init__(self, name):
        self.name = name
        self.grades = []  
    def add_grade(self, score):
        """Add a validated grade between 0 and 100."""
        if 0 <= score <= 100:
            self.grades.append(score)
            print(f"Grade {score} added for {self.name}.")
        else:
            print("Invalid grade. Please enter a value between 0 and 100.")

    def average_grade(self):
        """Calculate and return the mean grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def student_info(self):
        """Show name, school, and average grade."""
        avg = self.average_grade()
        return f"Name: {self.name}, School: {Student.school_name}, Average Grade: {avg:.2f}"



student1 = Student("Atalia")
student2 = Student("Ahmad")

student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(75)

student2.add_grade(95)
student2.add_grade(88)

print(student1.student_info())
print(student2.student_info())
