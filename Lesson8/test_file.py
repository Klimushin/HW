# Задача 3. Файл-тест.
# Файл для проверки 1.txt
# Проверить каждую строку файла, если строка записана
# верно, вывести ее и после написать True, если строка
# не верна, вывести результат с пометкой False.


with open('1.txt', 'r') as file:
    for line in file:
        first_part, second_part = line.split(";")
        average, remainder = second_part.split(" ")
        data = list(map(int, (first_part.split(" "))))
        result = sum(data) // len(data) == int(average) and sum(data) % len(data) == int(remainder)
        print(line.strip('\n'), result, end='\n')
