class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,value):
        if value<=0:
            raise ValueError("Salary cannot be Negative")
        self.__salary = value

Emp1 = Employee("Zaid",50000)
#Emp1.salary = -5000
print("="*5,"Employee Details","="*5)
print(f"\nEmployee Name:{Emp1.name}\nEmployee Salary:{Emp1.salary}")

