n = int(input("Please, input number: \n"))
b = n/1000
n = n%1000
c = n/100
n = n%100
d = n/10
n = n%10
print (str(int(b))+"*1000"+"+"+str(int(c))+"*100"+"+"+str(int(d))+"*10"+"+"+str(n))
