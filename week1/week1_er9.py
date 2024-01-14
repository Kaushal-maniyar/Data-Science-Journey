import math

population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}


def print_dictionary(dict):
    for country, count in dict.items():
        print(f'{country}==>{count}')


def circle_calc(radius):
    area = math.pi * (radius**2)
    circum = 2 * math.pi * radius
    diameter = 2 * radius
    return area, circum, diameter

# wish = input("Enter what you want : ")
# if wish == 'print':
#    print_dictionary(population)
# elif wish == 'add':
#    country_name = input("Enter country name :").lower()
#    if country_name in population:
#        print("Already Exist")
#    else:
#        count = int(input("Population please :"))
#        population[country_name] = count
# elif wish == 'remove':
#    country_name = input("Enter country name :").lower()
#    if country_name in population:
#        population.pop(country_name)
#        print_dictionary(population)
#    else:
#        print("Not Found")
# else:
#    print(population.get(input("Enter country : ")))


a, c, d = circle_calc(float(input("Enter Radius : ")))
print(f'Area : {a}\nCircumference : {c}\nDiameter : {d}')
