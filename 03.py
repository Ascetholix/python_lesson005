# Дан список чисел. Создайте список, в который попадають числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# 1, 5, 2, 3, 4, 6, 1, 7 -> 1, 5, 6, 7 и тд

lst = [1, 5, 2, 3, 4, 6, 1, 7]
ls =[]
ls.append(lst[0])
for i in range(len(lst)):
  if lst[i]>ls[-1]:
    ls.append(lst[i])
      
print(lst)
print(ls)