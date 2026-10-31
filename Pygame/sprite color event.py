import pygame
pygame.init
window=pygame.display.set_mode((250,250))
window.fill((250,250,250))
LIGHTBLUE=(25,75,25)
DARKBLUE=(0,255,0)
global gb_color1
global gb_color2
gb_color1=LIGHTBLUE
gb_color2=DARKBLUE
pygame.draw.Rect(window,gb_color1,(700,700))
pygame.draw.circle(window,gb_color2,(700,700))
pygame.display.update()