import pygame
import random
import math

# Initialize PyGame
pygame.init()

# Import mixer for playing sounds
from pygame import mixer
clock = pygame.time.Clock()

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

# Playing the background music
mixer.music.load('background.wav')
mixer.music.play()
# Player initial details
playerIcon = pygame.image.load('Player.png')
playerX = 380
playerY = 480
playerX_change = 0
playerY_change = 0
score = 0

def player(x, y): # Function which draws the icon at the initial position defined on the game window
    screen.blit(playerIcon, (x, y))

# Enemy Initial details
# Multiple enemies are created, whose individual details are stored as list
enemyIcon = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyIcon.append(pygame.image.load('Enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(48, 300))
    enemyX_change.append(0.3)
    enemyY_change.append(30)


def enemy(x, y): # Function which draws the icon at the initial position defined on the game window
    screen.blit(enemyIcon[i], (x, y))

# Bullet details
bulletIcon = pygame.image.load('bullet.png')
bulletX = 0 # Always shoot from ship nose
bulletY = 480 # Always shoot from same Y-level as the ship
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state # bullet_state is now global, which means its value can be altered from anywhere
    bullet_state = "fire"
    screen.blit(bulletIcon, (x+16, y+10))

# Creating a Score record system
score_value = 0
font = pygame.font.Font('Retro Gaming.ttf', 36)
# Create a new font object named 'font' from a font file or from a system font, then use it to render text onto a Pygame Surface.

textX = 15
textY = 15
def showScore(x, y):    # Displays the score of the player on game screen
    score = font.render("Score : " + str(score_value),  True, (255, 255, 255))
    # font.render() Renders text from the created font object onto the surface
    screen.blit(score, (x, y))

# Creating the Game over screen
over_font = pygame.font.Font('game_over.ttf', 90)
def GameOver():
    over_text = over_font.render("GAME OVER",  True, (255, 255, 255))
    screen.blit(over_text, (300, 250))

# Creating a function for collision detection
def inCollision(enemyX, enemyY, bulletX, bulletY):
    sum_sq_diffs = (enemyX-bulletX)**2 + (enemyY-bulletY)**2
    distance = math.sqrt(sum_sq_diffs)
    if distance < 30:
        return True
    else:
        return False

# Defining the background image
background = pygame.image.load('Bg3.png')

# Making the Game Loop
running = True
while running:
    # screen.fill((0, 0, 0))  # Fill the game window with background color in RGB format
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Checks whether a keystroke is made or not, and if made then is it right or left
        if event.type == pygame.KEYDOWN:
            #print('Keystroke detected')
            if event.key == pygame.K_LEFT:
                #print('LEFT')
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                #print('RIGHT')
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                #print('Shots fired!')
                bullet = mixer.Sound('bulletShot.wav')
                mixer.Sound.play(bullet)
                if bullet_state is "ready":
                    bulletX = playerX # Get the current X coordinate of the spaceship
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            #print('Keystroke released')
            playerX_change = 0



    '''
    pygame.KEYDOWN - Function which checks whether a key is pressed.
    pygame.KEYUP - Function which checks whether a key is released.
    '''

    # Update the values of playerX and playerY
    playerX += playerX_change

    # Adding boundaries so that player doesn't go out of window
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: # 800 - 64 (64 is size of Player PNG)
        playerX = 736

    # For each of the enemies, add functionality of movement updation and collision detection
    for i in range(num_of_enemies):
        # Game over screen display
        if enemyY[i] > 440:
            over_sound = mixer.Sound('GameOver.wav')
            mixer.Sound.play(over_sound)
            for j in range(num_of_enemies):
                enemyY[j] = 1500
            GameOver()
            break

        # Update the enemy position values
        enemyX[i] += enemyX_change[i]
        # Adding enemy movement
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i]>= 736:  # 800 - 64 (64 is size of Player PNG)
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Checking for collision and updating
        collision = inCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:  # If the collision happens, i.e. the collision value is 'True'
            explode = mixer.Sound('enemyKill.wav')
            mixer.Sound.play(explode)
            bullet_state = "ready"
            bulletY = 480
            score_value += 1
            # After hitting, the enemy has to respawn
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(48, 300)

    # Bullet movements
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY = bulletY - bulletY_change

    # Shooting multiple bullets
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    # Changing the X and Y coordinates of the player and enemy, and drawing it repeatedly on the screen by calling the function
    player(playerX, playerY)
    for i in range(num_of_enemies):
        enemy(enemyX[i], enemyY[i])

    # Display score on screen
    showScore(textX, textY)

    pygame.display.update() # Updates the game window
