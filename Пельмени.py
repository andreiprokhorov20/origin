import random
year = int(input('Введите год '))
month = int(input('Введите номер месяца '))
scholarship = int(input('Введите стипендию '))
price = int(input('Введите стоимость одной пачки '))
ostatok_pachki = 0
month_30 = [4,6,9,11]
month_31 = [1,3,5,7,8,10,12]
waste = 0
for i in range(1,5):
    dayweek = random.randint(1, 7)
    for j in range(1,8):
        if ostatok_pachki == 0:
            waste += price
            if j==dayweek: ostatok_pachki += 2
            else: ostatok_pachki += 1
        elif j==dayweek:
            waste += price
            ostatok_pachki += 2
        ostatok_pachki-=0.5
print(waste,ostatok_pachki)