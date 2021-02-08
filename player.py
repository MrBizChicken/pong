import pygame, random
from constants import *
import player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 10
        self.y = 0
        self.width = 30
        self.height = 200
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)





    def update(self):
        self.key_input()



    def key_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:

            if self.rect.y > 0:
                self.rect.y += -self.speed

        if keys[pygame.K_DOWN]:
            if self.rect.bottom < GAME_HEIGHT:
                self.rect.y += self.speed

    def  get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
