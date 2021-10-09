flag = True
while flag:
    try:
        a = int(input('Введите натуральное число: '))
    except ValueError:
        print('Вы ввели не натуральное число. Повторите попытку')
    else:
        if a <= 0:
            print('Данное число не может быть отрицательным')
        else:
            flag = False
flag = True
while flag:
    try:
        c = int(input('Выберите в какую систему счисления желаете перевести (2 или 8): '))
    except ValueError:
        print('Вы ввели не 2 и не 8')
    else:
        if not (c == 2 or c == 8):
            print('Опять мимо')
        else:
            flag = False
          
n = ''

while a > 0:
    n = str(a % c) + n
    a //= c

print(n)

    
