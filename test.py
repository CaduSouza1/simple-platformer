import pygame
from tile import Tilemap
from spritesheet import SpriteSheet

screen = pygame.display.set_mode((1280, 720))
tilemap = Tilemap(
    SpriteSheet("assets\ground\ground-sheet.png"), 
    "levels\level1.csv",  
    8, (160, 90)
)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    tilemap.DrawMap(screen)
    pygame.display.update()
