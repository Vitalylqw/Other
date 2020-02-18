# Определить, какое число в массиве встречается чаще всего.
import random
# сгенерируем массив arrow из случаных чисел
arrow=[random.randint(-10,10) for _ in range (0,30)]
print(arrow)

max=0
# создадим список с уникальными значениями массива
arrow_set=list(set(arrow))
for i in arrow_set:
    count=arrow.count(i)
    if count>max:
        max=count
        nuber=i
print(f'Чаще всего число {nuber} встречается раз {max}')


