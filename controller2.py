import player
import pygame

pygame.init()
display_width = 410
display_height = 800

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
yellow = (255, 255, 0)
green = (0, 200, 0)
bright_red =(255,0,0)
bright_green = (0,200,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
bg_size = width, height = 400, 710#height/width
screen = pygame.display.set_mode(bg_size)#calls scren
background = pygame.image.load("image/background.png")#gets image


def text_objects(text, font):
   textSurface = font.render(text, True, black)
   return textSurface, textSurface.get_rect()

def game_intro():#loop for the intro page- click events for starting the game
    intro = True#while we are here
    while intro:#while loop for exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(background, (0, 0))#blits background on main menu

        #gameDisplay.fill(white)#background of main menu

        sText = pygame.font.Font('freesansbold.ttf', 90)#places the word Space- color,height, width, font, size
        TextSurf, TextRect = text_objects("Space", sText)#font and text
        TextRect.center = ((display_width / 2), (display_height / 3))#placement
        gameDisplay.blit(TextSurf, TextRect)#blit it on surface

        iText = pygame.font.Font('freesansbold.ttf', 90)#places the word Invaders- color,height, width, font, size
        TextSurf, TextRect = text_objects("Invaders", iText)#font and text
        TextRect.center = ((display_width/2), (display_height /2))#placement
        gameDisplay.blit(TextSurf, TextRect)#blit on surface

        button("START", 150, 500,100,50, bright_red, green,"play")#for the first button
        button("QUIT", 150, 600, 100, 50, bright_red, green,"quit")#for the second button

        pygame.display.update()

def button(msg,x,y,w,h,ic,ac,action=None):#need message, x, y cooridnates, width and height and inactivecolor and activecolor and act of clicking

    mouse = pygame.mouse.get_pos()#using mouse position to make things happen
    click = pygame.mouse.get_pressed()#making something happen when it clicks


    if x +w > mouse[0]>x and y + h > mouse[1] > y: #top button-within boundaries ofthe box.greater than x coordinate
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))#wen mouse hovers over button
        if click[0] == 1 and action != None:
            if action == "play":
                controller()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))#when mouse not there it is green

    smallText = pygame.font.Font("freesansbold.ttf", 20)#text for the button- font and size
    textSurf, textRect = text_objects(msg, smallText)#text
    textRect.center = ((x+(w/2), (y+(h/2))))#placement based on where box is
    gameDisplay.blit(textSurf, textRect)#blit the word on the screen



clock.tick(100)



pygame.display.update()
    #time.sleep(2)
    #game_loop = ()

#game_intro()
#pygame.quit()
#quit()

#===================================Controller Class=============================================

class controller:

    def __init__(self):
        hero = player.Player(400, 710)
        pygame.init()

        bg_size = width, height = 400, 710  # backgroundsize
        screen = pygame.display.set_mode(bg_size)  # set bg  # set bg
        pygame.display.set_caption("Space invaders")
        background = pygame.image.load("image/background.png")  # bg picture
        # """image"""
        use_image = pygame.image.load("image/game_pause_pressed.png")  # pause_button_image
        resume_image = pygame.image.load("image/game_resume_pressed.png")
        gameover_image = pygame.image.load("image/game_over.png")  # bg_game_over
        gameover_rect = gameover_image.get_rect()
        button_inst = pygame.image.load("image/instruction.png")
        button_quit = pygame.image.load("image/quit.png")

        bg_inst = pygame.image.load("image/bg_inst.png")

        pygame.display.set_caption('SPACE INVADERS')


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
        clock = pygame.time.Clock()
        while not gameexit:
    #Movement of Player
            screen.blit(background, (0, 0))
            screen.blit(hero.image, hero.rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameexit = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        hero.move_up()

                    elif event.key == pygame.K_DOWN:
                        hero.move_down()

                    elif event.key == pygame.K_LEFT:
                        hero.move_left()

                    elif event.key == pygame.K_RIGHT:
                        hero.move_right()

                # elif event.type == pygame.KEYUP:
                #     if event.key == pygame.K_UP
                #     if event.key == pygame.K_DOWN
                #     if event.key == pygame.K_RIGHT
                #     if event.key == pygame.K_LEFT



# creating the enemy


        
#shooting the bullet



            pygame.display.update()
            clock.tick(30)



#pygame.quit()
#quit()

if __name__ == '__main__':
    game_intro()
    controller()