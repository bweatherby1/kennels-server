class Employee():
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        
new_employee = Employee(1, "Todd", 26)

print(new_employee.name)
