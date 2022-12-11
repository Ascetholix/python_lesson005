# Создайте программу для игры в ""Крестики-нолики"".
import pygame

pygame.init()# инициализация экрана

def win_user(mas,sing): # Функция проверки на выигрыш
  zero = 0
  for row in mas:
    zero += row.count(0)
    if row.count(sing)==3:
      return sing
  for col in range(3):
    if mas[0][col] == sing and mas[1][col] == sing and mas[2][col] == sing:
      return sing
  if mas[0][0] == sing and mas[1][1] == sing and mas[2][2] == sing:
    return sing
  if mas[0][2] == sing and mas[1][1] == sing and mas[2][0] == sing:
    return sing
  if zero == 0:
    return 'Piece'
  return False  

size_block = 100 # Размер блока
margin = 10 # Размер отступа
width = heidth = size_block*3 + margin*4 # Размер поля
size_win = (width,heidth)     # размер окна

# Цвета
RED = (255,0,0)   
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

img = pygame.image.load("games.png")    # иконка
pygame.display.set_icon(img)

user = 0 # Переменная для очередности
mass = [[0]*3 for i in range(3)] # Массив заполненый нулями

win = pygame.display.set_mode(size_win) # Окно игры
pygame.display.set_caption("Крестики нолики") # название окна

game_ower =False

while True:      # Основной цикл игры
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()
      
    elif event.type == pygame.MOUSEBUTTONDOWN and not game_ower:
      x_mouse, y_mouse = pygame.mouse.get_pos()  # возрашает место нажития те есть координаты
      print(f'x = {x_mouse} y = {y_mouse}')
      x_col = x_mouse//(margin+size_block) # Номер колонки
      y_row = y_mouse//(margin+size_block) # Номер ряда
    
      if mass[y_row][x_col] ==0: #Услови не заполнения повторно 
        if user%2==0:        # Условия проверки очедности
          mass[y_row][x_col] = 'x'
        else:
          mass[y_row][x_col] = 'o'
        user+=1
    #  Если поля польны игра перезагружеаться при нажатии SPACE пробел
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # 
      game_ower =False
      mass = [[0]*3 for i in range(3)]
      user = 0 
      win.fill(BLACK)
      
  if not game_ower:    
    for row in range(3):
      for col in range(3):
        if mass[row][col] == 'x':
          color = RED
        elif mass[row][col] == 'o':
          color = GREEN
        else:
          color = WHITE
          
        x = col*size_block+(col+1)*margin
        y = row*size_block+(row+1)*margin
        pygame.draw.rect(win,color,(x,y,size_block,size_block))
        # Рисуем Х и О
        if color==RED:
          # Линия от правого верхного угла в левый нижный
          pygame.draw.line(win, WHITE,(x+10,y+10),(x+size_block-10,y+size_block-10),4)
          # Линия от левого верхного угла вправый нижный
          pygame.draw.line(win, WHITE,(x+size_block-10,y+10),(x+10,y+size_block-10),4)
        elif color == GREEN:
          # Круг с центром x,y разделение на ширину блока и радиус как ширина болоак //2
          pygame.draw.circle(win,WHITE,(x+size_block//2,y+size_block//2), size_block//2-5,4)  
          
  if (user-1)%2 == 0:     # x      
    game_ower = win_user(mass,'x')
  else:
    game_ower = win_user(mass,'o')
    
  if game_ower: # Если игра окончено выводим текст
    win.fill(BLACK)
    font = pygame.font.SysFont('consolas', 80)
    text = font.render(game_ower, True, WHITE)
    
    text_rect = text.get_rect() # Находим  координаты текста
    text_x = win.get_width()/2-text_rect.width/2
    text_y = win.get_height()/2-text_rect.height/2
    win.blit(text,(text_x,text_y)) 
      
  pygame.display.update() # потом обявляем экран