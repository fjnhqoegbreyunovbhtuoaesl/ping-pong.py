from pygame import *
from random import randint

font.init()
font1 = font.SysFont('Verdana', 25)

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
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
display.set_caption('Shooter')
background = transform.scale(image.load('background1.jpg'), (700, 500))
clock = time.Clock()
FPS = 60

racket1 = Player('racket.png',5 ,200, 50, 150, 7)
racket2 = Player('racket.png',650 ,200, 50, 150, 7)
ball = GameSprite('tenis_ball.png',200 ,200, 50, 50, 5)
speed_x = 5
speed_y = 5
winner1 = font1.render("Player 1 win!", True, (255, 255, 255))
winner2 = font1.render("Player 2 win!", True, (255, 255, 255))

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if  finish != True:
        window.blit(background, (0, 0))
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(winner2, (300, 250))
    if ball.rect.x > 700:
            finish = True
            window.blit(winner1, (350, 250))
    display.update()
    clock.tick(FPS)
