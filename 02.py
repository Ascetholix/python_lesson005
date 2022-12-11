# В файле находиться N элементов натуральных чисел, записаных через пробел.
# Среди чисел нехватает одного, чтобы выпольнить условия a[i]-1 = a[i-1]
# Найдите его
# 4 5 6 7 9
from pathlib import Path

filePath = Path('text', 'test01.txt')
ls = []
with open(filePath, 'r') as file:
  # lst = file.read().split()
  # lst = list(map(int,lst))
  lst = list(map(int,file.read().split()))  # в одну строку
  for i in range(1,len(lst)):
    if lst[i]-1 != lst[i-1]:
      ls.append(lst[i]-1)
      print(lst[i])

    
print(lst)
print(ls)