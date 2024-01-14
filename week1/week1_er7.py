result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
heads = 0
tails = 0
for side in result:
    if side == 'heads':
        heads += 1
    else:
        tails += 1
print(f"No of tail: {tails}")
print(f"No of heads : {heads}")

for i in range(1,11):
    print(i**2)

expense_list = [2340, 2500, 2100, 3100, 2980]
month = ['Jan', 'Feb', 'March', 'April', 'May']
expense = int(input("Enter expense"))
if expense in expense_list:
    print(f"Month : {month[expense_list.index(expense)]}")
else:
    print("Nor Found")

for _ in range(5):
    answer = input("Are you tired?")
    if answer == 'yes':
        print("you didn't finish the race")
        break
else:
    print("Congratulations")

for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()