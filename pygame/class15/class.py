######################載入套件######################
import pygame
import sys
import os
from pygame.locals import *
import random
from typing import List

######################常數設定######################


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


class Enemy:
    def __init__(self, x, y, image, shift, burn_img):
        self.x = x
        self.y = y
        self.image = image
        self.active = True
        self.shift = shift
        self.wh = image.get_width() // 2
        self.hh = image.get_height() // 2
        self.burn_shift = 0
        self.burn_img = burn_img
        self.burn_w, self.burn_h = burn_img.get_rect().size
        self.EXP: int = 0
        self.hit = False

    def move(self):
        if self.active:
            self.y += self.shift
            if self.y > bg_y:
                self.reset(*creat_enemy(), self.shift)

    def draw(self, screen):
        if self.active:
            self.burn_shift = (self.burn_shift + 2) % 6
            screen.blit(
                self.burn_img,
                [self.x - self.burn_w / 2, self.y - self.burn_h - self.burn_shift],
            )
            screen.blit(self.image, (self.x - self.wh, self.y - self.hh))

    def reset(self, x, y, image, shift):
        self.x = x
        self.y = y
        self.image = image
        self.active = True
        self.shift = shift
        self.wh = image.get_width() // 2
        self.hh = image.get_height() // 2
        self.EXP = 0
        self.hit = False


class FastMissile(Missile):
    def __init__(self, x, y, image, shift):
        super().__init__(x, y, image, shift)
        self.shift += 10


class PiercingMissile(Missile):
    def __init__(self, x, y, image, shift):
        super().__init__(x, y, image, shift)


class Powerup:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.wh = image.get_width() // 2
        self.hh = image.get_height() // 2
        self.active = True
        self.type = random.choice([FastMissile, PiercingMissile, Missile])

    def draw(self, screen):
        if self.active:
            self.y += 5
            screen.blit(img_powerup, (self.x - self.wh, self.y - self.hh))
            if self.y > bg_y:
                self.active = False


######################定義函式區######################
def roll_bg():
    global roll_y

    roll_y = (roll_y + 10) % bg_y
    screen.blit(img_bg, (0, roll_y - bg_y))
    screen.blit(img_bg, (0, roll_y))


def move_starship():
    global ss_x, ss_y, ss_wh, ss_hh, ss_img, burn_shift, ss_invincible

    key = pygame.key.get_pressed()
    ss_img = img_sship[0]
    if key[pygame.K_UP]:
        ss_y -= 20
    if key[pygame.K_DOWN]:
        ss_y += 20
    if key[pygame.K_LEFT]:
        ss_x -= 20
        ss_img = img_sship[1]
    if key[pygame.K_RIGHT]:
        ss_x += 20
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
    ss_invincible = max(0, ss_invincible - 1)
    if ss_invincible % 2 == 0:
        screen.blit(img_burn, [ss_x - burn_w / 2, ss_y + burn_h + burn_shift])
        screen.blit(ss_img, [ss_x - ss_wh, ss_y - ss_hh])


def is_hit(x1, y1, x2, y2, r):
    if ((x1 - x2) ** 2 + (y1 - y2) ** 2) < (r**2):
        return True
    else:
        return False


def score_update():
    global score

    score_sur = score_font.render(str(score), True, (255, 0, 0))
    screen.blit(score_sur, [10, 10])


def creat_enemy():
    emy_img = random.choice(emy_show)
    emy_wh = emy_img.get_width() // 2
    emy_x = random.randint(emy_wh, bg_x - emy_wh)
    emy_y = random.randint(-bg_y, -emy_wh)
    return emy_x, emy_y, emy_img


def draw_explode(enemy: Enemy):
    if 0 < enemy.EXP < 6:
        exp_w, exp_h = img_explode[enemy.EXP].get_rect().size
        screen.blit(img_explode[enemy.EXP], [enemy.x - exp_w / 2, enemy.y - exp_h / 2])
        enemy.EXP += 1


def shield_update():
    shield_w = img_shield.get_width() * ss_shield / 100
    shield_h = img_shield.get_height()
    screen.blit(img_shield, [0, bg_y - shield_h], [0, 0, shield_w, shield_h])  # 繪製保護罩


def show_gameover():
    screen.blit(
        img_gg, [bg_x / 2 - img_gg.get_width() / 2, bg_y / 2 - img_gg.get_height() / 2]
    )


