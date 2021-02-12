# Написать fizzbuzz для 20 троек чисел,
# которые записаны в файл input.txt. Читаете 
# из файла первую строку, берете из нее числа,
# считаете для них fizzbuzz, записываете полученные
# значения в файл result.txt.

file_input = open('input.txt', 'r')

with open('result.txt', 'w') as writer:
    for line in file_input:
        first, second, third = line.split(" ")
        fizz = int(first)
        buzz = int(second)
        n = int(third)
        results = []
        x = 1
        while x <= n:
            if x % fizz == 0 and x % buzz == 0:
                results.append('FB')
            elif x % fizz == 0:
                results.append('F')
            elif x % buzz == 0:
                results.append('B')
            else:
                results.append(x)
            x += 1

        str_to_file = ''
        for res in results:
            str_to_file += "%s " % res
        str_to_file += '\n'
        writer.write(str_to_file)

file_input.close()
