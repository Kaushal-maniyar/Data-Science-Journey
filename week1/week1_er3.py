# 1
street = 'Street No. 7'
city = 'Rajkot'
country = 'india'

address1 = street + '\n' + city + '\n' + country
address2 = f'{street}\n{city}\n{country}'
print(address1)
print(address2)

# 2
sentence = 'Earth revolves around the sun'
print(sentence[6:14])
print(sentence[-3:])

# 3
x = 4
y = 2
print(f"I eat {x} veggies and {y} fruits daily.")

# 4
wrong_sentence = 'maine 2000 banana khaye'
right_sentence = wrong_sentence.replace('2000 banana', '10 samose')
print(right_sentence)