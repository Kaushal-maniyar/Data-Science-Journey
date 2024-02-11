class AdultException(Exception):
    def __init__(self, message="Person is Adult."):
        self.message = message
        super().__init__(self.message)


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        if self.age <= 18:
            print("Person in not adult")
        else:
            raise AdultException()

    def __str__(self):
        return f'Name : {self.name} \nAge : {self.age}'


person = Person('Manveer', 22)
print(person)
try:
    person.get_minor_age()
except AdultException as a:
    print(a.message)
