import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, use_image=True):
        super().__init__(groups)

        if use_image:
            # Load the image and convert it to a Surface
            self.image = pygame.image.load('C:/Users/kevin/OneDrive/Desktop/pygame_app/tree.png').convert_alpha()
            # Ensure the image is scaled to TILESIZE
            self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        else:
            # Create a solid color Surface
            self.image = pygame.Surface((TILESIZE, TILESIZE))
            self.image.fill((0, 255, 0))  # Example color (green)

        # Create the rect attribute
        self.rect = self.image.get_rect(topleft=pos)

        self.hitbox = self.rect.inflate(-5,-20)

