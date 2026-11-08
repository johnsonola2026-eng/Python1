import pygame
import random

pygame.init()
window = pygame.display.set_mode((250, 250))
pygame.display.set_caption("Sprite Color Event")

background_color = (250, 250, 250)
colors = [(173, 216, 230), (0, 0, 139), (255, 0, 0), (0, 180, 0)]
rectangle_color = colors[0]
circle_color = colors[1]
rectangle = pygame.Rect(25, 25, 80, 80)
circle_center = (165, 165)
circle_radius = 40
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rectangle.collidepoint(event.pos):
                rectangle_color = random.choice(colors)

            dx = event.pos[0] - circle_center[0]
            dy = event.pos[1] - circle_center[1]
            if dx * dx + dy * dy <= circle_radius * circle_radius:
                circle_color = random.choice(colors)

    window.fill(background_color)
    pygame.draw.rect(window, rectangle_color, rectangle)
    pygame.draw.circle(window, circle_color, circle_center, circle_radius)
    pygame.display.flip()

pygame.quit()