from pygame import *
font.init()
font1 = font.Font(None,36)
lost1 = font1.render('Первый игрок приграл',True,(0,0,0))
lost2 = font1.render('Второй игрок проиграл',True,(0,0,0))
window = display.set_mode((700,500))
display.set_caption("ping-pong")
background = transform.scale(image.load('images.jpeg'),(700, 500))
game = True
FPS = 60
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, x, y ,wight ,hight , spriteImage, speed):
        super().__init__()
        self.image = transform.scale(image.load(spriteImage),(wight, hight))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.wight = wight
        self.hight = hight
        self.speed = speed
    def drow(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def moveL(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500 - self.hight:
            self.rect.y += self.speed
    def moveR(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 500 - self.hight:
            self.rect.y += self.speed
finish = False
speedX = 3
speedY = 3
rocet1 = Player(0,250,50,150,'rocet.png',5)
rocet2 = Player(650,250,50,150,'rocet.png',5)
ball = GameSprite(350,250,30,30,'ball.jpeg',5)
while game:
    for e in event.get():
        if e.type == QUIT:  
            game = False
    if finish != True:
        window.blit(background,(0,0))
        rocet1.moveL()
        rocet2.moveR()
        ball.rect.x += speedX
        ball.rect.y += speedY
        if ball.rect.y < 0 or ball.rect.y > 500-ball.hight:
            speedY = speedY*(-1)
        if sprite.collide_rect(rocet1,ball) or sprite.collide_rect(rocet2,ball):
            speedY = speedY*(-1)
            speedX = speedX*(-1)
        if ball.rect.x < 0:
            finish = True
            window.blit(lost1,(250,250))
        if ball.rect.x > 700-ball.wight:
            window.blit(lost2,(250,250))
            finish = True
    rocet1.drow()
    rocet2.drow()
    ball.drow()
    display.update()
    clock.tick(FPS)
