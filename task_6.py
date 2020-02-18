# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random
# сгенерируем массив arrow из случаных чисел, нем будем анализировать элементы
arrow=[random.randint(-100,100) for _ in range (0,10)]
print(arrow)
if arrow[0]>=arrow[1]:
    min_first, min_second=arrow[0],arrow[1]
else:
    min_first, min_second = arrow[1], arrow[0]
for i in arrow:
    if i<min_first:
        min_second,min_first=min_first,i
    elif i<min_second:
        min_second=i
print(f"Самое маленькое число в массиве {min_first} , второе {min_second}")


