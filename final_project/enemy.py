import pygame
import random

BG_WIDTH = 480 # bg size
BG_HEIGHT = 852

class Enemy(pygame.sprite.Sprite):
    """Make enemy ships"""
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
        """Enemy ships moving down"""
        if self.rect.top < BG_HEIGHT:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        "reset enemy"
        self.rect.left, self.rect.top = (
            random.randint(0, BG_WIDTH - self.rect.width),random.randint(-5 * self.rect.height, 0))
        self.active = True