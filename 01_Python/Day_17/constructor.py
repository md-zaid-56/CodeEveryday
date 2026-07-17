class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Zaid",18,"Data Science")
student2 = Student("Luffy",56,"AI")

print("="*45)
print(student1)
print(f"Student name: {student1.name}, age: {student1.age}, Course: {student1.course} ")

print("="*45)
print(student2)
print(f"Student name: {student2.name}, age: {student2.age}, Course: {student2.course} ")
