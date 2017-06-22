class enemyShips(pygame.sprite.Sprite):
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
