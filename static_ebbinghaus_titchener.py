""" Static Ebbinghaus Titchener
Static circle in the middle surrounded by six circles whose diameter increase and decrease over time """

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

# ----- Variables ------
# Create clock object
clock = pygame.time.Clock()

# Reference x, y for circles' coordinates
ref_x = screen_width/4
ref_y = screen_heigth/4

# Radius' references 
radius = 25
radius_change=2

# Coordinate factors (list)
coord_fact = [
    # right circle 
    (3,2), (2.5,1), (2.5,3),
    # left circles 
    (1,2), (1.5, 1), (1.5, 3)]

# ------ Main program loop (Animation) -----
run = True
while run:
        # ----- EVENT HANDLER  
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                        run = False
        pygame.display.update()

        # ----- LOGIC
        radius += radius_change

        if radius <25 or radius > 60:
                radius_change *= -1
        
        #----- DRAWING 
        #new white canvas for a new frame
        screen.fill(WHITE)

        # Center circle
        pygame.draw.circle(screen, BLACK, (ref_x*2, ref_y*2), 25)
        
        # Surround circles 
        for x, y in coord_fact:
            pygame.draw.circle(screen, BLACK, (ref_x*x, ref_y*y), radius)

        #Update screen
        pygame.display.flip()

        #Set frame rate (frames/second)
        clock.tick(20)

pygame.quit()