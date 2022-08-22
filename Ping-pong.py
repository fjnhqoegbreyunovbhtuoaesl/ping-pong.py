from pygame import *
from random import randint

mixer.init()

mixer.music.load('space.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
        self.direction = ' '

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed

window = display.set_mode((800, 500))
display.set_caption('Shooter')
background = transform.scale(image.load('background1.jpg'), (700, 500))
clock = time.Clock()

racket1 = Player('racket.png',5 ,200, 50, 150, 10)
racket2 = Player('racket.png',750 ,200, 50, 150, 10)
ball = GameSprite('tenis_ball.png',200 ,200, 50, 50, 5)

game = True
while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    racket1.reset()
    racket2.reset()
    ball.reset()
    display.update()
    clock.tick()
