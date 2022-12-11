# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint
import sys, subprocess

def clear():                                 # Функция очистка консоли
  subprocess.run('cls', shell=True)          # Для windows 'cls' для Linux и Мас 'clear'
  
coins = 2021
user1 = 0
user2 = 0
usercons1 = 0
usercons2 = 0
cout = randint(0,1)              # Рандомный счетчит для очередности играков


print('ИГРА С КОФЕТАМИ')
while coins != 0 and coins > 0: # пока конфеты != 0 и или меньше 0
  
  if cout == 1:
    user1 = int(input('Игрок 1 возмите конфет от 1 до 28: '))
    while user1 > 28 or coins < user1:
      clear()
      
      if user1 > 28:
        print('Вы взяли много возмите до 28')
      elif coins < user1:
        print(f'Вы взяли много возмите конфет от 1 до {coins}')

      user1 = int(input('Игрок 1 возмите конфеты: '))
    coins = coins - user1
    usercons1 += user1 
    
    cout = 0                              # счетчик 0 для передачи хода
    
  else:
    user2 = int(input('Игрок 2 возмите конфет от 1 до 28: '))
    while user2 > 28 or coins < user2:
      clear()
      
      if user2 > 28:
        print('Вы взяли много возмите до 28')
      elif coins < user1:
        print(f'Вы взяли много возмите конфет от 1 до {coins}')
    
      user2 = int(input('И грок 2 возмите конфеты: '))
    coins = coins - user2
    usercons2 += user2

    cout = 1                              # счетчик 1 для передачи хода
    
  clear()
  print(f'Осталось конфет = {coins}')
  print(f'Игрок 1 конфет = {usercons1}')
  print(f'Игрок 2 конфет = {usercons2}')
  
print('Конец игры!!!')

if cout == 0:           # Условия последнего хода
  usercons1 +=usercons2
  usercons2 = 0
  print('Последный ход Игрока 1')
  print('Все конфеты Игрока 2 переходят Игроку 1')
else:
  usercons2 +=usercons1
  usercons1 = 0
  print('Последный ход Игрока 2')
  print('Все конфеты Игрока 1 переходят Игроку 2')

print(f'Результат Игрок 1 = {usercons1}, Игрок 2 = {usercons2}')

if usercons2 < usercons1:
  print('Победил Игрок 1')
elif usercons2 > usercons1:
  print('Победил Игрок 2')
else:
  print('Ничья')
