class Teacher:

    is_teacher = None


class Engineer:

    is_engineer = None


class Youtuber:

    is_youtuber = None


class Person(Teacher, Engineer, Youtuber):

    def __init__(self, teacher, engineer, youtuber):
        self.is_youtuber = youtuber
        self.is_engineer = engineer
        self.is_teacher = teacher


coder = Person(True, True, False)
print(coder.is_teacher)
print(coder.is_engineer)
print(coder.is_youtuber)
