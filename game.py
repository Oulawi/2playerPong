import pygame
from random import randint

pygame.init()
pygame.display.set_caption("Multiplayer Pong Courtesy of Olavi")

def draw_score(score1, score2):

    leftCorner = [324, 60]

    upLeft1 = pygame.Rect(leftCorner[0], leftCorner[1] + 6, 6, 24)
    downLeft1 = pygame.Rect(leftCorner[0], leftCorner[1] + 36, 6, 24)
    up1 = pygame.Rect(leftCorner[0] + 6, leftCorner[1], 24, 6)
    upRight1 = pygame.Rect(leftCorner[0] + 30, leftCorner[1] + 6, 6, 24)
    downRight1 = pygame.Rect(leftCorner[0] + 30, leftCorner[1] + 36, 6, 24)
    mid1 = pygame.Rect(leftCorner[0] + 6, leftCorner[1] + 30, 24, 6)
    down1 = pygame.Rect(leftCorner[0] + 6, leftCorner[1] + 60, 24, 6)

    if score1 == 1:
        pygame.draw.rect(screen, white, upLeft1)
        pygame.draw.rect(screen, white, downLeft1)
    elif score1 == 2:
        pygame.draw.rect(screen, white, up1)
        pygame.draw.rect(screen, white, mid1)
        pygame.draw.rect(screen, white, down1)
        pygame.draw.rect(screen, white, upRight1)
        pygame.draw.rect(screen, white, downLeft1)
    elif score1 == 3:
        pygame.draw.rect(screen, white, up1)
        pygame.draw.rect(screen, white, mid1)
        pygame.draw.rect(screen, white, down1)
        pygame.draw.rect(screen, white, upRight1)
        pygame.draw.rect(screen, white, downRight1)
    elif score1 == 4:
        pygame.draw.rect(screen, white, upLeft1)
        pygame.draw.rect(screen, white, upRight1)
        pygame.draw.rect(screen, white, mid1)
        pygame.draw.rect(screen, white, downRight1)
    elif score1 == 5:
        pygame.draw.rect(screen, white, up1)
        pygame.draw.rect(screen, white, upLeft1)
        pygame.draw.rect(screen, white, mid1)
        pygame.draw.rect(screen, white, downRight1)
        pygame.draw.rect(screen, white, down1)
    elif score1 == 6:
        pygame.draw.rect(screen, white, up1)
        pygame.draw.rect(screen, white, upLeft1)
        pygame.draw.rect(screen, white, mid1)
        pygame.draw.rect(screen, white, downRight1)
        pygame.draw.rect(screen, white, downLeft1)
        pygame.draw.rect(screen, white, down1)
    elif score1 == 7:
        pygame.draw.rect(screen, white, up1)
        pygame.draw.rect(screen, white, downRight1)
        pygame.draw.rect(screen, white, upRight1)
    elif score1 == 8:
        pygame.draw.rect(screen, white, upLeft1)
        pygame.draw.rect(screen, white, downLeft1)
        pygame.draw.rect(screen, white, up1)
        pygame.draw.rect(screen, white, upRight1)
        pygame.draw.rect(screen, white, downRight1)
        pygame.draw.rect(screen, white, mid1)
        pygame.draw.rect(screen, white, down1)
    elif score1 == 9:
        pygame.draw.rect(screen, white, upLeft1)
        pygame.draw.rect(screen, white, up1)
        pygame.draw.rect(screen, white, upRight1)
        pygame.draw.rect(screen, white, downRight1)
        pygame.draw.rect(screen, white, mid1)
        pygame.draw.rect(screen, white, down1)


    rightCorner = [240, 60]

    upLeft2 = pygame.Rect(rightCorner[0], rightCorner[1] + 6, 6, 24)
    downLeft2 = pygame.Rect(rightCorner[0], rightCorner[1] + 36, 6, 24)
    up2 = pygame.Rect(rightCorner[0] + 6, rightCorner[1], 24, 6)
    upRight2 = pygame.Rect(rightCorner[0] + 30, rightCorner[1] + 6, 6, 24)
    downRight2 = pygame.Rect(rightCorner[0] + 30, rightCorner[1] + 36, 6, 24)
    mid2 = pygame.Rect(rightCorner[0] + 6, rightCorner[1] + 30, 24, 6)
    down2 = pygame.Rect(rightCorner[0] + 6, rightCorner[1] + 60, 24, 6)

    if score2 == 1:
        pygame.draw.rect(screen, white, upRight2)
        pygame.draw.rect(screen, white, downRight2)
    elif score2 == 2:
        pygame.draw.rect(screen, white, up2)
        pygame.draw.rect(screen, white, mid2)
        pygame.draw.rect(screen, white, down2)
        pygame.draw.rect(screen, white, upRight2)
        pygame.draw.rect(screen, white, downLeft2)
    elif score2 == 3:
        pygame.draw.rect(screen, white, up2)
        pygame.draw.rect(screen, white, mid2)
        pygame.draw.rect(screen, white, down2)
        pygame.draw.rect(screen, white, upRight2)
        pygame.draw.rect(screen, white, downRight2)
    elif score2 == 4:
        pygame.draw.rect(screen, white, upLeft2)
        pygame.draw.rect(screen, white, upRight2)
        pygame.draw.rect(screen, white, mid2)
        pygame.draw.rect(screen, white, downRight2)
    elif score2 == 5:
        pygame.draw.rect(screen, white, up2)
        pygame.draw.rect(screen, white, upLeft2)
        pygame.draw.rect(screen, white, mid2)
        pygame.draw.rect(screen, white, downRight2)
        pygame.draw.rect(screen, white, down2)
    elif score2 == 6:
        pygame.draw.rect(screen, white, up2)
        pygame.draw.rect(screen, white, upLeft2)
        pygame.draw.rect(screen, white, mid2)
        pygame.draw.rect(screen, white, downRight2)
        pygame.draw.rect(screen, white, downLeft2)
        pygame.draw.rect(screen, white, down2)
    elif score2 == 7:
        pygame.draw.rect(screen, white, up2)
        pygame.draw.rect(screen, white, downRight2)
        pygame.draw.rect(screen, white, upRight2)
    elif score2 == 8:
        pygame.draw.rect(screen, white, upLeft2)
        pygame.draw.rect(screen, white, downLeft2)
        pygame.draw.rect(screen, white, up2)
        pygame.draw.rect(screen, white, upRight2)
        pygame.draw.rect(screen, white, downRight2)
        pygame.draw.rect(screen, white, mid2)
        pygame.draw.rect(screen, white, down2)
    elif score2 == 9:
        pygame.draw.rect(screen, white, upLeft2)
        pygame.draw.rect(screen, white, up2)
        pygame.draw.rect(screen, white, upRight2)
        pygame.draw.rect(screen, white, downRight2)
        pygame.draw.rect(screen, white, mid2)
        pygame.draw.rect(screen, white, down2)

