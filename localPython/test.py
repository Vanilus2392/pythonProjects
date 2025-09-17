class Test:
    def test_method(self, score, grade):
        self.score = score
        self.grade = grade
    
    def getScore(self):
        return self.score
    
    def getGrade(self):
        return self.grade
    
    def setScore(self, score):
        self.score = score

    def setGrade(self, grade):
        self.grade = grade

    def display(self):
        print(f"Score: {self.score}, Grade: {self.grade}")

students = []
n = int(input("Enter number of students: "))
for i in range(n):
    student = Test()
    score = float(input(f"Enter score for student {i+1}: "))
    grade = input(f"Enter grade for student {i+1}: ")
    student.setScore(score)
    student.setGrade(grade)
    students.append(student)

for student in students:
    print(f"Student {i+1}: ", end="")
    student.display()