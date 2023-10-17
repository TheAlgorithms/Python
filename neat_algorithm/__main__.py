## This file is just a sample visualizer for the neat algorithm
## population and species is not implemented here.
## You can also check out a version of this used to play Flappy bird
## Link for FlappyNEAT: https://github.com/kshitijaucharmal/FlappyNEAT

import pygame
from sys import exit

# NEAT Files
from genome import Genome
from geneh import GeneHistory

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
N_INPUTS = 10
N_OUTPUTS = 5

pygame.init()
clock = pygame.time.Clock()
# Set Font
font = pygame.font.SysFont('Segoe', 26)

# Window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Display for neural network
nn = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA, 32)
nn = nn.convert_alpha()

def quit_game():
    # Exit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# Setup
gh = GeneHistory(N_INPUTS, N_OUTPUTS)
g = Genome(gh)

# Game Main Method
def main():
    run = True
    while run:
        # Quit Event Check
        quit_game()

        # Draw neural Network
        g.show(nn)

        # Mutate every frame
        g.mutate()

        # Show neural network
        window.blit(nn, (0, 0))

        # Update with 60 FPS and update
        clock.tick(60)
        pygame.display.update()

# Run only if this file is executed
if __name__ == "__main__":
    main()
