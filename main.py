from typing import List

import pygame
from numpy import random

from Ship import Ship

DISPLAY_EXTENTS = (1024, 768)
FPS_CLOCK = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY_EXTENTS, pygame.DOUBLEBUF)

    pygame.display.set_caption('Oratorn')

    background = pygame.image.load('assets/images/background.png')
    background = pygame.transform.scale(background, DISPLAY_EXTENTS)

    ships: List[Ship] = []

    running = True
    while running:
        FPS_CLOCK.tick(10)

        # Set the background
        screen.blit(background, (0, 0))

        ship_spawning = random.normal(scale=1)
        spawn_chance = 1.8
        if ship_spawning > spawn_chance:
            ships.append(Ship(DISPLAY_EXTENTS))

        for ship in ships:
            # Set the ship image
            ship.ship_y_pos += ship.speed
            screen.blit(ship.ship_image, (ship.ship_x_pos, ship.ship_y_pos))

            # If the spaceship touches the bottom, you lose
            if ship.ship_y_pos > DISPLAY_EXTENTS[1] - ship.ship_y_size:
                running = False

        # Event handling
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_UP:
                    ships[0].speed += 1

                if event.key == pygame.K_DOWN:
                    ships[0].speed -= 1

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.flip()


if __name__ == '__main__':
    main()
