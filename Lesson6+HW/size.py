# Написать функцию перевода размеров женского белья из
# международного во все остальные. Внтри функции нужно
# просто обращаться к правильно составленному словарю.


xxs = {'rus' : 42, 'ger' :  36, 'usa' : 8, 'fr' : 38, 'gb' : 24}
xs = {'rus' : 44, 'ger' : 38, 'usa' : 10, 'fr' : 40, 'gb' : 26}
s = {'rus' : 46, 'ger' : 40, 'usa' : 12, 'fr' : 42, 'gb' : 28}
m = {'rus' : 48, 'ger' : 42, 'usa' : 14, 'fr' : 44, 'gb' : 30}
l = {'rus' : 50, 'ger' : 44, 'usa' : 16, 'fr' : 46, 'gb' : 32}
xl = {'rus' : 52, 'ger' : 46, 'usa' : 18, 'fr' : 48, 'gb' : 34}
xxl = {'rus' : 54, 'ger' : 48, 'usa' : 20, 'fr' : 50, 'gb' : 36}
xxxl = {'rus' : 56, 'ger' : 50, 'usa' : 22, 'fr' : 52, 'gb' : 38}


a = input ("Введите размер в международном формате: \n")
a = a.lower()
if a=="xxs":
    print (xxs)
elif a=="xs":
    print (xs)
elif a=="s":
    print (s)
elif a=="m":
    print (m)
elif a=="l":
    print (l)
elif a=="xl":
    print (xl)
elif a=="xxl":
    print (xxl)
elif a == "xxxl":
    print(xxxl)
else:
    print ("Размер не определён")
