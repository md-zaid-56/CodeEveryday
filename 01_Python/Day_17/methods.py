class Employee :
    def __init__(self,name,department,salary):
        self.name = name
        self.department = department
        self.salary = int(salary)
    
    def display_info(self) :
        """Display all the Employee Information"""
        print("\nEmployee Details")
        print("-"*64)
        print(f"Name :{self.name} \nDepartment: {self.department} \nSalary: {self.salary}")
        print("="*64)

    def give_raise(self,amount):
        """Increase in Salary"""
        self.salary += int(amount)
        print("\nRaised Salary")
        print("-"*64)
        print(f"{self.name} increased Salary by {amount}")
        print("="*64)

emp1 = Employee("Zaid","DataScience",50000)
emp2 = Employee("Zoro","ML","100000")

emp1.display_info()
emp2.display_info()

emp1.give_raise(6000)
emp2.give_raise(50000)