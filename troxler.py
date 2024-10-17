""" Troxler effect (visual illusion)
Fixate your gaze at the center of the picture below for 30 seconds to see the fill-in effect """

import pygame 

#Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (50,200, 255)
PINK = (240, 170, 240)
GREEN = (170, 240, 180)

#Create the window 
W, H = 500, 500
center_x = W // 2
center_y = H // 2

pygame.init()

screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
screen.fill(WHITE)

#Drawing the circles 
radius = 20
horiz_shift = 150  # x position relative to center

pygame.draw.circle(screen, BLUE, (center_x - horiz_shift, center_y), radius, 0)
pygame.draw.circle(screen, PINK, (center_x - horiz_shift, center_y-horiz_shift), radius, 0)
pygame.draw.circle(screen, GREEN, (center_x - horiz_shift, center_y+horiz_shift), radius, 0)

pygame.draw.circle(screen, GREEN, (center_x, center_y-horiz_shift), radius, 0)
pygame.draw.circle(screen, PINK, (center_x, center_y+horiz_shift), radius, 0)

pygame.draw.circle(screen, PINK, (center_x + horiz_shift, center_y-horiz_shift), radius, 0)
pygame.draw.circle(screen, BLUE, (center_x + horiz_shift, center_y), radius, 0)
pygame.draw.circle(screen, GREEN, (center_x + horiz_shift, center_y+horiz_shift), radius, 0)

pygame.draw.circle(screen, BLACK, (center_x, center_y), 2, 0)


pygame.display.flip()

#pygame.image.save(screen, "troxler.png")

#See what this does 
done = False
while not done:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()