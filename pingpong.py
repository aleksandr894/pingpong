from pygame import *
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
    
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= 10
        if keys[K_RIGHT] and self.rect.x < 635:
            self.rect.x += 10