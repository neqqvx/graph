import matplotlib.pyplot as plt
import numpy as np

# Случайно сгенерированные данные о количестве монет (для примера)
coins = np.random.choice([500, 1000, 1500, 2000, 2500, 3000, 3500, 4000], 30)

# Даты от 1 до 30
dates = np.arange(1, 31)

# Создаем график
plt.figure(figsize=(10, 6))
plt.plot(dates, coins, marker='o', linestyle='-', color='b')

# Называем оси
plt.xlabel('Дата')
plt.ylabel('Количество монет')

# Устанавливаем лимиты для осей
plt.xlim(1, 30)
plt.ylim(500, 4000)

# Добавляем сетку для удобства восприятия
plt.grid(True)

# Добавляем заголовок графика
plt.title('Количество монет на бирже по дням')

# Отображаем график
plt.show()