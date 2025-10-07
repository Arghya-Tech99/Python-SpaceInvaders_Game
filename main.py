import pygame

# Initialize PyGame
pygame.init()

# Create the screen using pygame.display.set_mode() function
screen = pygame.display.set_mode((800, 600)) # (width pixels, height pixels) - function arguments

'''
Event in PyGame - any action or message that the operating system or the user generates, which Pygame can detect and respond to.
Events are generally keyboard inputs or mouse clicks, in the context of game development.
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

# Player initial details
playerIcon = pygame.image.load('Player.png')
playerX = 380
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x, y): # Function which draws the icon at the initial position defined on the game window
    screen.blit(playerIcon, (x, y))


# Making the Game Loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fill the game window with background color in RGB format
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Checks whether a keystroke is made or not, and if made then is it right or left
        if event.type == pygame.KEYDOWN:
            print('Keystroke detected')
            if event.key == pygame.K_LEFT:
                print('LEFT')
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                print('RIGHT')
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            print('Keystroke released')
            playerX_change = 0
           


    '''
    pygame.KEYDOWN - Function which checks whether a key is pressed.
    pygame.KEYUP - Function which checks whether a key is released.
    '''

    # Update the values of playerX and playerY
    playerX += playerX_change

    # Changing the X and Y coordinates of the player, and drawing it repeatedly on the screen by calling the function
    player(playerX, playerY)

    pygame.display.update() # Updates the game window
