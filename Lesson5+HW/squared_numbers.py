# Написать функцию которая будет простое число
# возводить в квардрат. Необходимо возвести в
# квадрат все простые числа в списке,
# используя функцию map. Список задается последним
# его числом.

a=int(input("Укажите последнее число списка: \n"))

numbers = []

for num in range(2,a+1):
  if all(num%i!=0 for i in range(2,num)):
    numbers.append(num)  
print('Простые числа:','\n',numbers)

def my_square(num):
  return num ** 2

squared_numbers = list(map(my_square, numbers))

print('Квадраты простых чисел:','\n', squared_numbers, end="")


