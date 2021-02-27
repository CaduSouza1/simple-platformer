from typing import List
import pygame


class Button:
    pass


class MenuItem:
    def __init__(self, text: str, font_path: str, font_size: int, x: int, y: int, color: pygame.Color):
        self.text = text
        self.color = color
        self.font = pygame.font.Font(font_path, font_size)
        self.width, self.height = self.font.size(text)
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def Draw(self, surface: pygame.Surface):
        font_surface = self.font.render(
            self.text,
            True,
            self.color
        )

        surface.blit(font_surface, (self.rect.x, self.rect.y))

    def ShowOptions(self, surface: pygame.Surface):
        pass

    def DrawCursor(self):
        pass


class SelectionBar(MenuItem):
    cursor_width = 5
    cursor_height = 5
    def __init__(self, text: str, font_path: str, font_size: int, x: int, y: int, color: pygame.Color):
        super().__init__(text, font_path, font_size, x, y, color)

    def DrawCursor(self, surface: pygame.Surface):
        cursor_rect = pygame.Rect(
            self.rect.x, self.rect.y, self.width + SelectionBar.cursor_width, self.height + SelectionBar.cursor_height
        )
        pygame.draw.rect(surface, self.color, cursor_rect, 1)


class StartMenu:
    UP = 1
    DOWN = 2

    def __init__(self, menu_itens: List[MenuItem]):
        self.menu_itens = menu_itens
        self.selected_item_index = 0

    def Draw(self, surface: pygame.Surface):
        for menu in self.menu_itens:
            menu.Draw(surface)

    def DrawCursor(self, surface: pygame.Surface):
        self.menu_itens[self.selected_item_index].DrawCursor(surface)

    def CenterMenu(self, center_x: int, center_y: int):
        pass

    def MoveCursor(self, direction: int):
        if direction == StartMenu.UP:
            if self.selected_item_index > 0:
                self.selected_item_index -= 1

        elif direction == StartMenu.DOWN:
            if self.selected_item_index < len(self.menu_itens):
                self.selected_item_index += 1
