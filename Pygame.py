import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 20
BALL_SPEED = 5
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Game")

# Initialize the ball position and velocity
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_velocity_x = random.choice([-1, 1]) * BALL_SPEED
ball_velocity_y = random.choice([-1, 1]) * BALL_SPEED

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Boundary collision detection
    if ball_x - BALL_RADIUS < 0 or ball_x + BALL_RADIUS > SCREEN_WIDTH:
        ball_velocity_x = -ball_velocity_x
    if ball_y - BALL_RADIUS < 0 or ball_y + BALL_RADIUS > SCREEN_HEIGHT:
        ball_velocity_y = -ball_velocity_y

    # Clear the screen
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Control game speed
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
