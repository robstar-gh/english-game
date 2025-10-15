import pygame


class snap_slot():
    def __init__(self, screen, left, top, width, height, color="aqua"):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
        self.rect = pygame.Rect(left, top, width, height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def snap(self, draggable):
        if draggable.colliderect(self.rect):
            draggable.x = self.rect.x + int(self.rect.width / 2) - int(draggable.width / 2)
            draggable.y = self.rect.y + int(self.rect.height / 2) - int(draggable.height / 2)

