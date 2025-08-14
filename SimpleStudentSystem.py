class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class StudentSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(student.get_info())

    def remove_student(self, name):
        self.students = [student for student in self.students if student.name != name]

def main():
    system = StudentSystem()

    while True:
        action = input("Choose an action (add, display, remove, exit): ").strip().lower()
        
        if action == 'add':
            name = input("Enter student's name: ")
            age = input("Enter student's age: ")
            student = Student(name, age)
            system.add_student(student)
            print(f"Added student: {student.get_info()}")
        
        elif action == 'display':
            print("Current students:")
            system.display_students()
        
        elif action == 'remove':
            name = input("Enter the name of the student to remove: ")
            system.remove_student(name)
            print(f"Removed student with name: {name}")
        
        elif action == 'exit':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid action. Please try again.")    
    

if __name__ == "__main__":
    main()