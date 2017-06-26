import pygame
import random

BG_WIDTH = 480 # bg size
BG_HEIGHT = 852

class Player(pygame.sprite.Sprite):
    def __init__(self, BG_WIDTH,BG_HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/hero.png")  
        self.rect = self.image.get_rect()  
        self.rect.left, self.rect.top = (
            BG_WIDTH - self.rect.width) // 2, (BG_HEIGHT - self.rect.height - 60)
        self.speed = 10
        self.active = True  # active is ture, destroyed is flase
        self.explosion_image = [pygame.image.load("image/hero_blowup_n1.png"),
                                pygame.image.load("image/hero_blowup_n2.png"),
                                pygame.image.load("image/hero_blowup_n3.png"),
                                pygame.image.load("image/hero_blowup_n4.png")]

    def move_up(self):  
        if self.rect.top > 0: 
            self.rect.top -= self.speed

    def move_down(self):
        if self.rect.bottom < BG_HEIGHT - 60:
            self.rect.top += self.speed

    def move_left(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed

    def move_right(self):
        if self.rect.right < BG_WIDTH:
            self.rect.right += self.speed

    def reset(self):
        self.rect.left, self.rect.top = (BG_WIDTH - self.rect.width) // 2, (BG_HEIGHT - self.rect.height - 60)
        self.active = True


class SmallPlane(pygame.sprite.Sprite):
    def __init__(self, BG_WIDTH,BG_HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy1.png")  
        self.rect = self.image.get_rect()  
        self.speed = 2  
        self.rect.left, self.rect.top = (
            random.randint(0, BG_WIDTH - self.rect.width), random.randint(-5 * self.rect.height, -5))
        self.active = True  # active is true, destroyed is flase
        self.explosion_image = [pygame.image.load("image/enemy1_down1.png"),
                                pygame.image.load("image/enemy1_down2.png"),
                                pygame.image.load("image/enemy1_down3.png"),
                                pygame.image.load("image/enemy1_down4.png")]

    def move(self):  
        if self.rect.top < BG_HEIGHT:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = (
            random.randint(0, BG_WIDTH - self.rect.width),random.randint(-5 * self.rect.height, 0))
        self.active = True


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 12
        self.active = True

    def move(self):
        if self.rect.top < 0:
            self.active = False
        else:
            self.rect.top -= self.speed

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
