import pygame

# Initialize PyGame
pygame.init()

# Create the screen using pygame.display.set_mode() function
screen = pygame.display.set_mode((1000, 800)) # (height pixels, width pixels) - function arguments

'''
Event in PyGame - any action or message that the operating system or the user generates, which Pygame can detect and respond to.
pygame.event.get() -  used to retrieve and remove event messages from the Pygame event queue.

When you retrieve events using pygame.event.get(), you get a list of pygame.event.Event objects. 
To figure out what action occurred, you access the .type attribute on each event object.

The .type attribute returns an integer value that corresponds to a specific type of event (e.g., key press, mouse click, window close)

pygame.QUIT - User clicked on window close button
'''
# Changing the title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Making the Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 128)) # Fill the game window with background color in RGB format
    pygame.display.update() # Updates the game window
