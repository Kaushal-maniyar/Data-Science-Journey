class Employee:

    id = None

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID: {self.id} \nName: {self.name}")


# Creating a emp instance of Employee class
emp1 = Employee(1, "coder")
emp2 = Employee(2,'Hacker')
emp1.display()
emp2.display()
#
# # Deleting the property of object
# del emp.id
# # Deleting the object itself
# try:
#     print(emp.id)
# except AttributeError:
#     print("emp.id is not defined")
#
# del emp
# try:
#     emp.display()  # it will gives error after deleting emp
# except NameError:
#     print("emp is not defined")