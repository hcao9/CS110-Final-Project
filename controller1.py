import model
import pygame




class Stuff:

    def __init__(self):
        hero = model.Player(400, 710)
        pygame.init()

        bg_size = width, height = 400, 710  # backgroundsize
        screen = pygame.display.set_mode(bg_size)  # set bg  # set bg
        pygame.display.set_caption("Space invaders")
        background = pygame.image.load("image/background.png")  # bg picture
        # """image"""
        use_image = pygame.image.load("image/pause.png")  # pause_button_image
        resume_image = pygame.image.load("image/resume.png")
        gameover_image = pygame.image.load("image/game_over.png")  # bg_game_over
        gameover_rect = gameover_image.get_rect()
        button_inst = pygame.image.load("image/instruction.png")
        button_quit = pygame.image.load("image/quit.png")

        bg_inst = pygame.image.load("image/bg_inst.png")

        pygame.display.set_caption('SPACE INVADERS')

        clock = pygame.time.Clock()



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
        gameexit = False
        while not gameexit:
            screen.blit(background, (0, 0))
            screen.blit(hero.image, hero.rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameexit = True

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        hero.move_up()

                    if event.key == pygame.K_DOWN:
                        hero.move_down()

                    if event.key == pygame.K_LEFT:
                        hero.move_left()

                    if event.key == pygame.K_RIGHT:
                        hero.move_right()


#pygame.quit()
#quit()

if __name__ == '__main__':
    Stuff()




