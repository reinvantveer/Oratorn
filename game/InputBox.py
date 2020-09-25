import pygame


COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')


class InputBox:

    def __init__(self, display_extents):
        self.rect = pygame.Rect(40, 200, 200, 50)
        self.color = COLOR_INACTIVE
        self.text = ''  # Init as empty string
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_surface = self.font.render(self.text, True, self.color)
        self.active = False

    def render(self, screen) -> None:
        self.text_surface = self.font.render(self.text, True, self.color)
        screen.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
