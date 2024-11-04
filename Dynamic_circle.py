""" Dynamic circle - Size """

import pygame 

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the window
screen_width, screen_heigth = 600, 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_heigth), pygame.DOUBLEBUF)
pygame.display.set_caption('Dynamic Ebbinghaus Titchener')
screen.fill(WHITE)

# Variables 
## Reference x, y for circles' coordinates
ref_x = screen_width/4
ref_y = screen_heigth/4

## Radius' references 
radius = 25
radius_change=5

#Create clock object
clock = pygame.time.Clock()

# ------ Main program loop (Animation) -----
run = True
while run:
        # ----- Event handler 
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                        run = False
        pygame.display.update()

        # ----- LOGIC
        radius += radius_change

        if radius <25 or radius > 150:
                radius_change *= -1

        #----- DRAWING 
        #new white canvas for a new frame
        screen.fill(WHITE)

        #Draw the circle 
        pygame.draw.circle(screen, BLACK, (ref_x*2, ref_y*2), radius)

        #Update screen
        pygame.display.flip()

        #Set frame rate (frames/second)
        clock.tick(30)

pygame.quit()