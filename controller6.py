import player
import score
import enemyships
import shooting
import pygame
import time



#define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 200, 0)



#initialize pygame and create window
pygame.init()
display_width = 480
display_height= 710
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()  # tick
bg_size = width, height = 480, 710  # height/width
screen = pygame.display.set_mode(bg_size)  # calls screen
background = pygame.image.load("image/background.png")  # gets image
all_sprites = pygame.sprite.Group()



def text_objects(text, font):
    # ""Make text and font""
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def game_intro():  # loop for the intro page- click events for starting the game
    # """Make main menu"""
    intro = True  # while we are here
    while intro:  # while loop for exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(background, (0, 0))  # blits background on main menu
        # gameDisplay.fill(white)#background of main menu

        sText = pygame.font.Font('freesansbold.ttf', 70)  # places the word Space- color,height, width, font, size
        TextSurf, TextRect = text_objects("Space", sText)  # font and text
        TextRect.center = ((display_width / 2), (display_height / 8))  # placement
        gameDisplay.blit(TextSurf, TextRect)  # blit it on surface

        iText = pygame.font.Font('freesansbold.ttf', 70)  # places the word Invaders- color,height, width, font, size
        TextSurf, TextRect = text_objects("Invaders", iText)  # font and text
        TextRect.center = ((display_width / 2), (display_height / 4))  # placement
        gameDisplay.blit(TextSurf, TextRect)  # blit on surface

        rText = pygame.font.Font('freesansbold.ttf', 30)  # places the word Space- color,height, width, font, size
        TextSurf, TextRect = text_objects("How to Play", rText)  # font and text
        TextRect.center = ((display_width / 2), (display_height / 2.5))  # placement
        gameDisplay.blit(TextSurf, TextRect)  # blit it on surface

        yText = pygame.font.Font('freesansbold.ttf', 15)  # places the word Invaders- color,height, width, font, size
        TextSurf, TextRect = text_objects("Move the ship using your arrow keys", yText)  # font and text
        TextRect.center = ((display_width / 2), (display_height / 2.1))  # placement
        gameDisplay.blit(TextSurf, TextRect)  # blit on surface

        dText = pygame.font.Font('freesansbold.ttf', 15)  # places the word Invaders- color,height, width, font, size
        TextSurf, TextRect = text_objects("Shoot the enemy ships using the space bar", dText)  # font and text
        TextRect.center = ((display_width / 2), (display_height / 1.9))  # placement
        gameDisplay.blit(TextSurf, TextRect)  # blit on surface

        pText = pygame.font.Font('freesansbold.ttf', 15)  # places the word Invaders- color,height, width, font, size
        TextSurf, TextRect = text_objects("Get as high a score as possible", pText)  # font and text
        TextRect.center = ((display_width / 2), (display_height / 1.7))  # placement
        gameDisplay.blit(TextSurf, TextRect)  # blit on surface


        button("START", 195, 520, 100, 50, white, black, "play")  # for the first button
        button("QUIT", 195, 620, 100, 50, white, black, "quit")  # for the second button

        pygame.display.update()

# def instructions(): #instructions page
#     intro = True  # while we are here
#     while intro:  # while loop for exit
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#         screen.blit(background, (0, 0))  # blits background on main menu
#         # gameDisplay.fill(white)#background of main menu
#
#
#
#         button("Pause", 200, 620, 100, 50, white, black, "pause")
# pygame.display.update()



def button(msg, x, y, w, h, ic, ac,action=None):  # need message, x, y cooridnates, width and height and inactivecolor and activecolor and act of clicking
    """"Make button for main menu"""
    mouse = pygame.mouse.get_pos()  # using mouse position to make things happen
    click = pygame.mouse.get_pressed()  # making something happen when it clicks
    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # top button-within boundaries ofthe box.greater than x coordinate
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))  # when mouse hovers over button
        if click[0] == 1 and action != None:
            if action == "play":
                controller()

            if action == "back":
                game_intro()
            if action == "pause":
                pause()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))  # when mouse not there it is white
    smallText = pygame.font.Font("freesansbold.ttf", 20)  # text for the button- font and size
    textSurf, textRect = text_objects(msg, smallText)  # text
    textRect.center = ((x + (w / 2), (y + (h / 2))))  # placement based on where box is
    gameDisplay.blit(textSurf, textRect)  # blit the word on the screen
clock.tick(100)
pygame.display.update()



def sc(score):
    smallfont = pygame.font.SysFont("comicsansms", 25)
    text = smallfont.render("Score: "+str(score),True, black)
    gameDisplay.blit(text,[400,0])
    score()

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    game_intro()
        gameDisplay.fill(white)
        message_display("C = continue or Q = Quit")
        pygame.display.update()

# ===================================Controller Class=============================================

