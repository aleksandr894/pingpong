#импорт библиотек
from pygame import *
font.init()

#Окно игры
bg_col = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(bg_col)

#Состояние игры
run = True
finish = False
clock = time.Clock()
FPS = 60

#Классы
class GameSprite(sprite.Sprite):
    def __init__(self, x, y, pic, speed, width, height):
        super().__init__()
        self.pic = pic
        self.image = transform.scale(image.load(pic), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, x, y, pic, speed, width, height):
        super().__init__(x, y, pic, speed, width, height)
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= 10
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += 10
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= 10
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += 10

#ракетки
racket1 = Player(10, 200, 'racket.png', 4, 50, 150)
racket2 = Player(540, 200, 'racket.png', 4, 50, 150)
pl1_lose = False
pl2_lose = False

delay = 100

#мяч
ball = GameSprite(275, 225, 'tenis_ball.png', 0, 50, 50)
speed_x = 3
speed_y = 3

#игровой цикл
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.fill(bg_col)
        if ball.rect.y >= 450:
            speed_y *= -1
        if ball.rect.y <= 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball):
            speed_x *= -1
        if sprite.collide_rect(racket2, ball):
            speed_x *= -1
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()
        if ball.rect.x <= 0:
            finish = True
            pl1_lose = True
        if ball.rect.x >= 550:
            finish = True
            pl2_lose = True
    else:
        if pl1_lose:
            lose = font.SysFont('Arial', 50).render('player 1 lose', True, (250, 0, 0))
        elif pl2_lose:
            lose = font.SysFont('Arial', 50).render('player 2 lose', True, (250, 0, 0))
        window.blit(lose, (190, 200))
        delay -= 1
        if delay == 0:
            pl1_lose = False
            pl2_lose = False
            ball.rect.x = 275
            ball.rect.y = 225
            finish = False
            delay = 60

    display.update()
    clock.tick(FPS)