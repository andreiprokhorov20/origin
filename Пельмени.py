import random
print('Введите год')
year = int(input())
print('Введите номер месяца')
month = int(input())
print('Введите стипендию')
scholarship = int(input())
print('Введите стоимость одной пачки')
price = int(input())
ostatok_pachki = 0
month_30 = [4,6,9,11]
month_31 = [1,3,5,7,8,10,12]
waste = scholarship
dayweek = random.randint(1,7)
if ostatok_pachki == 0 and ((((year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)) and (month == 2)) or (month in month_30) or (dayweek == 1)):
    waste += price
elif ostatok_pachki == 0.5 and (month != 2):
    waste += price
elif ostatok_pachki == 1 and (month in month_31):
    waste += price
elif ostatok_pachki == 0:
    waste += 2 * price
print(waste)
