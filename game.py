import pygame

pygame.init()
pygame.display.set_caption("Multiplayer Pong Courtesy of Olavi")

clock = pygame.time.Clock()
tickrate = 64
screen = pygame.display.set_mode([400, 400])
done = False

ballVector = [3, 4]

black = [0, 0, 0]
white = [255, 255, 255]

ballCoor = [200, 200]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Game logic here
    ballCoor[0] += ballVector[0]
    ballCoor[1] += ballVector[1]

    screen.fill(black)
    #Draw here

    pygame.draw.rect(screen, white, pygame.Rect(ballCoor[0], ballCoor[1], 10, 10))

    pygame.display.update()
    pygame.display.flip()
    clock.tick(tickrate)
