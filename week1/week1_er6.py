india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# city = input("Enter city :")
# if city in india:
#    print("City belongs to India")
# elif city in pakistan:
#    print("City belongs to Pakistan")
# elif city in bangladesh:
#    print("City belongs to Bangladesh")
# else:
#    print("Not Found")

#city1 = input("Enter first city :")
#city2 = input("Enter second city :")

#if (city1 in india and city2 in india) or (city1 in pakistan and city2 in pakistan) or (
#        city1 in bangladesh and city2 in bangladesh):
#    print("Same country")
#else:
#    print("Not in same country")

sugar_level = float(input("Enter your sugar level : "))
if sugar_level < 80:
    print("Low Sugar Level")
elif sugar_level<=100:
    print("Normal Sugar Level")
else:
    print("High Sugar Level")
