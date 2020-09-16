from random import randint

import pygame


class Ship:
    def __init__(self, display_extents) -> None:
        self.ship_image = pygame.image.load('assets/images/normal_ship.png')
        self.ship_x_size, self.ship_y_size = self.ship_image.get_rect().size
        required_x_size = 100
        resize_ratio = required_x_size / self.ship_x_size
        new_x_size = int(self.ship_x_size * resize_ratio)
        new_y_size = int(self.ship_y_size * resize_ratio)
        self.ship_image = pygame.transform.scale(self.ship_image, (new_x_size, new_y_size))
        self.ship_x_size, self.ship_y_size = self.ship_image.get_rect().size
        self.ship_x_pos = randint(0, display_extents[0] - self.ship_x_size)
        self.ship_y_pos = 0
        self.speed = 5

        # set a taks to solve by the user
        self.task = '1 + 1'
        self.solution = '2'
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def render(self, screen) -> None:
        screen.blit(self.ship_image, (self.ship_x_pos, self.ship_y_pos))
        task_surface = self.font.render(self.task, False, (0, 0, 0))

        bottom = self.ship_y_pos + self.ship_y_size
        screen.blit(task_surface, (self.ship_x_pos, bottom))

