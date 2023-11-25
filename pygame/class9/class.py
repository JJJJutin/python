######################匯入模組######################
import pygame
import sys
import os
from pygame.locals import *
import random
from collections import deque

####################Queue######################
max_enemies = 3

enemies_queue = deque(maxlen=max_enemies)

active_enemies = []
enemies_delay = 0
enemies_delay_max = 20


######################障礙物物件######################
class Obstacle:
    def __init__(self, x, y, img: list[pygame.Surface], shift):
        self.x = x
        self.y = y
        self.img = img
        self.shift = shift
        self.center_x = x + img[0].get_width() / 2
        self.center_y = y + img[0].get_height() / 2
        self.detect_r = max(img[0].get_width(), img[0].get_height()) / 2
        self.index = 0

    def initial(self):
        self.x = bg_x - 100
        self.center_x = self.x + self.img[0].get_width() / 2
        self.center_y = self.y + self.img[0].get_height() / 2
        self.index = 0

    def move(self):
        self.x = (self.x - self.shift) % (bg_x - 100)
        self.index = (self.index - 1) % len(self.img)
        self.center_x = self.x + self.img[self.index].get_width() / 2
        self.center_y = self.y + self.img[self.index].get_height() / 2
        screen.blit(self.img[self.index], (self.x, self.y))


class Cacti(Obstacle):
    def __init__(self, x, y, img: list[pygame.Surface], shift: int):
        super().__init__(x, y, img, shift)
        self.detect_r = self.detect_r - 15


class Ptera(Obstacle):
    def __init__(self, x, y, img: list[pygame.Surface], shift: int):
        super().__init__(x, y, img, shift)
        self.detect_r = self.detect_r - 10


####################定義函式######################
def bg_update():
    global bg_roll_x

    bg_roll_x = (bg_roll_x - 10) % bg_x
    screen.blit(img, (bg_roll_x - bg_x, 0))
    screen.blit(img, (bg_roll_x, 0))


def move_dinosaur():
    global ds_y, jumpState, jumpValue, ds_index, ds_center_x, ds_center_y, ds_detect_r
    if dino_down:
        jumpState = False
        ds_y = LIMIT_LOW + 20
    if jumpState and not dino_down:
        if ds_y >= LIMIT_LOW:
            jumpValue = -jump_height
        if ds_y <= 0:
            jumpValue = jump_height
        ds_y += jumpValue

        jumpValue += 1

        if jumpValue < 0:
            jumpValue += 1
        else:
            jumpValue += 1

        if ds_y >= LIMIT_LOW:
            jumpState = False
            ds_y = LIMIT_LOW
    ds_index = (ds_index - 1) % len(ds_show)

    ds_center_x = ds_x + ds_show[ds_index].get_width() / 2
    ds_center_y = ds_y + ds_show[ds_index].get_height() / 2

    ds_detect_r = min(ds_show[0].get_width(), ds_show[0].get_height()) / 2

    screen.blit(ds_show[ds_index], (ds_x, ds_y))


def score_update():
    score_sur = score_font.render(str(score), False, RED)
    screen.blit(score_sur, (10, 10))


def is_hit(x1, y1, x2, y2, r):
    if ((x1 - x2) ** 2 + (y1 - y2) ** 2) < (r * r):
        return True
    else:
        return False


def game_over():
    screen.blit(img_gg, ((bg_x - gg_w) / 2, (bg_y - gg_h) / 2))


def add_enemy_to_queue():
    """隨機選擇一個敵人加入到隊列中"""
    enemy_type = random.choice(["cacti", "ptera"])  # 隨機選擇仙人掌或翼龍
    if len(enemies_queue) < max_enemies:  # 如果隊列中的敵人數量小於最大敵人數量
        enemies_queue.append(enemy_type)  # 將新敵人加入隊列
    # 在畫面右上角顯示目前對列中的敵人縮圖
    for i, enemy in enumerate(enemies_queue):
        # enumerate(enemies_queue)的意思是將enemies_queue中的元素依序取出，並且給予一個編號
        if enemy == "cacti":
            screen.blit(img_cacti, (bg_x - max_enemies * 50 + i * 50, 0))
        elif enemy == "ptera":
            screen.blit(img_ptera[0], (bg_x - max_enemies * 50 + i * 50, 0))


def create_enemies():
    """隨機決定是否召喚隊列中的敵人"""
    global active_enemies, score, gg, enemies_delay
    enemies_delay = (enemies_delay - 1) % enemies_delay_max  # 敵人出現間隔計數
    if len(enemies_queue) > 0 and enemies_delay == 0:
        enemy_type = enemies_queue.popleft()  # 將隊列中的敵人取出
        if enemy_type == "cacti":
            active_enemies.append(Cacti(bg_x - 100, LIMIT_LOW, [img_cacti], 10))
        elif enemy_type == "ptera":
            active_enemies.append(Ptera(bg_x - 100, PTERA_LIMIT_LOW, img_ptera, 10))
    for enemy in active_enemies:
        enemy.move()
        gg = is_hit(
            ds_center_x,
            ds_center_y,
            enemy.center_x,
            enemy.center_y,
            enemy.detect_r + ds_detect_r,
        )
        if gg:
            break
        if enemy.x <= 0:
            score += 1
            active_enemies.remove(enemy)


####################初始化######################
os.chdir(sys.path[0])
pygame.init()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIMIT_LOW = 140
PTERA_LIMIT_LOW = 110
clock = pygame.time.Clock()
####################載入圖片物件######################
img = pygame.image.load("bg.png")
img_dinosaur = [
    pygame.image.load("小恐龍1.png"),
    pygame.image.load("小恐龍2.png"),
]
img_cacti = pygame.image.load("cacti.png")
img_ptera = [pygame.image.load("翼龍飛飛1.png"), pygame.image.load("翼龍飛飛2.png")]
img_gg = pygame.image.load("gameover.png")
img_dino_down = [pygame.image.load("小恐龍蹲下1.png"), pygame.image.load("小恐龍蹲下2.png")]

bg_x = img.get_width()
bg_y = img.get_height()
bg_roll_x = 0
######################建立視窗######################
screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("Dinosaur")
######################分數物件######################
score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 36)
######################恐龍物件######################
ds_x = 50
ds_y = LIMIT_LOW
ds_index = 0
jumpState = False
jumpValue = 0
jump_height = 20
ds_center_x = ds_x + img_dinosaur[0].get_width() / 2
ds_center_y = ds_y + img_dinosaur[0].get_height() / 2

ds_detect_r = min(img_dinosaur[0].get_width(), img_dinosaur[0].get_height()) / 2
ds_show = img_dinosaur
dino_down = False


######################遊戲結束物件######################
gg = False
gg_w = img_gg.get_width()
gg_h = img_gg.get_height()
######################循環偵測######################
while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and ds_y <= LIMIT_LOW:
                jumpState = True
            elif event.key == K_DOWN:
                dino_down = True
                ds_show = img_dino_down
            if event.key == K_RETURN:
                score = 0
                gg = False
                ds_y = LIMIT_LOW
                jumpstate = False
                active_enemies.clear()
        if event.type == pygame.KEYUP:
            if event.key == K_DOWN:
                dino_down = False
                ds_show = img_dinosaur
                ds_y = LIMIT_LOW

    if gg:
        game_over()
    else:
        bg_update()
        move_dinosaur()
        score_update()
        add_enemy_to_queue()
        create_enemies()

    pygame.display.update()