clock = pygame.time.Clock()
tickrate = 50
screen = pygame.display.set_mode([600, 400])
done = False

rainbow = [[148, 0, 211],[75,0,130],[0,0,255],[0,255,0],[255,255,0],[255,127,0],[255,0,0]]
rainbowticker = 0


player1Score = 0
player2Score = 0

ballVector = [-10, 0]
player1 = 110
player2 = 110



def ball_reset():
    ballVector[1] = 0
    ballCoor[0] = 300
    ballCoor[1] = 200
    pygame.time.wait(1500)
    ballVector[0] = 10 * (-1)**randint(1,2)



black = [0, 0, 0]
white = [255, 255, 255]

ballCoor = [300, 200]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Game logic here
    #Some definitions...
    hitbox1 = [player1 - 10, player1 + 60]
    hitbox2 = [player2 - 10, player2 + 60]


    #Controls
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and player1 != 0:
        player1 -= 10
    elif pressed[pygame.K_DOWN] and player1 != 340:
        player1 += 10

    if pressed[pygame.K_w] and player2 != 0:
        player2 -= 10
    elif pressed[pygame.K_s] and player2 != 340:
        player2 += 10

    #Checking collisions
    if ballCoor[0] <= 10 and ballCoor[1] in range(hitbox1[0], hitbox1[1]):
        ballVector[0] = (-1)*ballVector[0]
        ballVector[1] = round((ballCoor[1] - ((hitbox1[0] + hitbox1[1])/2)) * 0.35, 0)
        tickrate += 1

    elif ballCoor[0] >= 579 and ballCoor[1] in range(hitbox2[0] - 10, hitbox2[1] + 10):
        ballVector[0] = (-1)*ballVector[0]
        ballVector[1] = round((ballCoor[1] - ((hitbox2[0] + hitbox2[1]) / 2)) * 0.35, 0)
        tickrate += 1

    #Edge collisions
    if ballCoor[1] <= 0:
        ballVector[1] = (-1)*ballVector[1]
    elif ballCoor[1] >= 389:
        ballVector[1] = (-1)*ballVector[1]


    #Ball moves
    ballCoor[0] += ballVector[0]
    ballCoor[1] += ballVector[1]

    #Check win conditions
    if ballCoor[0] <= -10:
        player1Score += 1
        ball_reset()
        tickrate = 28
    elif ballCoor[0] >= 600:
        player2Score += 1
        ball_reset()
        tickrate = 28


    screen.fill(rainbow[rainbowticker % 7])
    #Draw here
    #draw ball
    pygame.draw.rect(screen, rainbow[(rainbowticker + 1) % 7], pygame.Rect(ballCoor[0], ballCoor[1], 11, 11))

    #draw paddles
    pygame.draw.rect(screen, rainbow[(rainbowticker + 2) % 7], pygame.Rect(0, player1, 10, 60))
    pygame.draw.rect(screen, rainbow[(rainbowticker + 3) % 7], pygame.Rect(590, player2, 10, 60))

    #Draw midline
    pygame.draw.rect(screen, rainbow[(rainbowticker + 4) % 7], pygame.Rect(299, 0, 2, 400))

    draw_score(player1Score, player2Score)
    if player1Score == 10 or player2Score == 10:
        done = True

    rainbowticker += 1

    pygame.display.update()
    pygame.display.flip()
    clock.tick(tickrate)

pygame.quit()