class controller:
    def __init__(self):
        hero = player.Player(480, 710)#calling Player class
        enemy = enemyships.Enemyships(480, 710)#calling enemyships class
        #bullet = shooting.Shooting(hero.rect.left,hero.rect.top)#calling shooting class

        pygame.init()

        bg_size = width, height = 480, 710  # backgroundsize
        screen = pygame.display.set_mode(bg_size)  # set screen
        pygame.display.set_caption("Space invaders")
        background = pygame.image.load("image/background.png")  # bg picture
        use_image = pygame.image.load("image/game_pause_pressed.png")  # pause button
        resume_image = pygame.image.load("image/game_resume_pressed.png")  # play button
        gameover_image = pygame.image.load("image/game_over.png")  # game_over
        gameover_rect = gameover_image.get_rect()
        button_inst = pygame.image.load("image/instruction.png")  # instruction button
        button_quit = pygame.image.load("image/quit.png")  # quit button
        bg_inst = pygame.image.load("image/bg_inst.png")  # bg for instructions
        enemy_explosion_images = []
        hero_explosion_images = []
        enemy_explosion_list = [pygame.image.load("image/enemy1_down1.png"),
                                pygame.image.load("image/enemy1_down2.png"),
                                pygame.image.load("image/enemy1_down3.png"),
                                pygame.image.load("image/enemy1_down4.png")]
        hero.explosion_list = [pygame.image.load("image/hero_blowup_n1.png"),
                                pygame.image.load("image/hero_blowup_n2.png"),
                                pygame.image.load("image/hero_blowup_n3.png"),
                                pygame.image.load("image/hero_blowup_n4.png")]



        # ==================Initialize==================
        pygame.mixer.init()
        background = pygame.image.load("image/background.png")  # Load background image


        # ==========Load music and sound====================
        # pygame.mixer.music.load("sound/background.wav")
        # pygame.mixer.music.set_volume(0.3)
        # bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
        # pygame.mixer.Sound.set_volume(bullet_sound, 0.3)
        # enemy_down_sound = pygame.mixer.Sound("sound/enemy_down.wav")
        # pygame.mixer.Sound.set_volume(enemy_down_sound, 0.3)
        # hero_down_sound = pygame.mixer.Sound("sound/hero_down.wav")
        # pygame.mixer.Sound.set_volume(hero_down_sound, 0.3)
        # button_sound = pygame.mixer.Sound("sound/button.wav")
        # pygame.mixer.Sound.set_volume(button_sound, 0.3)


        # ==========Load image and button====================
        # pause_image = pygame.image.load("image/pause.png")
        #
        # gameover_image = pygame.image.load("image/game_over.png")
        # gameover_rect = gameover_image.get_rect()
        # button_inst = pygame.image.load("image/instruction.png")
        # button_quit = pygame.image.load("image/quit.png")
        # rsume_image = pygame.image.load("image/game_resume_pressed.png")
        # bg_inst = pygame.image.load("image/bg_inst.png")
        # score_image = pygame.image.load("image/score.png")
        # top_score_image = pygame.image.load("image/top_score.png")


        # ==========Main Loop start====================
        gameexit = False
        clock = pygame.time.Clock()
        while not gameexit:  # while loop of game events - with a for loop for keys for player

            while gameexit == True:#game over page
                gameDisplay.fill(white)
                message_display("Game Over")
                pygame.display.update()

            screen.blit(background, (0, 0))  # image of background
            screen.blit(hero.image, hero.rect)  # hero image
            screen.blit(enemy.image, enemy.rect)  # enemy ship image

            # if button("B", 20, 20, 30, 30, white, black, "back"): #on playing screen B is for going back to the menu
            #     game_intro()
            # if button("P", 20, 55, 30, 30, white, black, "pause"):#makes the P a puase button on playing screen
            #     pause()
           # if button("P", 20, 55, 30, 30, white, black, "pause"):
            pygame.display.update()  # update


            for event in pygame.event.get():  # for loop for player
                if event.type == pygame.QUIT:  # if event is quit
                    quit()
                elif event.type == pygame.KEYDOWN:  # if up key is pressed the playermoves up
                    if event.key == pygame.K_UP:
                        hero.move_up()
                    elif event.key == pygame.K_DOWN:  # if down key is pressed the player moves down
                        hero.move_down()
                    elif event.key == pygame.K_LEFT:  # if left key is pressed the player moves left
                        hero.move_left()
                    elif event.key == pygame.K_RIGHT:  # if right key is pressed player moves right
                        hero.move_right()
                    # elif event.key == pygame.K_p:
                    #     pause()
                    elif event.key == pygame.K_SPACE:#press space bar fires
                         hero.shoot()

            if hero.rect.top == enemy.rect.bottom:  # collision of hero and enemy ships
                gameexit = True
                crash() #message display of losing
                  # calling enemy ships class
            enemy.move()

          #  hits = pygame.sprite.spritecollideany(player,enemyships,False)#colliding
         #   if hits:
        #        gameexit = True


        if hero.rect.top > 740 or hero.rect.bottom < -740 or hero.rect.left < -480 or hero.rect.right > 480:  # boundaries to keep player within the screen- outside of while loop because we don't want to cycle through this we want it at all times
            gameexit = True
        score(bullet - 1) #calling score funtion above
       # all_sprites.draw(screen)
        pygame.display.update()


def message_display(text):
    """Create message for message display variable in crash"""
    sText = pygame.font.Font('freesansbold.ttf', 50)#font and size
    TextSurf, TextRect = text_objects(text, sText)
    TextRect.center = ((display_width / 2), (display_height / 3))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_intro()


def crash():
    """Display message for when hero crashes into enemy"""
    message_display('You Died Sucka')
pygame.display.update()

# pygame.quit()
# quit()


if __name__ == '__main__':
    game_intro()

    controller3 = controller()
