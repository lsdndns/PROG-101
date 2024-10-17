""" Kanizasa square (visual illusion)"""

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
screen.fill(GREY)

#Drawing circles 
radius = 50
horiz_shift = 100

pygame.draw.circle(screen, BLACK, (center_x - horiz_shift, center_y - horiz_shift), radius, 0)
pygame.draw.circle(screen, BLACK, (center_x + horiz_shift, center_y-horiz_shift), radius, 0)

pygame.draw.circle(screen, WHITE, (center_x - horiz_shift, center_y + horiz_shift), radius, 0)
pygame.draw.circle(screen, WHITE, (center_x + horiz_shift, center_y+horiz_shift), radius, 0)

# Drawing a square (coordinate x, y of the top left corner, width, heighth)
pygame.draw.rect(screen, GREY, (center_x - horiz_shift, center_y - horiz_shift, (2*horiz_shift), (2*horiz_shift)))

pygame.display.flip()
    

#Boucle pour garder la fenêtre ouverte, sauf si action fermeture 
done = False
while not done:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()