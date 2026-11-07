import pygame
import random
import math

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
PLAYER_START_X=370
PLAYER_START_Y=380
enemy_start_position_x = random.randint(0, SCREEN_WIDTH - 64)
enemy_start_position_y = random.randint(50, 150)
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED=10
COLLISION_SCORE=1
ENEMY_COUNT=7

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background=pygame.image.load('ATTACK.avif')
playerImg=pygame.image.load('MECH.jpg')
enemyImg=pygame.image.load('ATTACKERS.jpg')
icon=pygame.image.load('ATTACKERS.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invader")
playerX=PLAYER_START_X
playerY=PLAYER_START_Y
playerX_change=0
playerY_change=0
point_change=0
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerX -= 5
    if keys[pygame.K_RIGHT]:
        playerX += 5

    screen.blit(background, (0, 0))
    screen.blit(enemyImg, (enemy_start_position_x, enemy_start_position_y))
    screen.blit(playerImg, (playerX, playerY))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()