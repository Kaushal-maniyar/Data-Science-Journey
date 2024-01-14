monthly_expense = [2200, 2350, 2600, 2130, 2190]
print(f"Feb extra use compare to Jan : {monthly_expense[1]-monthly_expense[0]}")
print(f"First quarter Total : {sum(monthly_expense)}")
print(f"Months where I spent exactly 2000 : {monthly_expense.count(2000)}")
monthly_expense.append(1980)
monthly_expense[3] = monthly_expense[3] - 200
print(monthly_expense)

heros=['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print(f'Total heros : {len(heros)}')
heros.append('black panther')
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
heros[1:3] = ['doctor strange']
heros.sort()
print(heros)
