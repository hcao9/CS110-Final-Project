import pygame
import sys
import traceback
import player
import enemy
import bullet
BG_WIDTH = 480 # set screen size
BG_HEIGHT = 852


def enemy_add(group,num):
    """initiating the enemy"""
    for i in range(num):
        e = enemy.Enemy(BG_WIDTH,BG_HEIGHT)
        group.add(e)


class controller():
    """Run main loop for game"""
    def __init__(self):
        """Attributes for game"""
        # ==================Initialize==================
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode([BG_WIDTH, BG_HEIGHT])  # Set viewer screen
        pygame.display.set_caption("Space Invaders")
        background = pygame.image.load("image/background.png")  # Load background image
        # ==========Load music and sound====================
        pygame.mixer.music.load("sound/background.wav")
        pygame.mixer.music.set_volume(0.3)
        bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
        pygame.mixer.Sound.set_volume(bullet_sound, 0.3)
        enemy_down_sound = pygame.mixer.Sound("sound/enemy_down.wav")
        pygame.mixer.Sound.set_volume(enemy_down_sound, 0.3)
        hero_down_sound = pygame.mixer.Sound("sound/hero_down.wav")
        pygame.mixer.Sound.set_volume(hero_down_sound, 0.3)
        button_sound = pygame.mixer.Sound("sound/button.wav")
        pygame.mixer.Sound.set_volume(button_sound, 0.3)
        # ==========Load image and button====================
        pause_image = pygame.image.load("image/pause.png")
        resume_image = pygame.image.load("image/resume.png")
        gameover_image = pygame.image.load("image/game_over.png")
        gameover_rect = gameover_image.get_rect()
        button_inst = pygame.image.load("image/instruction.png")
        button_quit = pygame.image.load("image/quit.png")
        button_start = pygame.image.load("image/resume.png")
        button_back = pygame.image.load("image/back.png")
        bg_inst = pygame.image.load("image/bg_inst.png")
        score_image = pygame.image.load("image/score.png")
        top_score_image = pygame.image.load("image/top_score.png")
        # ==========Main program start====================
        running = True  # set main loop start point
        ticks = 60  # time-delay counts
        score = 0  # score initial setting
        score_font = pygame.font.SysFont("arial", 48)
        start_font = pygame.font.SysFont("arial", 60, True)
        start_text = start_font.render("Space Invaders", True, (54, 62, 63))
        state = 'beginner'  # set state of level
        life_image = pygame.image.load("image/life.png")  # life initial setting
        life_rect = life_image.get_rect()
        start = False  # set game-start initial status
        instruction = False
        paused = False  # set pause initial status
        paused_image = pause_image # set pause button initial image
        # =============Button position setting=========================
        start_rect = button_start.get_rect()
        start_rect.left, start_rect.top = 120, 700  # start button position
        start_inst_rect = button_inst.get_rect()
        start_inst_rect.left, start_inst_rect.top = 300, 700  # instruction button position
        paused_rect = paused_image.get_rect()
        paused_rect.left, paused_rect.top = BG_WIDTH - paused_rect.width - 10, 10  # pause button position
        inst_rect = button_inst.get_rect()
        inst_rect.left, inst_rect.top = BG_WIDTH - inst_rect.width - 8, 70  # instruction button position
        quit_rect = button_quit.get_rect()
        quit_rect.left, quit_rect.top = BG_WIDTH - inst_rect.width - 3, 130  # quit button position
        back_rect = button_back.get_rect()
        back_rect.left, back_rect.top = (BG_WIDTH - back_rect.width) / 2, 650  # back-to-start button position
        score_image_rect = score_image.get_rect()
        score_image_rect.left, score_image_rect.top = 5, 5  # score text position
        top_score_image_rect = top_score_image.get_rect()
        top_score_image_rect.left, top_score_image_rect.top = 5 , 5  # top score position
        # ===============Object initialize=====================
        hero = player.Player(BG_WIDTH, BG_HEIGHT)  # build player plane
        enemies = pygame.sprite.Group()  # build enemy group
        bullets = pygame.sprite.Group()
        pygame.mixer.music.load("sound/background.wav")
        pygame.mixer.music.play(-1)
        while running:
            clock = pygame.time.Clock()  # set frame rate
            clock.tick(60)
            # ====================Level setting====================
            if score > 8000 and state == 'beginner':  # when level reach 'easy',add 3 enemies and speed up
                enemy_add(enemies, 3)
                for each in enemies:
                    each.speed += 1
                state = 'easy'
            elif score > 20000 and state == 'easy':  # when level reach 'normal',add 3 enemies and speed up
                enemy_add(enemies, 3)
                for each in enemies:
                    each.speed += 1
                state = 'normal'
            elif score > 40000 and state == 'normal':  # when level reach 'hard',add 3 enemies and speed up
                enemy_add(enemies, 3)
                for each in enemies:
                    each.speed += 1
                state = 'hard'
            elif score > 80000 and state == 'hard':  # when level reaches 'super hard',add 3 enemies and speed up
                enemy_add(enemies, 3)
                for each in enemies:
                    each.speed += 1
                state = 'super hard'
            if not start:  # if not start,show game-start screen
                life_num = 3  # set initial life counts
                score = 0  # set initial score
                enemies.empty()  # reset enemy and player state
                hero.reset()
                enemy_add(enemies, 1)
                state = 'beginner'  # reset level state
                if instruction:#instruction page
                    screen.blit(bg_inst, (0, 0))
                    screen.blit(button_back, back_rect)
                    pygame.display.update()
                else:
                    screen.blit(background, (0, 0))
                    screen.blit(start_text, (60, 300))
                    screen.blit(button_start, start_rect)
                    screen.blit(button_inst, start_inst_rect)
                    pygame.display.update()
            else:
                pygame.mixer.music.play(-1)#music for when you die
                screen.blit(background, (0, 0))
                # ====================Lives====================
                if life_num != 0:
                    screen.blit(paused_image, paused_rect)
                    screen.blit(button_inst, inst_rect)
                    screen.blit(button_quit, quit_rect)
                    pygame.display.update(paused_rect)
                # ====================Keeps running====================
                    if not paused:  # if not paused,game continues to running
                        screen.blit(score_image, score_image_rect)
                        score_text = score_font.render("%s" % str(score), True, (54, 62, 63))
                        screen.blit(score_text, (score_image_rect.width + 15, 15))
                        if hero.active:  # if player is alive,draw player ship
                            screen.blit(hero.image, hero.rect)
                        else:
                            for i in range(0, 3):  # show explosion image sequence
                                screen.blit(hero.explosion_image[i], hero.rect)
                            hero_down_sound.play()
                            life_num -= 1  # life counts -1,player reset
                            hero.reset()
                # ====================Keys for moving player====================
                        key_pressed = pygame.key.get_pressed()  # get all user stay-pressed keyboard message
                        if key_pressed[pygame.K_UP]:  # if keyboard stay-pressed UP,player move up
                            hero.move_up()
                        if key_pressed[pygame.K_DOWN]:
                            hero.move_down()
                        if key_pressed[pygame.K_LEFT]:
                            hero.move_left()
                        if key_pressed[pygame.K_RIGHT]:
                            hero.move_right()
                        for i in range(life_num):  # draw life counts image
                            screen.blit(life_image, (BG_WIDTH - 10 - (i + 1) * life_rect.width, BG_HEIGHT - 10 - life_rect.height))
                        if ticks % 10 == 0:  # create a bullet every 10 frames
                            bullet_sound.play()#bullet sound
                            b = bullet.Bullet(hero.rect.midtop)
                            bullets.add(b)
                        # ====================Bullets====================
                        for each in bullets:
                            if each.active is True:  # only alive bullet can hit enemy
                                each.move()
                                screen.blit(each.image, each.rect)
                                enemy_hit = pygame.sprite.spritecollide(each, enemies, False)  # bullet-enemy hit test
                                if enemy_hit:  # if bullet hit any enemy
                                    each.active = False  # bullet died
                                    for e in enemy_hit:
                                        e.active = False  # enemy died
                        for each in enemies:
                            if each.active: # draw and move alive enemies
                                each.move()
                                screen.blit(each.image, each.rect)
                            else:
                                for i in range(0, 3):  # show explosion image sequence
                                    screen.blit(each.explosion_image[i], each.rect)
                                enemy_down_sound.play()
                                score += 500  # add score when enemy down
                                each.reset()
                        enemies_crash = pygame.sprite.spritecollide(hero, enemies, False)
                        if enemies_crash:  # check collision between player and enemy
                            hero.active = False  # player died
                            for e in enemies_crash:
                                e.active = False  # enemy died
                        pygame.display.flip()
                else:  # draw game-over screen when life counts equals 0
                    clock = pygame.time.Clock()  # frame setting
                    clock.tick(60)
                    # ================Draw game-over screen and buttons==============
                    screen.blit(gameover_image, gameover_rect)
                    screen.blit(button_back, back_rect)
                    screen.blit(top_score_image, top_score_image_rect)
                    screen.blit(score_image, (5, top_score_image_rect.height + 10))
                    pygame.mixer.music.stop()  # stop background music
                    pygame.mixer.stop()  # stop all sound effect
                    with open("score_record.txt", "r") as f:  # load top score from file
                        top_score = int(f.read())
                    if score > top_score:  # save as top score if player score is larger than file
                        with open("score_record.txt", "w") as f:
                            f.write(str(score))
                    # =====================Draw score text========================
                    top_score_text = score_font.render("%d" % top_score, True, (54, 62, 63))
                    screen.blit(top_score_text, (top_score_image_rect.width + 15 , 15))
                    game_over_score_text = score_font.render("%d" % score, True, (54, 62, 63))
                    screen.blit(game_over_score_text, (score_image_rect.width + 15, top_score_image_rect.height + 15))
                    pygame.display.flip()
            for event in pygame.event.get():  # get all user events
                if event.type == pygame.QUIT:  # if user click quit of the viewer window
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:  # for any mouse click
                    button_sound.play()
                    if not start:
                        if event.button == 1 and start_rect.collidepoint(event.pos):  # start-screen check
                            start = True
                        elif event.button == 1 and start_inst_rect.collidepoint(event.pos):
                            instruction = True
                    if (event.button == 1 and paused_rect.collidepoint(event.pos)) or (event.button == 1 and inst_rect.collidepoint(event.pos)):
                        # pause status check
                        if event.button == 1 and inst_rect.collidepoint(event.pos):
                            # instruction status re-check
                            screen.blit(bg_inst,(0,0))
                            pygame.display.flip()
                            paused = True
                        if event.button == 1 and paused_rect.collidepoint(event.pos):
                            # switch pause status
                            paused = not paused
                        if paused:
                            paused_image = resume_image  # switch pause button image
                            pygame.mixer.music.pause()
                            pygame.mixer.pause()
                        else:
                            paused_image = pause_image  # switch pause button image
                            pygame.mixer.music.unpause()
                            pygame.mixer.unpause()
                            screen.blit(background, (0, 0))
                            pygame.display.update()
                    if event.button == 1 and quit_rect.collidepoint(event.pos):  # quit button check
                        pygame.quit()
                        sys.exit()
                    if event.button == 1 and back_rect.collidepoint(event.pos) :
                        if life_num == 0:  # back button check
                            start = False
                        elif instruction:
                            instruction = False
            if ticks == 0:
                ticks = 60
            ticks -= 1

if __name__ == '__main__':
    controller()
