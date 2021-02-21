import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__()


class Tilemap:
    def __init__(self, filename: str):
        self.filename = filename
