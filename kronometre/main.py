import pygame
from pygame import event

ICON=pygame.image.load('kronometre.png')
WIDTH=400
HEIGHT=400

def main():
    pygame.init()
    pygame.display.set_caption('Kronometre')
    pygame.display.set_icon(ICON)
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    screen.fill(pygame.Color("blue"))

    running=True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running=False
            if running==False:
                pygame.quit()
            elif e.type==pygame.MOUSEBUTTONDOWN:
                location=pygame.mouse.get_pos()#x,y mouse location

if __name__=="__main__":
    main()