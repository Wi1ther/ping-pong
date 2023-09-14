from pygame import *
window = display.set_mode((700,500))
display.set_caption("ping-pong")
background = transform.scale(image.load('images.jpeg'),(700, 500))
game = True
FPS = 60
clock = time.Clock()
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)