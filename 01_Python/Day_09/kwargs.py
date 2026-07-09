def register_employee(**details):
    print("New Registerd Employee info is :")
    for key, values in details.items():
        print(key," : ",values,end="\n")
    print("\n")

register_employee(name="Zaid",Position="Data Scientist",Department="Data Analytics")
register_employee(name="Sujal",Position="CEO",Department="Management",Salary=10000000)


        