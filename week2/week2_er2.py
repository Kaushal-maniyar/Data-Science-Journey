class Animal:
    def __init__(self, habitat):
        self.habitat = habitat


class Dog(Animal):
    def __init__(self, habitat):
        super().__init__(habitat)

    def __str__(self):
        return f'{self.habitat}'


dog1 = Dog('Mini house')
dog2 = Dog('Street')

print(dog1)
print(dog2)
