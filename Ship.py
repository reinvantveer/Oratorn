from random import randint

import pygame


class Ship:
    def __init__(self, display_extents) -> None:
        self.ship_image = pygame.image.load('assets/images/normal_ship.png')
        self.ship_image_x_size, self.ship_y_size = self.ship_image.get_rect().size
        self.ship_x_pos = randint(0, display_extents[0] - self.ship_image_x_size)
        self.ship_y_pos = 0
        self.speed = 5
