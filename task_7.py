# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
#  Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

arrow=[[int(input(f'введите значение {i} элеимента {j} строки')) for i in range(1,4)] for  j in range(1,6)]
for i in arrow:
    for j in i:
        print(f'{j:<4}',end='')
    print('')
print("-"*15)
for i in arrow:
    sum = 0
    for j in i:
        sum+=j
    i.append(sum)
for i in arrow:
    for j in i:
        print(f'{j:<4}',end='')
    print('')