######################初始化設定######################
os.chdir(sys.path[0])
pygame.init()
clock = pygame.time.Clock()
gameover = False
####################載入圖片######################
img_bg = pygame.image.load("space.png")
img_sship = [
    pygame.image.load("fighter_M.png"),
    pygame.image.load("fighter_L.png"),
    pygame.image.load("fighter_R.png"),
]
img_burn = pygame.image.load("starship_burner.png")
img_emy_burn = pygame.transform.rotate(img_burn, 180)
img_weapon = pygame.image.load("bullet.png")
bg_x = img_bg.get_width()
bg_y = img_bg.get_height()
bg_size = (bg_x, bg_y)
pygame.display.set_caption("Galaxy Launcer")
screen = pygame.display.set_mode(bg_size)
roll_y = 0
img_enemy = pygame.image.load("enemy1.png")
img_enemy2 = pygame.image.load("enemy2.png")
img_explode = [
    None,
    pygame.image.load("explosion1.png"),
    pygame.image.load("explosion2.png"),
    pygame.image.load("explosion3.png"),
    pygame.image.load("explosion4.png"),
    pygame.image.load("explosion5.png"),
]
img_shield = pygame.image.load("shield.png")
img_gg = pygame.image.load("gameover (1).png")

img_powerup = pygame.image.load("powerup.png")
######################遊戲視窗設定######################

######################玩家設定######################
ss_x = bg_x / 2
ss_y = bg_y / 2
ss_wh = img_sship[0].get_width() / 2
ss_hh = img_sship[0].get_height() / 2
ss_img = img_sship[0]

ss_invincible = 0  # 無敵時間
ss_shield = 100

burn_shift = 0
burn_w, burn_h = img_burn.get_rect().size
######################飛彈設定######################
msl_wh = img_weapon.get_width() / 2
msl_hh = img_weapon.get_height() / 2
msl_shift = 10  # 飛彈移動速度
MISSILE_MAX = 1000  # 飛彈數量

missiles = [
    PiercingMissile(0, 0, img_weapon, msl_shift) for _ in range(MISSILE_MAX)
]  # 飛彈列表
msl_cooldown = 0  # 飛彈冷卻時間
msl_cooldown_max = 0  # 飛彈冷卻時間上限

######################敵人設定######################
emy_show = [img_enemy, img_enemy2]

emy_shift = 5
# enemy = Enemy(*creat_enemy(), emy_shift)

# emy2_shift = 10
# enemy2 = Enemy(*creat_enemy(), emy_shift)
emy_list: list[Enemy] = []  # 敵人列表
emy_num = 10  # 敵人數量
for _ in range(emy_num):
    emy_list.append(Enemy(*creat_enemy(), emy_shift, img_emy_burn))
######################音樂設定######################
pygame.mixer.music.load("hit.mp3")
######################分數設定######################
score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 36)
######################道具列表######################
powerups: List[Powerup] = []
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

    if gameover:
        show_gameover()
    else:
        roll_bg()
        move_starship()

        msl_cooldown = max(0, msl_cooldown - 1)
        for missile in missiles:
            missile.move()
            missile.draw(screen)

        for enemy in emy_list:
            enemy.move()
            enemy.draw(screen)
            draw_explode(enemy)
            for missile in missiles:
                if missile.active and is_hit(
                    missile.x, missile.y, enemy.x, enemy.y, msl_wh + enemy.wh
                ):
                    if enemy.hit:
                        break

                    enemy.hit = True
                    if not isinstance(missile, PiercingMissile):
                        missile.active = False
                    enemy.active = False
                    score += 1
                    enemy.EXP = 1
                    pygame.mixer.music.play()
                    powerups.append(Powerup(enemy.x, enemy.y, img_powerup))
                    break

            if not enemy.active and enemy.EXP == 6:
                enemy.reset(*creat_enemy(), emy_shift)

            if (
                enemy.active
                and is_hit(ss_x, ss_y, enemy.x, enemy.y, ss_wh + enemy.wh)
                and ss_invincible == 0
            ):
                ss_invincible = 40
                score -= 1
                ss_shield -= 20

            if ss_shield <= 0:
                gameover = True
                break

        for powerup in powerups:
            powerup.draw(screen)
            if is_hit(powerup.x, powerup.y, ss_x, ss_y, powerup.wh + ss_wh):
                powerup.active = False
                missiles = [
                    powerup.type(0, 0, img_weapon, msl_shift)
                    for _ in range(MISSILE_MAX)
                ]
                if powerup.type == FastMissile:
                    msl_cooldown_max = 0
                else:
                    msl_cooldown_max = 10

                print(powerup.type, msl_cooldown_max)
            if not powerup.active:
                powerups.remove(powerup)
        shield_update()
        score_update()
    pygame.display.update()
