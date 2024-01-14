def calculate_area(base, height, shape):
    if shape == 'triangle':
        area = (1 / 2) * base * height
    else :
        area = base * height
    return area

def print_pyramid(number):
    for i in range(number):
        for j in range(i + 1):
            print('*', end='')
        print()
print(calculate_area(5,10, 'triangle'))
print_pyramid(10)