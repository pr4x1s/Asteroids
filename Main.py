#TO DO:
#Make image, find way to blit
#
#
import Player
import pygame
import time
#SETUP ---------------------------------------------
pygame.init()
window  = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Asteroids")
pygame.key.set_repeat(1)
test_rect = pygame.Surface((400, 300), pygame.SRCALPHA)
pygame.draw.rect(test_rect, (0, 0, 0), (400, 300, 10, 10))
done = False
player = Player.Player()
print player.toString()
#---------------------------------------------------
clock = pygame.time.Clock()
while done is not True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_UP:
                if player.speed < player.maxSpeed:
                    player.speed += 1
                    player.negativeVelocity = False
                else:
                    player.speed = 20

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.negativeVelocity = True
    if player.negativeVelocity is True and player.speed > 0:
        player.speed -= 1
    if player.y <= 590:
        player.y = player.y + player.speed
    window.blit(test_rect, (400, player.y))
    window.fill((255,255,255))
    pygame.display.flip()
    print player.y
