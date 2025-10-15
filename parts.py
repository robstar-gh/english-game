import pygame


class snap_slot():
    _snapables = {}

    def __init__(self, screen, left, top, width, height, color="aqua"):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
        self.rect = pygame.Rect(left, top, width, height)
        snap_slot._snapables[len(snap_slot._snapables) + 1] = self

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def snap(self, draggable):
        if draggable.colliderect(self.rect):
            draggable.x = self.rect.x + int(self.rect.width / 2) - int(draggable.width / 2)
            draggable.y = self.rect.y + int(self.rect.height / 2) - int(draggable.height / 2)


class draggable():
    def __init__(self, screen, left, top, width=160, height=110, color="aqua"):
        self.offset_y = None
        self.offset_x = None
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
        self.dragging = False
        self.rect = pygame.Rect(left, top, width, height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def drag(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.dragging = True
                mouse_x, mouse_y = event.pos
                self.offset_x = self.rect.x - mouse_x
                self.offset_y = self.rect.y - mouse_y


        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
            for snappable in snap_slot._snapables.values():
                snappable.snap(self.rect)

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y
