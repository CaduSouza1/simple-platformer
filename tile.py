from typing import List, Tuple
import pygame
import csv
from spritesheet import SpriteSheet


class Tile(pygame.sprite.Sprite):
    def __init__(self, image: str, x: int, y: int, sprite_sheet: SpriteSheet):
        self.image = sprite_sheet.ParseSprite(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def Draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)


class Tilemap:
    def __init__(self, sprite_sheet: SpriteSheet, level_file: str, tile_size: int, tile_count: Tuple[int]):
        self.tile_size = tile_size
        self.tile_count = tile_count
        self.sprite_sheet = sprite_sheet
        self.game_map = self.Readcsv(level_file)
        self.tiles = [
            sprite_sheet.ParseSprite(r"dirt-with-rock.png"),
            sprite_sheet.ParseSprite(r"grass-with-rock.png"),
            sprite_sheet.ParseSprite(r"normal-dirt.png"),
            sprite_sheet.ParseSprite(r"normal-grass.png"),
        ]
        self.level = self.LoadMap()

    def DrawMap(self, surface: pygame.Surface):
        surface.blit(self.level, (0, 0))

    def LoadMap(self) -> pygame.Surface:
        map_surface = pygame.Surface(
            (self.tile_count[0] * self.tile_size, self.tile_count[1] * self.tile_size)
        )
        for x, row in enumerate(self.game_map):
            for y, tile_index in enumerate(row):
                index = int(tile_index)
                if index != -1:
                    map_surface.blit(
                        self.tiles[index], (x * self.tile_size, y * self.tile_size, 8,  8)
                    )

        return map_surface

    def Readcsv(self, level_file: str) -> List:
        game_map = []
        with open(level_file, "r") as level:
            for row in csv.reader(level):
                game_map.append(row)

        return game_map
