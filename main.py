import pygame

DISPLAY_EXTENTS = (1024, 768)
FPS_CLOCK = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY_EXTENTS, pygame.DOUBLEBUF)

    pygame.display.set_caption('Oratorn')

    while True:
        FPS_CLOCK.tick(10)

        # Event handling
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()


if __name__ == '__main__':
    main()
