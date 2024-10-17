"""Kanisza triangle (visual illusion) """

import pygame 

#Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (50,200, 255)
PINK = (240, 170, 240)
GREY = (128, 128, 128)

#Create the window 
W, H = 500, 500
center_x = W // 2
center_y = H // 2

pygame.init()

screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
screen.fill(WHITE)

#Drawing circles 
radius = 40
shift = 100

pygame.draw.circle(screen, BLACK, (center_x, center_y-shift), radius, 0)
pygame.draw.circle(screen, BLACK, (center_x-shift, center_y+shift), radius, 0)
pygame.draw.circle(screen, BLACK, (center_x + shift, center_y+shift), radius, 0)


pygame.draw.polygon(screen, BLACK, ([center_x, center_y+1.5*shift], [center_x-shift, center_y-1/2*shift], [center_x+shift, center_y-1/2*shift]), 1)
pygame.draw.polygon(screen, WHITE, ([center_x, center_y-shift], [center_x-shift, center_y+shift], [center_x + shift, center_y +shift]))

pygame.display.flip()
    

#Boucle pour garder la fenêtre ouverte, sauf si action fermeture 
done = False
while not done:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()