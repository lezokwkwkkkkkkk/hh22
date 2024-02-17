import pygame
from pygame import *
pygame.init()
window = pygame.display.set_mode((600,400))
pygame.display.set_caption("Ping Pong")

bg = pygame.image.load("PINGPING.jpg")

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,width,height):
        super().__init__()
        self.image = pygame.transform.scale(image.load(player_image), (width,height)) #разом 55,55 - параметри
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def show(self):
     window.blit(self.image,(self.rect.x,self.rect.y))
    
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 300:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 385:
            self.rect.y += self.speed

player_1 = Player('players.png',50,200,1,20,100)
player_2 = Player('players.png',525,200,1,20,100)

exit = False

while not exit:
    for events in pygame.event.get():
        if events.type == QUIT:
            exit = True
               
    window.blit(bg, (0, 0))
    player_1.update_l()
    player_2.update_r()
    player_1.reset()
    player_2.reset()
    pygame.display.update()

    