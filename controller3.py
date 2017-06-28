import player
import enemyships
import shooting
import pygame
import time

pygame.init()
display_width = 480
display_height = 710

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
yellow = (255, 255, 0)
green = (0, 200, 0)
bright_red =(255,0,0)
bright_green = (0,200,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock() #tick
bg_size = width, height = 480, 710#height/width
screen = pygame.display.set_mode(bg_size)#calls screen
background = pygame.image.load("image/background.png")#gets image


def text_objects(text, font):
        #""Make text and font""
   textSurface = font.render(text, True, black)
   return textSurface, textSurface.get_rect()

def game_intro():#loop for the intro page- click events for starting the game
   #"""Make main menu"""
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
        button("QUIT", 150, 600, 100,50, bright_red, green,"quit")#for the second button

        pygame.display.update()

def button(msg,x,y,w,h,ic,ac,action=None):#need message, x, y cooridnates, width and height and inactivecolor and activecolor and act of clicking
    """"Make button for main menu"""
    mouse = pygame.mouse.get_pos()#using mouse position to make things happen
    click = pygame.mouse.get_pressed()#making something happen when it clicks


    if x +w > mouse[0]>x and y + h > mouse[1] > y: #top button-within boundaries ofthe box.greater than x coordinate
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))#wen mouse hovers over button
        if click[0] == 1 and action != None:
            if action == "play":
                controller.main_loop()
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
    # time.sleep(2)
    # game_loop = ()

#game_intro()
#pygame.quit()
#quit()

#===================================Controller Class=============================================

class controller:

    def __init__(self):
        self.hero = player.Player(480, 710)
        self.enemy = enemyships.Enemyships(480,710)
        #bullet = shooting.Shooting()
        pygame.init()

        bg_size = width, height = 480, 710  # backgroundsize
        screen = pygame.display.set_mode(bg_size)  # set screen
        pygame.display.set_caption("Space invaders")
        background = pygame.image.load("image/background.png")  # bg picture
        use_image = pygame.image.load("image/game_pause_pressed.png")  # pause button
        resume_image = pygame.image.load("image/game_resume_pressed.png") #play button
        gameover_image = pygame.image.load("image/game_over.png")  # game_over
        gameover_rect = gameover_image.get_rect()
        button_inst = pygame.image.load("image/instruction.png")#instruction button
        button_quit = pygame.image.load("image/quit.png")#quit button
        bg_inst = pygame.image.load("image/bg_inst.png")#bg for instructions


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
        #
        #gameover_image = pygame.image.load("image/game_over.png")
        #gameover_rect = gameover_image.get_rect()
        #button_inst = pygame.image.load("image/instruction.png")
        #button_quit = pygame.image.load("image/quit.png")
        #rsume_image = pygame.image.load("image/game_resume_pressed.png")
        #bg_inst = pygame.image.load("image/bg_inst.png")
        #score_image = pygame.image.load("image/score.png")
        #top_score_image = pygame.image.load("image/top_score.png")
        # ==========Main program start====================

    def main_loop(self):
        gameexit = False
        clock = pygame.time.Clock()
        while not gameexit:#while loop of game events - with a for loop for keys for player
            screen.blit(background, (0, 0))#image of background
            screen.blit(self.hero.image, self.hero.rect)#hero image
            screen.blit(self.enemy.image,self.enemy.rect)#enemy ship image
            pygame.display.flip()#update

            for event in pygame.event.get():#for loop for player
                if event.type == pygame.QUIT:#if event is quit
                    quit()

                elif event.type == pygame.KEYDOWN:#if up key is pressed the playermoves up
                    if event.key == pygame.K_UP:
                        self.hero.move_up()

                    elif event.key == pygame.K_DOWN:#if down key is pressed the player moves down
                        self.hero.move_down()

                    elif event.key == pygame.K_LEFT:#if left key is pressed the player moves left
                        self.hero.move_left()

                    elif event.key == pygame.K_RIGHT:#if right key is pressed player moves right
                        self.hero.move_right()
                        # elif event.key == pygame.K_SPACE:
                        #     bullet.move()

            self.enemy.move()#calling enemyships class
            self.enemy.move()
            self.enemy.move()
            if self.hero.rect.top < self.enemy.rect.bottom:#creating boundary for crash
               crash()#reads the message

                # if hero.rect.left > enemy.rect.right:
                #     gameexit = True
        if self.hero.rect.top > 740 or self.hero.rect.bottom < -740 or self.hero.rect.left < -480 or self.hero.rect.right > 480:  # boundaries to keep player within the screen- outside of while loop because we don't want to cycle through this we want it at all times
            gameexit = True
        pygame.display.update()



def message_display(text):
    """Create message for message display variable in crash"""
    sText = pygame.font.Font('freesansbold.ttf', 50)
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


#pygame.quit()
#quit()

if __name__ == '__main__':
    controller3 = controller()
    game_intro()