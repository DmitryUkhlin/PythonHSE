salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
capital = 0

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

#print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", ...)

for months in range(0, 11):
    if months == 0:
        capital += salary-spend
    else:
        spend += spend * increase
        capital += salary - spend
        months += 1
    if months == 10:
        capital *= -1
        print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {capital:.2f}")

