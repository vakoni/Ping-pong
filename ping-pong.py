from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))  

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update_r(self):
        keys = key.get_pressed()
        if  keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed


window = display.set_mode((700, 500))
FPS = 60
blue = [176, 196, 222]
window.fill(blue)
Clock = time.Clock()
platform1= Player('platform.png', 30, 200, 4, 50, 150)
platform2= Player('platform.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)
speed_x = 3
speed_y = 3
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(blue)
        platform1.reset()
        platform2.reset()
    display.update()
    Clock.tick(FPS)
 
        
