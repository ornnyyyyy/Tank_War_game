import sys
import pygame
import scene
import bullet
import food
import tanks
import home
import time
from pygame.locals import *


# Start interface display
def show_start_interface(screen, width, height):
    bgs = pygame.image.load('./images/others/bg_brick.png')
    tfont = pygame.font.Font('./font/NP Happy new year_i.ttf', width//7)
    cfont = pygame.font.Font('./font/DSNDRA_.ttf', width//17)
    title = tfont.render('Tank War', True, (255, 0, 0))
    content1 = cfont.render('1 player', True, (0, 0, 255))
    content2 = cfont.render('2 player', True, (0, 0, 255))
    content3 = cfont.render('HOW TO PLAY', True, (0, 0, 255))
    content4 = cfont.render('QUIT', True, (0, 0, 255))
    trect = title.get_rect()
    trect.midtop = (width/2, height/4)
    crect1 = content1.get_rect()
    crect1.midtop = (width/2, height/1.8)
    crect2 = content2.get_rect()
    crect2.midtop = (width/2, height/1.6)
    crect3 = content3.get_rect()
    crect3.midtop = (width / 2, height / 1.4)
    crect4 = content4.get_rect()
    crect4.midtop = (width / 2, height / 1.2)
    screen.blit(bgs, (0,0))
    screen.blit(title, trect)
    screen.blit(content1, crect1)
    screen.blit(content2, crect2)
    screen.blit(content3, crect3)
    screen.blit(content4, crect4)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 1
                if event.key == pygame.K_2:
                    return 2
                if event.key == pygame.K_3:
                    inf = pygame.image.load("./images/others/information.png")
                    screen.blit(inf, (0, 0))
                    pygame.display.update()
                if event.key == pygame.K_HOME:
                    main()
                if event.key == pygame.K_4:
                    quit()
                if event.key == pygame.K_q:
                    quit()


# End screen display
def show_end_interface(screen, width, height, is_win):
    bg_img = pygame.image.load("./images/others/background.png")
    screen.blit(bg_img, (0, 0))
    if is_win:
        win_img = pygame.image.load("./images/others/youwin.png")
        rect = win_img.get_rect()
        rect.midtop = (width / 2, height / 2)
        screen.blit(win_img, rect)
    else:
        fail_img = pygame.image.load("./images/others/gameover.png")
        rect = fail_img.get_rect()
        rect.midtop = (width/2, height/2)
        screen.blit(fail_img, rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
                if event.key == pygame.K_q:
                    quit()


# Level switch
def show_switch_stage(screen, width, height, stage):
    bg_img = pygame.image.load("./images/others/background.png")
    screen.blit(bg_img, (0, 0))
    font = pygame.font.Font('./font/NP Happy new year_i.ttf', width//10)
    content = font.render('stage '+str(stage), True, (0, 250, 0))
    rect = content.get_rect()
    rect.midtop = (width/2, height/2)
    screen.blit(content, rect)
    pygame.display.update()
    time.sleep(1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit()
            return


# Main function
def main():
    # initialization
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((630, 630))
    pygame.display.set_caption("Tank War []=")
    # Loading image
    bg_img = pygame.image.load("./images/others/background.png")
    heart_img = pygame.image.load("./images/heart.png")
    # Load sound
    add_sound = pygame.mixer.Sound("./audios/add.wav")
    add_sound.set_volume(1)
    bang_sound = pygame.mixer.Sound("./audios/bang.wav")
    bang_sound.set_volume(1)
    blast_sound = pygame.mixer.Sound("./audios/blast.wav")
    blast_sound.set_volume(1)
    fire_sound = pygame.mixer.Sound("./audios/fire.wav")
    fire_sound.set_volume(1)
    Gunfire_sound = pygame.mixer.Sound("./audios/Gunfire.wav")
    Gunfire_sound.set_volume(1)
    hit_sound = pygame.mixer.Sound("./audios/hit.wav")
    hit_sound.set_volume(1)
    start_sound = pygame.mixer.Sound("./audios/start.wav")
    start_sound.set_volume(1)
    # Start interface
    num_player = show_start_interface(screen, 630, 630)
    # Play the music at the beginning of the game
    start_sound.play()
    # Level
    stage = 0
    num_stage = 2
    dead = 0
    # Whether the game is over
    is_gameover = False
    # clock
    clock = pygame.time.Clock()
    # Main loop
    while not is_gameover:
        # Level
        stage += 1
        if stage > num_stage:
            break
        show_switch_stage(screen, 630, 630, stage)
        # The total number of checkpoint tanks
        enemytanks_total = min(stage * 18, 80)
        # The total number of enemy tanks present on the field
        enemytanks_now = 0
        # The total number of enemy tanks that can exist on the field
        enemytanks_now_max = min(max(stage * 2, 4), 8)
        # Elf group
        tanksGroup = pygame.sprite.Group()
        mytanksGroup = pygame.sprite.Group()
        enemytanksGroup = pygame.sprite.Group()
        bulletsGroup = pygame.sprite.Group()
        mybulletsGroup = pygame.sprite.Group()
        enemybulletsGroup = pygame.sprite.Group()
        myfoodsGroup = pygame.sprite.Group()
        # Custom event
        # 	- Generate enemy tank events
        genEnemyEvent = pygame.constants.USEREVENT + 0
        pygame.time.set_timer(genEnemyEvent, 100)
        # 	- enemy tank stationary recovery event
        recoverEnemyEvent = pygame.constants.USEREVENT + 1
        pygame.time.set_timer(recoverEnemyEvent, 8000)
        # 	- Our tank invincible recovery event
        noprotectMytankEvent = pygame.constants.USEREVENT + 2
        pygame.time.set_timer(noprotectMytankEvent, 8000)
        # Level map
        map_stage = scene.Map(stage)
        # Our tank
        tank_player1 = tanks.myTank(1)
        tanksGroup.add(tank_player1)
        mytanksGroup.add(tank_player1)
        if num_player > 1:
            tank_player2 = tanks.myTank(2)
            tanksGroup.add(tank_player2)
            mytanksGroup.add(tank_player2)
        is_switch_tank = True
        player1_moving = False
        player2_moving = False
        # For the animation of the tire
        time = 0
        # Enemy tank
        for i in range(0, 3):
            if enemytanks_total > 0:
                enemytank = tanks.enemyTank(i)
                tanksGroup.add(enemytank)
                enemytanksGroup.add(enemytank)
                enemytanks_now += 1
                enemytanks_total -= 1
        # Base camp
        myhome = home.Home()
        # Appearance effects
        appearance_img = pygame.image.load("./images/others/appear.png").convert_alpha()
        appearances = []
        appearances.append(appearance_img.subsurface((0, 0), (48, 48)))
        appearances.append(appearance_img.subsurface((48, 0), (48, 48)))
        appearances.append(appearance_img.subsurface((96, 0), (48, 48)))
        # Level main loop
        while True:
            if is_gameover is True:
                break
            if enemytanks_total < 1 and enemytanks_now < 1:
                is_gameover = False
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit()
                if event.type == genEnemyEvent:
                    if enemytanks_total > 0:
                        if enemytanks_now < enemytanks_now_max:
                            enemytank = tanks.enemyTank()
                            if not pygame.sprite.spritecollide(enemytank, tanksGroup, False, None):
                                tanksGroup.add(enemytank)
                                enemytanksGroup.add(enemytank)
                                enemytanks_now += 1
                                enemytanks_total -= 1
                if event.type == recoverEnemyEvent:
                    for each in enemytanksGroup:
                        each.can_move = True
                if event.type == noprotectMytankEvent:
                    for each in mytanksGroup:
                        mytanksGroup.protected = False
            # Check user keyboard operations
            key_pressed = pygame.key.get_pressed()
            # Player one
            # WASD -> up and down
            # Space bar shooting
            if key_pressed[pygame.K_w]:
                tanksGroup.remove(tank_player1)
                tank_player1.move_up(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
                tanksGroup.add(tank_player1)
                player1_moving = True
            elif key_pressed[pygame.K_s]:
                tanksGroup.remove(tank_player1)
                tank_player1.move_down(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
                tanksGroup.add(tank_player1)
                player1_moving = True
            elif key_pressed[pygame.K_a]:
                tanksGroup.remove(tank_player1)
                tank_player1.move_left(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
                tanksGroup.add(tank_player1)
                player1_moving = True
            elif key_pressed[pygame.K_d]:
                tanksGroup.remove(tank_player1)
                tank_player1.move_right(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
                tanksGroup.add(tank_player1)
                player1_moving = True
            elif key_pressed[pygame.K_SPACE]:
                if not tank_player1.bullet.being:
                    fire_sound.play()
                    tank_player1.shoot()
            # Player teo
            # ↑↓←→ -> Up, down, left and right
            # Keypad 0 key shot
            if num_player > 1:
                if key_pressed[pygame.K_UP]:
                    tanksGroup.remove(tank_player2)
                    tank_player2.move_up(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
                    tanksGroup.add(tank_player2)
                    player2_moving = True
                elif key_pressed[pygame.K_DOWN]:
                    tanksGroup.remove(tank_player2)
                    tank_player2.move_down(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
                    tanksGroup.add(tank_player2)
                    player2_moving = True
                elif key_pressed[pygame.K_LEFT]:
                    tanksGroup.remove(tank_player2)
                    tank_player2.move_left(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
                    tanksGroup.add(tank_player2)
                    player2_moving = True
                elif key_pressed[pygame.K_RIGHT]:
                    tanksGroup.remove(tank_player2)
                    tank_player2.move_right(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
                    tanksGroup.add(tank_player2)
                    player2_moving = True
                elif key_pressed[pygame.K_KP0]:
                    if not tank_player2.bullet.being:
                        fire_sound.play()
                        tank_player2.shoot()
            # background
            screen.blit(bg_img, (0, 0))
            # Stone wall
            for each in map_stage.brickGroup:
                screen.blit(each.brick, each.rect)
            # Steel wall
            for each in map_stage.ironGroup:
                screen.blit(each.iron, each.rect)
            time += 1
            if time == 5:
                time = 0
                is_switch_tank = not is_switch_tank
            # Our tank
            if tank_player1 in mytanksGroup:
                if is_switch_tank and player1_moving:
                    screen.blit(tank_player1.tank_0, (tank_player1.rect.left, tank_player1.rect.top))
                    player1_moving = False
                else:
                    screen.blit(tank_player1.tank_1, (tank_player1.rect.left, tank_player1.rect.top))
                if tank_player1.protected:
                    screen.blit(tank_player1.protected_mask1, (tank_player1.rect.left, tank_player1.rect.top))
            if num_player > 1:
                if tank_player2 in mytanksGroup:
                    if is_switch_tank and player2_moving:
                        screen.blit(tank_player2.tank_0, (tank_player2.rect.left, tank_player2.rect.top))
                        player1_moving = False
                    else:
                        screen.blit(tank_player2.tank_1, (tank_player2.rect.left, tank_player2.rect.top))
                    if tank_player2.protected:
                        screen.blit(tank_player1.protected_mask1, (tank_player2.rect.left, tank_player2.rect.top))
            # Enemy tank
            for each in enemytanksGroup:
                # Birth effect
                if each.born:
                    if each.times > 0:
                        each.times -= 1
                        if each.times <= 10:
                            screen.blit(appearances[2], (3+each.x*12*24, 3))
                        elif each.times <= 20:
                            screen.blit(appearances[1], (3+each.x*12*24, 3))
                        elif each.times <= 30:
                            screen.blit(appearances[0], (3+each.x*12*24, 3))
                        elif each.times <= 40:
                            screen.blit(appearances[2], (3+each.x*12*24, 3))
                        elif each.times <= 50:
                            screen.blit(appearances[1], (3+each.x*12*24, 3))
                        elif each.times <= 60:
                            screen.blit(appearances[0], (3+each.x*12*24, 3))
                        elif each.times <= 70:
                            screen.blit(appearances[2], (3+each.x*12*24, 3))
                        elif each.times <= 80:
                            screen.blit(appearances[1], (3+each.x*12*24, 3))
                        elif each.times <= 90:
                            screen.blit(appearances[0], (3+each.x*12*24, 3))
                    else:
                        each.born = False
                else:
                    if is_switch_tank:
                        screen.blit(each.tank_0, (each.rect.left, each.rect.top))
                    else:
                        screen.blit(each.tank_1, (each.rect.left, each.rect.top))
                    if each.can_move:
                        tanksGroup.remove(each)
                        each.move(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
                        tanksGroup.add(each)
            # Our bullets
            for tank_player in mytanksGroup:
                if tank_player.bullet.being:
                    tank_player.bullet.move()
                    screen.blit(tank_player.bullet.bullet, tank_player.bullet.rect)
                    # Bullet colliding with enemy bullets
                    for each in enemybulletsGroup:
                        if each.being:
                            if pygame.sprite.collide_rect(tank_player.bullet, each):
                                tank_player.bullet.being = False
                                each.being = False
                                enemybulletsGroup.remove(each)
                                break
                        else:
                            enemybulletsGroup.remove(each)
                    # Bullet colliding with enemy tank
                    for each in enemytanksGroup:
                        if each.being:
                            if pygame.sprite.collide_rect(tank_player.bullet, each):
                                if each.is_red == True:
                                    myfood = food.Food()
                                    myfood.generate()
                                    myfoodsGroup.add(myfood)
                                    each.is_red = False
                                each.blood -= 1
                                each.color -= 1
                                if each.blood < 0:
                                    bang_sound.play()
                                    each.being = False
                                    enemytanksGroup.remove(each)
                                    enemytanks_now -= 1
                                    tanksGroup.remove(each)
                                else:
                                    each.reload()
                                tank_player.bullet.being = False
                                break
                        else:
                            enemytanksGroup.remove(each)
                            tanksGroup.remove(each)
                    # Bullet collision stone wall
                    if pygame.sprite.spritecollide(tank_player.bullet, map_stage.brickGroup, True, None):
                        tank_player.bullet.being = False
                    # Bullet hitting steel wall
                    if tank_player.bullet.stronger:
                        if pygame.sprite.spritecollide(tank_player.bullet, map_stage.ironGroup, True, None):
                            tank_player.bullet.being = False
                    else:
                        if pygame.sprite.spritecollide(tank_player.bullet, map_stage.ironGroup, False, None):
                            tank_player.bullet.being = False
                    # Bullet hits the base camp
                    if pygame.sprite.collide_rect(tank_player.bullet, myhome):
                        tank_player.bullet.being = False
                        myhome.set_dead()
                        is_gameover = True
            # Enemy bullet
            for each in enemytanksGroup:
                if each.being:
                    if each.can_move and not each.bullet.being:
                        enemybulletsGroup.remove(each.bullet)
                        each.shoot()
                        enemybulletsGroup.add(each.bullet)
                    if not each.born:
                        if each.bullet.being:
                            each.bullet.move()
                            screen.blit(each.bullet.bullet, each.bullet.rect)
                            # Bullet colliding with our tank
                            for tank_player in mytanksGroup:
                                if pygame.sprite.collide_rect(each.bullet, tank_player):
                                    if not tank_player.protected:
                                        bang_sound.play()
                                        tank_player.life -= 1
                                        dead += 1
                                        if tank_player.life < 0:
                                            mytanksGroup.remove(tank_player)
                                            tanksGroup.remove(tank_player)
                                            if len(mytanksGroup) < 1:
                                                is_gameover = True
                                        else:
                                            tank_player.reset()
                                    each.bullet.being = False
                                    enemybulletsGroup.remove(each.bullet)
                                    break
                            # Bullet collision stone wall
                            if pygame.sprite.spritecollide(each.bullet, map_stage.brickGroup, True, None):
                                each.bullet.being = False
                                enemybulletsGroup.remove(each.bullet)
                            # Bullet hitting steel wall
                            if each.bullet.stronger:
                                if pygame.sprite.spritecollide(each.bullet, map_stage.ironGroup, True, None):
                                    each.bullet.being = False
                            else:
                                if pygame.sprite.spritecollide(each.bullet, map_stage.ironGroup, False, None):
                                    each.bullet.being = False
                            # Bullet hits the base camp
                            if pygame.sprite.collide_rect(each.bullet, myhome):
                                each.bullet.being = False
                                myhome.set_dead()
                                is_gameover = True
                else:
                    enemytanksGroup.remove(each)
                    tanksGroup.remove(each)
            # Home
            if dead == 0:
                screen.blit(heart_img, (580, 590))
                screen.blit(heart_img, (560, 590))
                screen.blit(heart_img, (540, 590))
            if dead == 1:
                screen.blit(heart_img, (580, 590))
                screen.blit(heart_img, (560, 590))
            if dead == 2:
                screen.blit(heart_img, (580, 590))
            screen.blit(myhome.home, myhome.rect)
            # Food
            for myfood in myfoodsGroup:
                if myfood.being and myfood.time > 0:
                    screen.blit(myfood.food, myfood.rect)
                    myfood.time -= 1
                    for tank_player in mytanksGroup:
                        if pygame.sprite.collide_rect(tank_player, myfood):
                            # Destroy all current enemies
                            if myfood.kind == 0:
                                for _ in enemytanksGroup:
                                    bang_sound.play()
                                enemytanksGroup = pygame.sprite.Group()
                                enemytanks_total -= enemytanks_now
                                enemytanks_now = 0
                            # Enemy still
                            if myfood.kind == 1:
                                for each in enemytanksGroup:
                                    each.can_move = False
                            # Bullet enhancement
                            if myfood.kind == 2:
                                add_sound.play()
                                tank_player.bullet.stronger = True
                            # Make the wall of the base camp into a steel plate
                            if myfood.kind == 3:
                                map_stage.protect_home()
                            # The tank gets a protective cover for a while
                            if myfood.kind == 4:
                                add_sound.play()
                                for tank_player in mytanksGroup:
                                    tank_player.protected = True
                            # Tank upgrade
                            if myfood.kind == 5:
                                add_sound.play()
                                tank_player.up_level()
                            # Tank life +1
                            if myfood.kind == 6:
                                add_sound.play()
                                tank_player.life += 1
                            myfood.being = False
                            myfoodsGroup.remove(myfood)
                            break
                else:
                    myfood.being = False
                    myfoodsGroup.remove(myfood)
            pygame.display.flip()
            clock.tick(60)
    if not is_gameover:
        show_end_interface(screen, 630, 630, True)
    else:
        show_end_interface(screen, 630, 630, False)



if __name__ == '__main__':
    main()