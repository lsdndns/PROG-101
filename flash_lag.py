""" Flag Lag Illusion  """

import pygame 

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the window
screen_width, screen_heigth = 500, 500
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_heigth), pygame.DOUBLEBUF)
pygame.display.set_caption('Flag Line Illusion')

#Create clock object
clock = pygame.time.Clock()

# Variables 
# Dimension of the rectangle 
rect_width = 50
rect_heigth = 50

#Position of the rectangle 
rect_x = 0
rect_y = screen_heigth/2 - rect_heigth

# Position of the second rectangle 
rect2_x = screen_width/2 - rect_width/2
rect2_y = screen_heigth/2 + rect_heigth

#Vector, direction and speed of the rectangle 
rect_change_x=2
rect_change_y=0

# ------ Main program loop (Animation) -----
run = True
while run:
        # ----- Event handler 
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                        run = False
        pygame.display.update()

        # ----- GAME LOGIC
        rect_x += rect_change_x
        rect_y += rect_change_y

        if rect_x < 0 or  rect_x > screen_width - rect_width  :
                rect_change_x *= -1

        #----- GAME DRAWING 
        #new white canvas for a new frame
        screen.fill(WHITE)

        #Draw the rectangle 
        pygame.draw.rect(screen, BLACK, (rect_x, rect_y, rect_heigth, rect_heigth))

        # Draw the second rectangle 
        if screen_width/2 - rect_width/2 < rect_x < screen_width/2 + rect_width/2 :
                pygame.draw.rect(screen, BLACK, (rect2_x, rect2_y, rect_heigth, rect_heigth))

        #Update screen
        pygame.display.flip()

        #Set frame rate (frames/second)
        clock.tick(200)

pygame.quit()