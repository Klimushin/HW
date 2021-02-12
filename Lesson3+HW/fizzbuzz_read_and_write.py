# Написать fizzbuzz для 20 троек чисел,
# которые записаны в файл input.txt. Читаете из файла
# первую строку, берете из нее числа, считаете
# для них fizzbuzz, результат записывается в файл output.txt.

file_input = open('input.txt', 'r')
file_output = open("output.txt", "w")
 
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
   string =(" ".join(str(a) for a in results)+"\n")
   file_output.write(string)
    
file_input.close() 
file_output.close()

