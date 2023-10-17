import pygame
import math

class Node:
    def __init__(self, node, layer):
        # Number in the network
        self.number = node
        # On Layer
        self.layer = layer
        # final output to pass on
        self.output = 0
        # all genes coming to this node
        self.in_genes = []
        # Sigmoid activation
        self.sigmoid = lambda x : 1 / (1 + math.exp(-x))

        # For Showing
        self.color = (255, 255, 255)
        self.bcolor = (0, 0, 0)

        self.radius = 5
        self.border_radius = 2
        self.pos = [0, 0]

        pass

    # Clone the node
    def clone(self):
        n = Node(self.number, self.layer)
        n.output = self.output
        n.pos = self.pos
        return n

    # Calculate output value
    def calculate(self):
        if self.layer == 0:
            print('No calculations for first layer')
            return

        s = 0
        for g in self.in_genes:
            if g.enabled:
                s += g.in_node.output * g.weight
        self.output = self.sigmoid(s)
        pass

    # Only for showing
    def show(self, ds):
        pygame.draw.circle(ds, self.bcolor, self.pos, self.radius + self.border_radius)
        pygame.draw.circle(ds, self.color, self.pos, self.radius)
        pass
