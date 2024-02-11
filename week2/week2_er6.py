def generator(limit):
    for i in range(limit):
        yield i ** 2


iterator = generator(10)
for i in iterator:
    print(i)
