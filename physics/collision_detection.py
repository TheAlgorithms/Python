"""
Title : AABB Collision Detection and Counter

Description : This program simulates two moving boxes that bounce back when they
collide with each other or with the edges of the screen. A collision counter
increments each time the boxes collide, except when they touch the edges of the
screen, where they rebound without increasing the counter. The motion and
collision logic demonstrate axis-aligned bounding box (AABB) collision detection.

The program is implemented using Pygame and features:
- Two boxes moving towards each other
- Collision detection between the boxes
- Edge collision handling (without counter increment)
- A visual counter displaying the number of collisions

Source :
- https://en.wikipedia.org/wiki/Bounding_volume
- https://www.pygame.org/docs/
"""

import pygame

# Initialize Pygame
pygame.init()

# Constants for screen dimensions and box properties
WIDTH, HEIGHT = 500, 300  # Screen width and height
BOX_SIZE = 50  # Size of each box
SPEED = 3  # Speed of movement

# Colors
WHITE = (255, 255, 255)  # Background color
RED = (255, 0, 0)  # Box 1 color
BLUE = (0, 0, 255)  # Box 2 color

# Create display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AABB Collision Detection")

# Initial positions of the boxes
box1_x, box1_y = 50, HEIGHT // 2 - BOX_SIZE // 2
box2_x, box2_y = WIDTH - 100, HEIGHT // 2 - BOX_SIZE // 2

# Movement directions
box1_dir = SPEED
box2_dir = -SPEED

# Collision counter
collision_count = 0

# Main game loop
running = True
while running:
    pygame.time.delay(20)  # Controls the frame rate
    screen.fill(WHITE)  # Clear screen before drawing

    # Move the boxes
    box1_x += box1_dir
    box2_x += box2_dir

    # Collision detection between the two boxes
    if box1_x + BOX_SIZE > box2_x:
        # Only increase the counter if they overlap beyond just touching edges
        if box1_x + BOX_SIZE > box2_x + 1 or box2_x > box1_x + 1:
            collision_count += 1
        box1_dir *= -1  # Reverse direction
        box2_dir *= -1  # Reverse direction

    # Edge collision detection (bouncing without increasing counter)
    if box1_x <= 0 or box1_x + BOX_SIZE >= WIDTH:
        box1_dir *= -1
    if box2_x <= 0 or box2_x + BOX_SIZE >= WIDTH:
        box2_dir *= -1

    # Draw the boxes
    pygame.draw.rect(screen, RED, (box1_x, box1_y, BOX_SIZE, BOX_SIZE))
    pygame.draw.rect(screen, BLUE, (box2_x, box2_y, BOX_SIZE, BOX_SIZE))

    # Display the collision count
    font = pygame.font.Font(None, 36)
    text = font.render("Collisions: " + str(collision_count), True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Number of collisions occurred are", collision_count)
    pygame.display.update()
# Quit Pygame
pygame.quit()
