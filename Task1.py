money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

#print("Количество месяцев, которое можно протянуть без долгов:", ...)

for value in range(0, 13):
    if value == 0:
        money_capital += salary - spend
    else:
        spend += spend * increase
        money_capital += salary - spend
    if money_capital < 0:
        print("Количество месяцев, которое можно протянуть без долгов:", value )
        break