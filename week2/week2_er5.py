class Fibonacci:

    def __init__(self, limit):
        self.a = 0
        self.b = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self.c = self.a + self.b
        self.a = self.b
        self.b = self.c
        if self.c <= self.limit:
            return self.c
        else:
            raise StopIteration


no_series = Fibonacci(2000)
for i in no_series:
    print(i)