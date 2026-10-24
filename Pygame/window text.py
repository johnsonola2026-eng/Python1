import pygame
pygame.init()
screen=pygame.display.set_mode((500, 500))
window=pygame.display.set_caption("my first game screen")
background_colour=(0, 0, 0)
BLUE=(0,70,0)
pygame.draw.Rect(BLUE,window,(500,500,),10,10)
screen.fill(background_colour)
pygame.display.update
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()