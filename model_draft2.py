import pygame
import random

bg_width = 480 # bg size
bg_height = 852

class Player(pygame.sprite.Sprite):
    def __init__(self, bg_width,bg_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/hero.png")  
        self.rect = self.image.get_rect()  
        self.rect.left, self.rect.top = (
            bg_width - self.rect.width) // 2, (bg_height - self.rect.height - 60)
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
        if self.rect.bottom < bg_height - 60:
            self.rect.top += self.speed

    def move_left(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed

    def move_right(self):
        if self.rect.right < bg_width:
            self.rect.right += self.speed

    def reset(self):
        self.rect.left, self.rect.top = (bg_width - self.rect.width) // 2, (bg_height - self.rect.height - 60)
        self.active = True


class SmallPlane(pygame.sprite.Sprite):
    def __init__(self, bg_width,bg_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy1.png")  
        self.rect = self.image.get_rect()  
        self.speed = 2  
        self.rect.left, self.rect.top = (
            random.randint(0, bg_width - self.rect.width), random.randint(-5 * self.rect.height, -5))
        self.active = True  # active is true, destroyed is flase
        self.explosion_image = [pygame.image.load("image/enemy1_down1.png"),
                                pygame.image.load("image/enemy1_down2.png"),
                                pygame.image.load("image/enemy1_down3.png"),
                                pygame.image.load("image/enemy1_down4.png")]

    def move(self):  
        if self.rect.top < bg_height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = (
            random.randint(0, bg_width - self.rect.width),random.randint(-5 * self.rect.height, 0))
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
