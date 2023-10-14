######################匯入模組######################
import pygame
import sys
import os
import random


####################定義函式######################
def gophers_update():
    global tick, pos
    if tick > max_tick:
        new_pos = random.randint(0, 5)
        pos = pos6[new_pos]
        tick = 0
    else:
        tick += 1
    pygame.draw.circle(screen, BLUE, pos, 50)


####################初始化######################
pygame.init()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()
tick = 0
max_tick = 20
######################建立視窗######################
bg_x = 600
bg_y = 400
screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("打地鼠")
######################背景物件######################
bg = pygame.Surface([bg_x, bg_y])
bg.fill(BLACK)
######################地鼠物件######################
pos6 = [[200, 200], [300, 200], [400, 200], [200, 300], [300, 300], [400, 300]]

pos = pos6[0]
######################分數物件######################

######################滑鼠物件######################

######################循環偵測######################
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(bg, (0, 0))
    gophers_update()

    pygame.display.update()