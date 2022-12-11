# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'Я люблю Джавуабв абви Питон'
# 'Я люблю Питон'

def f(text, list):              # Через вклбчение
  list  = [x for x in list if text not in x]
  return list

def f1(text, ls):              # Через лямбду и филтер
  lis  = list(filter(lambda x: text not in x, ls))
  return lis

txt = 'Я люблю Джавуабв абви Питон'
lst = txt.split()
tx = 'абв'
lis = []

for i in lst:                 # обычный цикл проверки
  if tx not in i:
    lis.append(i)
    
listOne = list(filter(lambda x: tx not in x, txt.split())) ###### В одну сроку !!!!

print(*lst)               # * - звездечка распаковка списка
print(*lis)
print(*f(tx,lst))
print(*f1(tx,lst))
print(*listOne)

