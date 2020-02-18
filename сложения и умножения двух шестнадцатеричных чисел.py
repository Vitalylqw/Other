#  Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
#  элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
#  Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
#  задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
#  Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
from collections import deque

def sum (a,b):
    c=deque()
    modulo=0
    for i in range(1,len(a)+1):
         if i<=len(b):
            num=check_list.index(a[len(a)-i])+check_list.index(b[len(b)-i])
            c.appendleft(check_list[(num+modulo)%16])
            modulo=(num+modulo)//16
         else:
            num = check_list.index(a[len(a)-i])
            c.appendleft(check_list[(num + modulo) % 16])
            modulo = (num + modulo) // 16
    if modulo==1:
        c.appendleft('1')
    return list(c)

def multiplication(a,b):
    answer=[]
    z=0
    for i in reversed(a):
        c = deque()
        modulo = 0
        for j in reversed(b):
            num = check_list.index(i) * check_list.index(j)
            c.appendleft(check_list[(num + modulo) % 16])
            modulo = (num + modulo) // 16
        if modulo!=0:
            c.appendleft(check_list[modulo])
        c=list(c)
        c+=['0']*z
        z+=1
        answer=sum(c,answer)
    return answer

def insert_number():
    print('введите поочередно символы 16-го числа, начиная с левого. По окончании нажмите q')
    lst=[]
    # check_list=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','Q']
    while True:
        answer=input('введите очередной символ').upper()
        if answer in check_list:
            if answer=='Q':
                return lst
            lst.append(answer)
        else:
            print('Введите корректные данные')


check_list=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','Q']
a=insert_number()
b=insert_number()
operand=input('введите операцию: + или *')
if operand=='+':
    if len(a)>=len(b):
        result = sum(a, b)
    else:
        result = sum(b, a)
elif operand=='*':
    if len(a)>=len(b):
        result = multiplication(a, b)
    else:
        result = multiplication(b, a)
else:
    result='Вы ввели не корректные данные'
print(result)
print("Проверка сумма")
print(hex(int(''.join(a),16)+int(''.join(b),16)))
print('Проверка произведение')
print(hex(int(''.join(a),16)*int(''.join(b),16)))



# print(sum(['F', '9', 'F'],['A', '8','F']  ))
# print(hex(0xf9f+0xa8f))
# print(multiplication(['A', '2'],['C', '4','F']  ))