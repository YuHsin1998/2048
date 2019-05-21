#!/usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
import sys
from random import *
from math import pi
import random
background_image_filename = '20.png'
PIXEL = 150  
SCORE_PIXEL = 100  
SIZE = 4 
global scores
global max_sco
max_sco = 0
scores = 0
pygame.init();
screen = pygame.display.set_mode((490, 650), 0, 32)
pygame.display.set_caption("Hello, World!")
background = pygame.image.load(background_image_filename).convert()
Size = 4
class Button(object):
	def __init__(self, name, col,position, size):
		self.name = name
                self.col = col
                self.size = size
		self.position = position
	def isOver(self):
		point_x,point_y = pygame.mouse.get_pos()
		x, y = self. position
		w, h = self.size
		in_x = x - w < point_x < x
		in_y = y - h < point_y < y
		return in_x and in_y
	def render(self):
		w, h = self.size
		x, y = self.position
                pygame.draw.rect(screen, self.col, ((x - w, y - h), (w, h)), 0)
		num_font = pygame.font.Font(None, h - 1)
                font_test=num_font.render(self.name, True, (255, 255, 255))
                fsetting = font_test.get_rect()
                fsetting.center = (x - w / 2, y - h / 2)
                screen.blit(font_test,fsetting)
def cal(x):
   t = -1;
   while (x > 0):
       t += 1;
       x /= 2;
   return colours[t]
def add_scores(x):
   global scores
   scores +=  x
   global max_sco
   if (scores > max_sco):
        max_sco = scores
def map_init():
   screen.fill((250, 248, 239))
   screen.blit(background, (14,25))
   submap = pygame.Surface((436, 436))
   submap.fill((187, 173, 160)) 
   block = pygame.Surface((95, 95)) 
   screen.blit(submap, (30, 185))
   global scores
   button.name = str(scores) 
   button.render()
   global max_sco
   menu.name = str(max_sco) 
   menu.render()
   for i in range(Size):
     for j in range(Size):
        x = 30 + (i + 1) * 8 + i * 100;
        y = 185 + (j + 1) * 8 + j * 100;
        block.fill((205, 193, 180)) 
        screen.blit(block, (x, y))
        if (a[i][j] == 0):
           continue
        block.fill(cal(a[i][j]))
        screen.blit(block, (x, y))
        if (a[i][j] <= 4):
            font_test=num_font.render(str(a[i][j]), True, (119, 110, 101))
        else: 
            font_test=num_font.render(str(a[i][j]), True, (249, 246, 242))
        fsetting = font_test.get_rect()
        fsetting.center = (x + 50, y + 50)
        screen.blit(font_test,fsetting)
def puts(s):
   font_test=num_font.render(s	, True, (100, 100, 0))
   fsetting = font_test.get_rect()
   fsetting.center = (500, 50)
   screen.blit(font_test,fsetting)
   pygame.display.update()
def data_init():
   for i in range(4):
     for j in range(4):
       a[i][j] = 0;
   x1 = 0
   x2 = 0
   y1 = 0
   y2 = 0
   while((x1 == x2 and y1 == y2)):
       x1 = random.randint(0, 3)
       x2 = random.randint(0, 3)
       y1 = random.randint(0, 3)
       y2 = random.randint(0, 3)
   a[x1][y1] = 2;
   a[x2][y2] = 2;
def insert():
   ran = random.randint(0, 7)
   if (ran == 0):
       num = 8
   elif (ran <= 2):
       num = 4
   else:
       num = 2
   x = random.randint(0, 3)
   y = random.randint(0, 3)
   while(a[x][y] != 0):
      x = random.randint(0, 3)
      y = random.randint(0, 3)
   a[x][y] = num
def push_down():
  for j in range(4):
      bol = [0 for x in range(4)]
      i = 2;
      while (i >= 0):
          while(i + 1<= 3 and a[i][j] != 0 and a[i + 1][j] == 0):
              a[i + 1][j] = a[i][j]
              a[i][j] = 0
              i += 1
          if (i < 3 and bol[i + 1] == 0 and a[i][j] == a[i + 1][j]):
              a[i + 1][j] = a[i + 1][j] * 2
              add_scores( a[i + 1][j])
              a[i][j] = 0
              bol[i + 1] = 1
          i -= 1
def down_zero():
  for j in range(4):
    for i in range(0, 3):
      if (a[i][j] != 0 and a[i + 1][j] == 0):
        return True
  return False
def up_zero():
  for j in range(4):
    for i in range(1, 4):
      if (a[i][j] != 0 and a[i - 1][j] == 0):
        return True
  return False
