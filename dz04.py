# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример
# SSSSOOOEEERROOOAAYYYYYDDDDOEUUUUUWWWWJJJO->S4O3E3R2O3A2Y5D4O1E1U5W4J3O1
# 41 ->28

def rle(string):
  temp_text =''
  result = ''
  count = 1

  for i in string:
    if i != temp_text:
      if temp_text:
        result+=temp_text+str(count)
      count = 1
      temp_text = i
    else:
      count+=1
  result+=temp_text+str(count)
  return result

def de_rle(string):
  result_index = ''
  result_text = ''
  result =''

  for i in range(0,len(string),2):
    result_index+=text[i+1]
    
  for i in range(0,len(string),2):
    result_text+=text[i]
    
  for i in range(len(result_index)):
    temp = result_text[i]*int(result_index[i])
    result+=temp
  return result
  
choice = 0  
while choice != 1 and choice !=2:
  choice = int(input('Выберите 1 - шифровка 2 - дешифровка: '))
if choice == 1:
  text = input('Введите текст шифровки:')
  print(f'Результат шифровки = {rle(text)}')
elif choice == 2:   
  text = input('Введите текст для дешифровки:') 
  print(f'Результат дешифровки = {de_rle(text)}')
else:
  print('Ошибка')
