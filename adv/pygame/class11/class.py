######################載入套件######################
import pygame
import sys
import os
from pygame.locals import *


####################物件類別######################
class Missile:
    def __init__(self, x, y, image, shift):
        """初始化飛彈"""
        self.x = x
        self.y = y
        self.image = image
        self.active = False
        self.shift = shift

    def launch(self, x, y):
        """shoot"""
        if not self.active:
            self.x = x
            self.y = y
            self.active = True

    def move(self):
        """move"""
        if self.active:
            self.y -= self.shift
            if self.y < 0:
                self.active = False

    def draw(self, screen):
        """draw"""
        if self.active:
            screen.blit(self.image, (self.x, self.y))


######################定義函式區######################
def roll_bg():
    global roll_y

    roll_y = (roll_y + 10) % bg_y
    screen.blit(img_bg, (0, roll_y - bg_y))
    screen.blit(img_bg, (0, roll_y))


def move_starship():
    global ss_x, ss_y, ss_wh, ss_hh, ss_img, burn_shift

    key = pygame.key.get_pressed()
    ss_img = img_sship[0]
    if key[pygame.K_UP]:
        ss_y -= 50
    if key[pygame.K_DOWN]:
        ss_y += 50
    if key[pygame.K_LEFT]:
        ss_x -= 50
        ss_img = img_sship[1]
    if key[pygame.K_RIGHT]:
        ss_x += 50
        ss_img = img_sship[2]

    ss_hh = ss_img.get_height() / 2
    ss_wh = ss_img.get_width() / 2

    if ss_y < ss_hh:
        ss_y = ss_hh
    if ss_y > bg_y - ss_hh:
        ss_y = bg_y - ss_hh
    if ss_x < ss_wh:
        ss_x = ss_wh
    if ss_x > bg_x - ss_wh:
        ss_x = bg_x - ss_wh

    burn_shift = (burn_shift + 3) % 6
    screen.blit(img_burn, [ss_x - burn_w / 2, ss_y + burn_h + burn_shift])
    screen.blit(ss_img, [ss_x - ss_wh, ss_y - ss_hh])


######################初始化設定######################
os.chdir(sys.path[0])
pygame.init()
clock = pygame.time.Clock()
####################載入圖片######################
img_bg = pygame.image.load("space.png")
img_sship = [
    pygame.image.load("fighter_M.png"),
    pygame.image.load("fighter_L.png"),
    pygame.image.load("fighter_R.png"),
]
img_burn = pygame.image.load("starship_burner.png")
img_weapon = pygame.image.load("bullet.png")
bg_x = img_bg.get_width()
bg_y = img_bg.get_height()
bg_size = (bg_x, bg_y)
pygame.display.set_caption("Galaxy Launcer")
screen = pygame.display.set_mode(bg_size)
roll_y = 0
######################遊戲視窗設定######################

######################玩家設定######################
ss_x = bg_x / 2
ss_y = bg_y / 2
ss_wh = img_sship[0].get_width() / 2
ss_hh = img_sship[0].get_height() / 2
ss_img = img_sship[0]

burn_shift = 0
burn_w, burn_h = img_burn.get_rect().size
######################飛彈設定######################
msl_wh = img_weapon.get_width() / 2
msl_hh = img_weapon.get_height() / 2
msl_shift = 30
MISSILE_MAX = 10

missiles = [Missile(0, 0, img_weapon, msl_shift) for _ in range(MISSILE_MAX)]
msl_cooldown = 0
msl_cooldown_max = 1

######################主程式######################
while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_F11:
                screen = pygame.display.set_mode(bg_size, FULLSCREEN)
            elif event.key == K_ESCAPE:
                screen = pygame.display.set_mode(bg_size)

            if event.key == K_SPACE and msl_cooldown == 0:
                for missile in missiles:
                    if not missile.active:
                        missile.launch(ss_x - msl_wh, ss_y - msl_hh)
                        msl_cooldown = msl_cooldown_max
                        break

    roll_bg()
    move_starship()

    msl_cooldown = max(0, msl_cooldown - 1)
    for missile in missiles:
        missile.move()
        missile.draw(screen)

    pygame.display.update()
