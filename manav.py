import pygame
import random
import math
import pyttsx3
from pygame import mixer


red = (200, 0, 0)
light_red = (255, 0, 0) 

black = (0, 0, 0)
white = (225, 225, 225)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (0, 115, 0)
light_green = (0, 225, 0)


# calling init()
pygame.init()

# creating a gamedisplay
gamedisplay = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('screenshot.png')

# background sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# icon and caption
pygame.display.set_caption('space invader')
icon = pygame.image.load('spring.png')
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load('gaming.png')
playerx = 370
playery = 480
playerx_change = 0

# enemy
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('avatar.png'))
    enemyx.append(random.randint(0, 750))
    enemyy.append(random.randint(50, 150))
    enemyx_change.append(5)
    enemyy_change.append(40)

bullitimg = pygame.image.load('misc.png')
bullitx = 0
bullity = 480
bullitx_change = 0
bullity_change = 20
bullit_state = "ready"


def bullit_fire(x, y):
    global bullit_state
    bullit_state = "fire"
    gamedisplay.blit(bullitimg, (x + 12, y + 10))


def iscollision(enemyx, enemyy, bullitx, bullity):
    distance = math.sqrt((math.pow(enemyx - bullitx, 2)) + (math.pow(enemyy - bullity, 2)))
    if distance < 27:
        return True
    else:
        return False


# score

score_value = 0

font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10

# game over
over_font = pygame.font.Font('freesansbold.ttf', 60)


def show_score(x, y):
    score = font.render("score : " + str(score_value), True, (255, 255, 255))
    gamedisplay.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    gamedisplay.blit(over_text, (200, 250))


def player():
    gamedisplay.blit(playerimg, (playerx, playery))


def enemy(x, y, i):
    gamedisplay.blit(enemyimg[i], (x, y))


running = True
while running:
    gamedisplay.fill((0, 0, 0))
    # background
    gamedisplay.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -8
            if event.key == pygame.K_RIGHT:
                playerx_change = 8
            if event.key == pygame.K_SPACE:
                if bullit_state is "ready":
                    bullit_sound = mixer.Sound("laser.wav")
                    bullit_sound.play()
                    bullitx = playerx
                    bullit_fire(bullitx, bullity)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    playerx += playerx_change
    if playerx <= 0:
           playerx = 0
    elif playerx >= 750:
        playerx = 750

    for i in range(num_of_enemies):

        # game over
        if enemyy[i] > 480:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break

        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 5
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 750:
            enemyx_change[i] = -5
            enemyy[i] += enemyy_change[i]

        colusion = iscollision(enemyx[i], enemyy[i], bullitx, bullity)
        if colusion:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bullity = 480
            bullit_state = "ready"
            score_value += 1
            enemyx[i] = random.randint(0, 750)
            enemyy[i] = random.randint(50, 150)
        enemy(enemyx[i], enemyy[i], i)

    if bullity <= 0:
        bullity = 480
        bullit_state = "ready"

    if bullit_state is "fire":
        bullit_fire(bullitx, bullity)
        bullity -= bullity_change

    show_score(textx, texty)
    player()

    pygame.display.update()







    
