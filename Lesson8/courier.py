# Задача 1. Курьер
# Вам известен номер квартиры, этажность дома и
# количество квартир на этаже. Задача: написать функцию,
# которая по заданным параметрам напишет вам, в какой
# подъезд и на какой этаж подняться, чтобы найти искомую квартиру.

def calculate(count_entrance, count_floor, flats):
    entrance  = int(1 + (flats - 1) / count_entrance )  
    floor  = int(1 + ((flats - 1) % count_entrance ) / count_floor)  
    print("Подъезд: %d" % entrance )
    print("Этаж: %d" % floor)


number = int(input("Введите номер квартиры: \n"))
a = 15  # количество квартир в подъезде
b = 3  # количество квартир на этаже
calculate(a, b, number)
