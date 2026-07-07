student_ids = [101, 102, 103, 104]
student_names = [
    "Zaid",
    "Ali",
    "Sara",
    "Aman"
]
marks = [91, 85, 96, 78]
students = dict(zip(student_ids,student_names)) #Using Zip() to converting to Dictonary by using dict() with keys as Student ID and Value as Student Name
print(students)

result = list(zip(student_ids,student_names,marks)) #using Zip() to converting to list by uning list() and using 3 iterator
print(result)