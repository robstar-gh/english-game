import pygame
from parts import snap_slot, draggable

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

rect = draggable(screen, 300, 200, 150, 100, "blue")
snap_rect1 = snap_slot(screen, 295, 450, 160, 110)
snap_rect2 = snap_slot(screen, 100, 450, 160, 110)
dragging = False




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        rect.drag(event)

    screen.fill("white")

    snap_rect1.draw()
    snap_rect2.draw()
    rect.draw()

    # Renders the game
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()


if __name__ == '__main__':
    pass