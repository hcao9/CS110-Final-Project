import pygame


pygame.init()
bg_size = width, height = 400, 710  # backgroundsize
bg_width = 400
bg_height = 710
screen = pygame.display.set_mode(bg_size)  # set bg
pygame.display.set_caption("Space invaders")
background = pygame.image.load("image/background.png")  # bg picture
# """image"""
use_image = pygame.image.load("image/game_pause_pressed.png") # pause_button_image
resume_image = pygame.image.load("image/game_resume_pressed.png")
gameover_image = pygame.image.load("image/game_over.png")  # bg_game_over
gameover_rect = gameover_image.get_rect()
button_inst = pygame.image.load("image/instruction.png")
button_quit = pygame.image.load("image/quit.png")

bg_inst = pygame.image.load("image/bg_inst.png")


class Player(pygame.sprite.Sprite):

    def __init__(self, bg_width,bg_height):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/hero.png")  
        self.rect = self.image.get_rect()  
        self.rect.left, self.rect.top = (bg_width - self.rect.width) // 2, (bg_height - self.rect.height - 60)
        self.speed = 10
        self.active = True  # active is True, destroyed is False
        self.destroyed_image = [pygame.image.load("image/hero_blowup_n1.png"),
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
