import pygame
import sys
from parts import snap_slot

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

rect = pygame.Rect(300, 200, 150, 100)
snap_rect = snap_slot(screen, 295, 450, 160, 110)
dragging = False




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(pygame.mouse.get_pos()):
                dragging = True
                mouse_x, mouse_y = event.pos
                offset_x = rect.x - mouse_x
                offset_y = rect.y - mouse_y


        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            snap_rect.snap(rect)

        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x, mouse_y = event.pos
                rect.x = mouse_x + offset_x
                rect.y = mouse_y + offset_y
        mouse_x, mouse_y = pygame.mouse.get_pos()
        print(f"{mouse_x}, {mouse_y}")

    screen.fill("white")


    pygame.draw.rect(screen, "aqua", snap_rect)
    pygame.draw.rect(screen, "blue", rect)




    # Renders the game
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()


if __name__ == '__main__':
    pass