def left_zero():
     for i in range(4):
         for j in range(1, 4):
            if (a[i][j] != 0  and a[i][j - 1] == 0):
                return True
     return False 
def right_zero():
     for i in range(4):
         for j in range(0, 3):
            if (a[i][j] != 0  and a[i][j + 1] == 0):
                return True
     return False 
def check_column():
  for j in range(4):
     x = 0
     for i in range (4):
         if (a[i][j] != 0 and a[i][j] == x):
             return True
         else :
             x = a[i][j]
  return False
def check_row():
   for i in range(4):
       x = 0
       for j in range (4):
           if (a[i][j] != 0 and a[i][j] == x):
               return True
           else:
               x = a[i][j]
   return False
def has_zero():
   for i in range(4):
     for j in range(4):
        if (a[i][j] == 0) :
           return True
   return False
def alter():
   dx = [0, 1, 0, -1]
   dy = [1, 0, -1, 0]
   for i in range(4):
      for j in range(4):
         for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if (x >= 0 and x < 4 and y >= 0 and y <4 and a[x][y] == a[i][j]):                
               return True
   return False
def game_over():
   if (has_zero() == True  or alter() == True):
       return False
   return True   
def push_up():
   for j in range(4):
       bol = [0 for x in range(4)]
       i = 1;
       while(i < 4):
          while(i > 0 and a[i][j] != 0 and a[i - 1][j] == 0):
              a[i - 1][j] =a[i][j];
              a[i][j] = 0;
              i -=1
          if (i > 0 and bol[i - 1] == 0 and a[i][j] == a[i - 1][j]):
              a[i - 1][j] *= 2; 
              add_scores(a[i - 1][j])
              a[i][j] = 0;
              bol[i - 1] = 1;
          i += 1
def push_left():
   for i in range(4):
       bol = [0 for x in range(4)]
       j = 1;
       while(j < 4):
           while (j > 0 and a[i][j] != 0 and a[i][j - 1] == 0):
               a[i][j - 1] = a[i][j]
               a[i][j] = 0
               j -= 1
           if (j > 0 and bol[j - 1] == 0 and a[i][j] == a[i][j - 1]):
               a[i][j - 1] *= 2
               add_scores(a[i][j - 1])
               a[i][j] = 0
               bol[j - 1] = 1;
           j += 1
def push_right():
   for i in range(4):
       bol = [0 for x in range(4)]
       j = 4;
       while(j >= 0):
           while(j < 3 and a[i][j + 1] == 0 and a[i][j] != 0):
               a[i][j + 1] = a[i][j]
               a[i][j] = 0
               j += 1
           if (j < 3 and bol[j] == 0 and a[i][j] == a[i][j + 1]):
               a[i][j + 1] *= 2
               add_scores(a[i][j + 1])
               a[i][j] = 0
           j -= 1
def ply_with():
   pygame.draw.rect(screen, (0, 255, 0), ((200, 5), (100, 100)), 10)
   pygame.draw.rect(screen, (255, 255, 0), ((310, 5), (105, 100)), 10)
   pygame.draw.rect(screen, (0, 0, 255), ((200, 115), (100, 100)), 10)
num_font = pygame.font.Font(None, 62)
a = [[0 for col in range(4)] for row in range(4)]  
colours = [(238, 228, 218), (237, 224, 200), (242, 177, 121), (245, 149, 99), (245, 129, 96), (246, 94, 59), (237, 207, 114), (237, 204, 97), (237, 200, 80), (255, 215, 0), (255, 140, 0)]
data_init()
button = Button("New", (187, 173, 160),(360,87),(85, 25))
menu = Button("Menu", (187, 173, 160),(463,87),(85, 25))
tr = Button("Menu", (0, 0, 0),(469,143),(113, 37))
while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           exit()
       elif event.type ==  MOUSEBUTTONDOWN:
           if (tr.isOver() == True): 
                data_init()
                scores = 0
       elif event.type == KEYDOWN:
           delta = False
           if  event.key == K_LEFT:
               if (check_column() == True  or  up_zero() == True):
                  push_up()
                  delta = True
           elif  event.key == K_RIGHT:
               if (check_column() == True  or  down_zero() == True):
                  push_down()
                  delta = True
           elif  event.key == K_UP:
               if (check_row() == True  or  left_zero() == True):
                  push_left()
                  delta = True
           elif  event.key == K_DOWN: 
               if (check_row() == True  or  right_zero() == True):
                  push_right()
                  delta = True
           if (delta == True and has_zero() == True):
               insert()
           if (game_over() == True):
               print "Loser"
           map_init()
    map_init()
    pygame.display.update()
