# сумму списка при помощи while

l=[1,2,3,4,6,7]
sum1=0
index=0
list_lest_index=len(l) 
while index<list_lest_index:
  sum1+=l[index]
  index+=1
print(sum1)
