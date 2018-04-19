import pygame

pygame.init()
pygame.display.set_caption("Multiplayer Pong Courtesy of Olavi")
screen = pygame.display.set_mode([400, 400])
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            done = True

    #Game logic here

    screen.fill(black)
    #Draw here

    pygame.display.update()
    pygame.display.flip()
    clock.tick(tickrate)
