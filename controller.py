
import player
import pygame



display_width = 800
display_height = 600
white = (255,255,255)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('SPACE INVADERS')
pygame.init()

clock = pygame.time.Clock()
ship = pygame.image.load('image/hero.png')

class stuff:

    def __init__(self):
        x = (display_width * 0.45)
        y = (display_height * 0.8)
        self.x = x
        self.y = y

        self.hero = player.Player(400, 710)



        # ==================Initialize==================
        pygame.mixer.init()
        background = pygame.image.load("image/background.png")  # Load background image
        # ==========Load music and sound====================
        #pygame.mixer.music.load("sound/background.wav")
        #pygame.mixer.music.set_volume(0.3)
        #bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
        #pygame.mixer.Sound.set_volume(bullet_sound, 0.3)
        #enemy_down_sound = pygame.mixer.Sound("sound/enemy_down.wav")
        #pygame.mixer.Sound.set_volume(enemy_down_sound, 0.3)
        #hero_down_sound = pygame.mixer.Sound("sound/hero_down.wav")
        #pygame.mixer.Sound.set_volume(hero_down_sound, 0.3)
        #button_sound = pygame.mixer.Sound("sound/button.wav")
        #pygame.mixer.Sound.set_volume(button_sound, 0.3)
        # ==========Load image and button====================
        #pause_image = pygame.image.load("image/pause.png")
        #resume_image = pygame.image.load("image/resume.png")
        #gameover_image = pygame.image.load("image/game_over.png")
        #gameover_rect = gameover_image.get_rect()
        #button_inst = pygame.image.load("image/instruction.png")
        #button_quit = pygame.image.load("image/quit.png")
        #button_restart = pygame.image.load("image/resume.png")
        #bg_inst = pygame.image.load("image/bg_inst.png")
        #score_image = pygame.image.load("image/score.png")
        #top_score_image = pygame.image.load("image/top_score.png")
        # ==========Main program start====================

    def loop(self):

        gameDisplay.blit(ship,(x,y))


        y_up = 0
        y_down = 0
        x_left = 0
        x_right = 0
        x_change_right = 0
        x_change_left = 0
        y_change_up = 0
        y_change_down = 0

        y_up += y_change_up
        y_down += y_change_down
        x_left += x_change_left
        x_right += x_change_right

        gameexit = False

        while not gameexit:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        if self.hero.move_up():
                            y_change_up += 5

                    if event.key == pygame.K_DOWN:
                        if self.hero.move_down():
                            y_change_down += -5

                    if event.key == pygame.K_LEFT:
                        if self.hero.move_left():
                            x_change_left += -5

                    if event.key == pygame.K_RIGHT:
                        if self.hero.move_right():
                            x_change_right += 5
                if event.type == pygame.KEYUP: #this is so that when you hold down the key that the object still moves and you don't have to contatnly press the key to get it to move
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change_right == 0
                        x_change_left == 0
                        y_change_up == 0
                        y_change_down == 0

                if event.type == pygame.QUIT:
                    gameexit = True


        gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(30)

#pygame.quit()
#quit()


def main():
    stuff()


main()


