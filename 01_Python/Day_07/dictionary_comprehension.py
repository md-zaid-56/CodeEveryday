courses = ["Python","C++","Machine Learning","SQL"]
course_length = {
    course:len(course) 
    for course in courses
    }
print(course_length)

length_more_than_5 = {
    course:len(course)
    for course in courses
    if len(course)>5
} 

print(length_more_than_5)