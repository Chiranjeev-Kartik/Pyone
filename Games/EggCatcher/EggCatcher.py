import pygame
import random
import time

"""
Author: Kartikay Chiranjeev Gupta
Last Date of Modification: 2/7/2021
"""

# Initialize pygame
pygame.init()

# Set window size
WIDTH = 1120
HEIGHT = 600

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title
pygame.display.set_caption("Egg Catcher")

# Load images
background = pygame.image.load('assets/background.png')
basket = pygame.image.load('assets/basket.png')
egg = pygame.image.load('assets/egg.png')

# Set the player position
player_pos = [WIDTH / 2, HEIGHT - 2 * 50]

# Set the egg properties
egg_pos = [random.randint(0, WIDTH - 50), 0]
egg_speed = 10

# Set the font
font = pygame.font.Font(None, 36)

# Set the score
score = 0

# Set the game over flag
game_over = False

# Game loop
SPEED = 0.05  # Lower for faster
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= 50
            if event.key == pygame.K_RIGHT:
                player_pos[0] += 50

    # Update the egg position
    egg_pos[1] += egg_speed

    # Check if the egg has reached the bottom of the screen
    if egg_pos[1] > HEIGHT:
        egg_pos[0] = random.randint(0, WIDTH - 50)
        egg_pos[1] = 0
        score -= 1

    # Check if the player has caught the egg
    if (egg_pos[0] < player_pos[0] + 50) and (egg_pos[0] + 50 > player_pos[0]):
        if (egg_pos[1] < player_pos[1] + 50) and (egg_pos[1] + 50 > player_pos[1]):
            egg_pos[0] = random.randint(0, WIDTH - 50)
            egg_pos[1] = 0
            score += 1

    screen.blit(background, (0, 0))
    # Draw the player
    screen.blit(basket, (player_pos[0], player_pos[1]))
    # pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], 50, 50))

    # Draw the egg
    screen.blit(egg, (egg_pos[0], egg_pos[1]))
    # pygame.draw.rect(screen, egg_color, (egg_pos[0], egg_pos[1], 50, 50))

    # Draw the score
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (WIDTH - 150, HEIGHT - 40))
    time.sleep(SPEED)
    # Update the display
    pygame.display.flip()
