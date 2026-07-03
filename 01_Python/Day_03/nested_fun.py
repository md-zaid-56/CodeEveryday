def course():
    """Print course name as well as student name using nested function"""
    print("The Course name is Data Science")

    def student():  #Nested function
        print("The Student name is Mohamad Zaid")

    student()

course()

#student()  # This will raise an NameError