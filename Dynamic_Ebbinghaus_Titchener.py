""" Dynamic Ebbinghaus Titchener
Static circle in the middle surrounded by six circles whose diameter increase and decrease over time  """

import pygame 
import numpy as np

# ----- VARIABLES 
# Create clock object
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Circles
radius_center = 25
radius_surround = 25
delta_radius = -1

# ----- FUNCTION
def Ebbinghaus(surface, n_surround, distance, radius_1, radius_2, col_1, col_2, x, y):
        """ Draws a circle surrounded by outer ones.

        Arguments:
            surface: pygame surface to display the stimulus on
            n_surround: number of surrounding circles
            distance: distance between the center of inner circle and surrounding ones
            radius_1: radius of inner circle
            radius_2: radius of outer circles
            col_1: color of the inner circle
            col_2: color of the outer circles
            x, y: coordinates of the center of the figure on the screen

        Returns:
            None
            the stimulus is drawn on the surface

        """

# Draw the inner circle
        pygame.draw.circle(surface, col_1, (int(x), int(y)), radius_1, 0)

# Draw the surrounding circles
        for i in range(n_surround):
                angle = (2 * np.pi * i) / n_surround
                x1 = x + int(distance * np.cos(angle))
                y1 = y + int(distance * np.sin(angle))
                pygame.draw.circle(surface, col_2, (int(x1), int(y1)), radius_2, 0)


# Create the window
screen_width, screen_heigth = 600, 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_heigth), pygame.DOUBLEBUF)
pygame.display.set_caption('Dynamic Ebbinghaus Titchener')
screen.fill(WHITE)

# ------ MAIN PROGRAM LOOP (ANIMATION) -----
run = True
while run:
        # ----- EVENT HANDLER  
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                        run = False

        # ----- LOGIC
        radius_surround += delta_radius
        if radius_surround < 25 or radius_surround > 50:
                delta_radius *= -1
        
        #----- DRAWING 
        #new white canvas for a new frame
        screen.fill(WHITE)
        Ebbinghaus(screen, 6, 100, radius_center, radius_surround, BLACK, BLACK, screen_width/2, screen_heigth/2)

        #Update screen
        pygame.display.flip()

        #Set frame rate (frames/second)
        clock.tick(20)

pygame.quit()