# У вас есть три числа, они вводятся из консоли.
# Первое число называется fizz, второе называется buzz.
# До третьего необходимо досчитать от единицы.
# Считая, надо выводить число.
# Если число кратно fizz - надо выводить F вместо числа.
# Если число кратно buzz - надо выводить B вместо числа.
# Если число кратно и fizz и buzz, надо выводить FB.
# И так - пока не будет достигнуто третье введенное число.

fizz = int(input('Input first number:'))
buzz = int(input('Input second number:'))
n = int(input('Input third number:'))
x = 1

for x in range(1, 1 + n):
    if x % fizz == 0 and x % buzz == 0:
        print("FB", end=" ")
    elif x % fizz == 0:
        print('F', end=" ")
    elif x % buzz == 0:
        print('B', end=" ")
    else:
        print(x, end=" ")

# Введены числа 2, 5, 18
# Вывод должен быть таким:
# 1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F
