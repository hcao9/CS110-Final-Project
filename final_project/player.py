import pygame
import random

BG_WIDTH = 480 # bg size
BG_HEIGHT = 852

class Player(pygame.sprite.Sprite):
    """Make player move"""
    def __init__(self, BG_WIDTH,BG_HEIGHT):
        """Set up the image and other attributes"""
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
        """Makes player move up"""
        if self.rect.top > 0:
            self.rect.top -= self.speed

    def move_down(self):
        """Make player move down"""
        if self.rect.bottom < BG_HEIGHT - 60:
            self.rect.top += self.speed

    def move_left(self):
        """Make player move left"""
        if self.rect.left > 0:
            self.rect.left -= self.speed

    def move_right(self):
        """Make player move right"""
        if self.rect.right < BG_WIDTH:
            self.rect.right += self.speed

    def reset(self):
        "Make player reset itself"
        self.rect.left, self.rect.top = (BG_WIDTH - self.rect.width) // 2, (BG_HEIGHT - self.rect.height - 60)
        self.active = True