from random import randint

import pygame

DISPLAY_EXTENTS = (1024, 768)
FPS_CLOCK = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY_EXTENTS, pygame.DOUBLEBUF)

    pygame.display.set_caption('Oratorn')

    background = pygame.image.load('assets/images/background.png')
    background = pygame.transform.scale(background, DISPLAY_EXTENTS)

    ship_image = pygame.image.load('assets/images/Python_logo-large.png')
    ship_image_x_size = ship_image.get_rect().size[0]
    ship_x_pos = randint(0, DISPLAY_EXTENTS[0] - ship_image_x_size)
    ship_y_pos = 0
    speed = 1

    while True:
        FPS_CLOCK.tick(10)

        # Set the background
        screen.blit(background, (0, 0))

        # Set the ship image
        ship_y_pos += speed
        screen.blit(ship_image, (ship_x_pos, ship_y_pos))

        # Event handling
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_UP:
                    speed += 1

                if event.key == pygame.K_DOWN:
                    speed -= 1

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.flip()


if __name__ == '__main__':
    main()
