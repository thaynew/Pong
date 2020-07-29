import pygame
from pygame import mixer
import random
import math

#initilizing the game
pygame.init()
WIDTH = 800
HEIGHT = 600
#Creating the screen (W, H)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
#background


#background sound


#Title and ICON
pygame.display.set_caption("pong")

#Player
playerImg = pygame.image.load('bone.png')
playerX = -7
playerY = 300
playerY_change = 0

#enemy
enemyImg = pygame.image.load('bone.png')
enemyX = 775
enemyY = 300
enemyY_change = 0

#Ball
ballImg = pygame.image.load('sport.png')
ballX = 390
ballY = 300
ballX_change = 3
ballY_change = 3

#scores
font = pygame.font.Font('freesansbold.ttf',16)
player_score_value = 0
player_textX = 100
player_textY = 10
player_score = 0
enemy_score_value = 0
enemy_textX = 500
enemy_textY = 10
enemy_score = 0

def player_show_score(x, y):
    player_score = font.render("score : " + str(player_score_value), True, (0,255,0))
    screen.blit(player_score, (x, y))

def enemy_show_score(x, y):
    enemy_score = font.render("score : " + str(enemy_score_value), True, (255,0,0))
    screen.blit(enemy_score, (x, y))

def isCollision(enemyX, enemyY, ballX, ballY):
    distance = math.sqrt((math.pow(enemyX-ballX, 2))+ (math.pow(enemyY-ballY, 2)))
    if distance < 27:
        return True
    else:
        return False

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def ball(x, y):
    screen.blit(ballImg, (x, y))


#Game loop - Makes sure the game is running.
running = True
while running:

    #Add color to the screen, Replaceable with a photo?
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255,255,255), [(WIDTH/2),0], [WIDTH/2,800], 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # if keystroke is pressed check wherther is up or down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -4
            if event.key == pygame.K_DOWN:
                playerY_change = 4
            if event.key == pygame.K_w:
                enemyY_change = -4
            if event.key == pygame.K_s:
                enemyY_change = 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                enemyY_change = 0

    #Keeps player in the screen
    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 565:
        playerY = 565

    #Keeps enemy in the screen and helps to move it
    enemyY += enemyY_change
    if enemyY <= 0:
        enemyY = 0
    elif enemyY >= 565:
        enemyY = 565
    
    #ball movement
    ballX = (ballX + ballX_change)
    ballY = (ballY + ballY_change)
    

    #boader checking
    if ballY > 575:
        ballY = 575
        ballY_change *= -1
    
    if ballY < 0:
        ballY = 0
        ballY_change *= -1

    if ballX > 790:
        player_score_value += 1
        ballX = 390
        ballY = 300
        ballY_change *= -1

    if ballX < 0:
        enemy_score_value += 1
        ballX = 390
        ballY = 300
        ballY_change *= -1

    #Check for player collision
    if (ballX > 760 and ballX < 780) and (ballY < enemyY+36 and ballY > enemyY-36):
        ballX_change *= -1
    if (ballX > 10 and ballX < 15) and (ballY < playerY+36 and ballY > playerY-36):
        ballX_change *= -1

    player(playerX, playerY)
    ball(ballX, ballY)
    enemy(enemyX, enemyY)
    player_show_score(player_textX, player_textY)
    enemy_show_score(enemy_textX, enemy_textY)
    
    pygame.display.update()
    print(clock.tick(60))