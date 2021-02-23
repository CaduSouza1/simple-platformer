from typing import List
import pygame

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4


class Button:
    pass


class Menu:
    def __init__(self, text: str, font_path: str, font_size: int, x: int, y: int, color: pygame.Color):
        self.text = text
        self.font = pygame.font.Font(font_path, font_size)
        self.font_width, self.font_height = self.font.size(text)
        self.selected = True
        self.color = color
        self.x = x
        self.y = y

    def Draw(self, surface: pygame.Surface):
        font_rect = pygame.Rect(0, 0, self.font_width, self.font_height)
        font_rect.center = (self.x, self.y)

        font_surface = self.font.render(
            self.text,
            True,
            self.color
        )

        surface.blit(font_surface, (font_rect.x, font_rect.y))

    def DrawCursor(self):
        pass


class SelectionBar(Menu):
    def __init__(self, text: str, font_path: str, font_size: int, x: int, y: int, color: pygame.Color):
        super().__init__(text, font_path, font_size, x, y, color)

    def DrawCursor(self):
        pass


class StartMenu:
    def __init__(self, menu_itens: List[Menu], shape: tuple, centered=False):
        self.menu_itens = menu_itens
        self.shape = shape
        self.centered = centered

    def Draw(self, surface: pygame.Surface):
        for menu in self.menu_itens:
            menu.Draw(surface)

    def DrawCursor(self):
        pass

    def MoveCursor(self, direction: int):
        pass
