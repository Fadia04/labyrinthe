import os
import pygame.image
from config import IMG_PATH

#pylint: disable=R0903
class Character: 
    #Define parameters for character
    def __init__(self, y_pos, x_pos, img, mapping):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.root = os.path.dirname(os.path.dirname(__file__))
        self.img = os.path.join(self.root, IMG_PATH, img)
        self.pygame_img = pygame.image.load(self.img)
        self.set_onmap(mapping)

    def set_onmap(self, mapping):
        mapping.set_macgyver(self.y_pos, self.x_pos)
