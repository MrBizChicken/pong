import pygame
from constants import *
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x =  50
        self.y = 100
        self.width = 40
        self.height = 40
        self.speed = 10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.horz_speed = 3
        self.vert_speed = 3




    def update(self,player):
        self.move()
        self.collide(player)






    def move(self):
        self.rect = self.rect.move(self.horz_speed, -self.vert_speed)
        if self.rect.right >= GAME_WIDTH:
             self.horz_speed = -self.horz_speed
             self.vert_speed + self.vert_speed


        if self.rect.left < 0:
            self.horz_speed = -self.horz_speed
            self.vert_speed = -self.vert_speed



        if self.rect.bottom >= GAME_HEIGHT:
            self.horz_speed + self.horz_speed
            self.vert_speed = -self.vert_speed
        if self.rect.top <= 0:
            self.horz_speed + self.horz_speed
            self.vert_speed = -self.vert_speed



    def collide(self, player):
        if rect.right >= player.Player.rect:
            self.horz_speed = -self.horz_speed
