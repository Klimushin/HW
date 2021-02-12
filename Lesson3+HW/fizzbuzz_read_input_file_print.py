# Написать fizzbuzz для 20 троек чисел, которые
# записаны в файл. Читаете из файла первую строку,
# берете из нее числа, считаете для них fizzbuzz,
# выводите. Файл для входящих данный input.txt


file_input = open('input.txt', 'r')
 
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
   string = " ".join(str(a) for a in results)
   print(string)
 
file_input.close()
