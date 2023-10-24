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
dayweek = random.randint(1,7)
if ostatok_pachki == 0 and ((((year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)) and (month == 2)) or (month in month_30) or (dayweek == 1)):
    waste += price
elif ostatok_pachki == 0.5 and (month != 2):
    waste += price
elif ostatok_pachki == 1 and (month in month_31):
    waste += price
elif ostatok_pachki == 0 and month != 2:
    waste += 2 * price
if waste-scholarship>0:
    print("Надо занять",waste-scholarship,"рублей")
else:
    print("Ура!Стипендии хватит!!!")
