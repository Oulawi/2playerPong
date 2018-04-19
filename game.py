import pygame

pygame.init()
pygame.display.set_caption("Multiplayer Pong Courtesy of Olavi")

clock = pygame.time.Clock()
tickrate = 64
screen = pygame.display.set_mode([600, 400])
done = False

ballVector = [5, 0]
player1 = 110
player2 = 110


black = [0, 0, 0]
white = [255, 255, 255]

ballCoor = [300, 200]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Game logic here
    #Controls
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and player1 != 0:
        player1 -= 10
    elif pressed[pygame.K_DOWN] and player1 != 350:
        player1 += 10

    if pressed[pygame.K_w] and player2 != 0:
        player2 -= 10
    elif pressed[pygame.K_s] and player2 != 350:
        player2 += 10

    ballCoor[0] += ballVector[0]
    ballCoor[1] += ballVector[1]

    screen.fill(black)
    #Draw here
    #draw ball
    pygame.draw.rect(screen, white, pygame.Rect(ballCoor[0], ballCoor[1], 10, 10))

    #draw paddles
    pygame.draw.rect(screen, white, pygame.Rect(0, player1, 10, 50))
    pygame.draw.rect(screen, white, pygame.Rect(590, player2, 10, 50))

    pygame.display.update()
    pygame.display.flip()
    clock.tick(tickrate)
