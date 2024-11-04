""" Lilac chaser """

import pygame 
import numpy

# ----- VARIABLES 
# Clock object
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREY = (211, 213, 211) 
PINK = (255, 192, 203)

# Circles
n = 12
radius_center = 25
invisible = 0
col = PINK 

# ----- FUNCTION
def Lilac_chaser(surface, n, distance, radius, col, invisible, x, y):
        """ Draws a circle surrounded by outer ones.

        Arguments:
            surface: pygame surface to display the stimulus on
            n: number of circles
            distance: distance between the fixation point and circles
            radius: radius of circles
            col: color of the circles
            invisible: index of the circle to be invisible
            x, y: coordinates of the center of the figure on the screen

        Returns:
            None
            the stimulus is drawn on the surface

        """

# Draw the circles
        for i in range(n):
                angle = (2 * 3.1415 * i) / n
                x1 = x + int(distance * numpy.cos(angle))
                y1 = y + int(distance * numpy.sin(angle))

                #Make the specified circle invisible 
                if i == invisible:
                        col = GREY
                else: 
                        col = PINK

                pygame.draw.circle(surface, col, (x1, y1), radius, 0)


# Create the window
screen_width, screen_heigth = 600, 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_heigth), pygame.DOUBLEBUF)
pygame.display.set_caption('Lilac Chaser')
screen.fill(GREY)

# ------ MAIN PROGRAM LOOP (ANIMATION) -----
run = True
while run:
        # ----- EVENT HANDLER  
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                        run = False
        pygame.display.update()

        # ----- LOGIC
        invisible += 1
        # reset the invisible circle after a full rotation 
        if invisible == 11:
                invisible = 0
        
        #----- DRAWING
        # new white canvas for a new frame
        screen.fill(GREY)

        # draw the fixation point (cross)
        pygame.draw.line(screen, BLACK, (screen_width/2-5, screen_heigth/2), (screen_width/2+5, screen_heigth/2))
        pygame.draw.line(screen, BLACK, (screen_width/2, screen_heigth/2-5), (screen_width/2, screen_heigth/2+5))

        # call circles 
        Lilac_chaser(screen, 12, 150, 25, col, invisible, screen_width/2, screen_heigth/2)

        #Update screen
        pygame.display.flip()

        #Set frame rate (frames/second)
        clock.tick(10)

pygame.quit()