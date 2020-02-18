
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
import random,sys

def count_memory(object):
    return sys.getsizeof(object)


# Вариант 1
# сгенерируем массив arrow из случаных чисел
memory1=0
arrow=[random.randint(-100,100) for _ in range (0,10)]
print(arrow)
data_dic={max:[0,arrow[0]],min:[0,arrow[0]]} # в словаре будем хранить индекс и значение минимального и максимально элемента
for i,item in enumerate(arrow):
    if item>data_dic[max][1]:
        data_dic[max][1],data_dic[max][0]=item,i
    if item < data_dic[min][1]:
        data_dic[min][1], data_dic[min][0] = item, i
print(f'минимальное число {data_dic[min][1]}, максимальное число {data_dic[max][1]}')
arrow[data_dic[max][0]] ,  arrow[data_dic[min][0]]= data_dic[min][1], data_dic[max][1]
print("Измененный массив")
print(arrow)
