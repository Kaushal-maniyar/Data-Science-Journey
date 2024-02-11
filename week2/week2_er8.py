def check(fun):
    def modified_factorial(num):
        if type(num) == int and num >= 0:
            return fun(num)
        else:
            raise Exception("Number is not integer.")

    return modified_factorial


@check
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))
try:
    print(factorial(1.2))
except Exception as e:
    print(e)

try:
    print(factorial(-1.2))
except Exception as e:
    print(e)
