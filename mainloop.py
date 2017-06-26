
import player
import pygame

pygame.init()
display_width = 800
display_height = 600
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('SPACE INVADERS')
clock = pygame.time.Clock()


class Controller:
    def __init__(self):
        self.hero = player.Player()
        self.bg_height = bg_height
        self.bg_width = bg_width
        self.getEvents = getEvents
        self.x = x
        self.y = y
    def mainloop(self):


        x = (display_width * 0.45)
        y = (display_height * 0.8)
        x_change = 0
        y_change = 0

        gameExit = False
        while not gameExit:
            for event in pygame.getEvents():

                if event.key == pygame.K_UP:
                    if self.hero.move_up():
                        y_change = 5

                if event.key == pygame.K_DOWN:
                    if self.hero.move_down():
                        y_change = -5

                if event.key == pygame.K_LEFT:
                    if self.hero.move_left():
                        x_change = -5

                if event.key == pygame.K_RIGHT:
                    if self.hero.move_right():
                        x_change = 5
                if event.type == pygame.QUIT:
                    gameExit = True

                if event.key ==



gameDisplay.fill(white)
pygame.display.update()
clock.tick(30)

pygame.quit()
quit()
