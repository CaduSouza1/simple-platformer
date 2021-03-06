import pygame
import json


class SpriteSheet:
    def __init__(self, file_path: str):
        self.sprite_sheet = pygame.image.load(file_path).convert()
        with open(file_path.replace(".png", ".json"), "r") as metadata:
            self.data = json.load(metadata)

    def GetSprite(self, x: int, y: int, width: int, height: int) -> pygame.Surface:
        sprite_surface = pygame.Surface((width, height))
        sprite_surface.set_colorkey((0, 0, 0))
        sprite_surface.blit(self.sprite_sheet, (0, 0, width, height))

        return sprite_surface

    def ParseSprite(self, sprite_name: str) -> pygame.Surface:
        sprite_data = self.data["frames"][sprite_name]["frame"]
        return self.GetSprite(sprite_data["x"], sprite_data["y"], sprite_data["w"], sprite_data["h"])
