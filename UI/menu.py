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


class Selector(MenuItem):
    cursor_width = 5
    cursor_height = 5
    def __init__(self, text: str, font_path: str, font_size: int, x: int, y: int, color: pygame.Color):
        super().__init__(text, font_path, font_size, x, y, color)

    def DrawCursor(self, surface: pygame.Surface):
        cursor_rect = pygame.Rect(
            self.rect.x, self.rect.y, self.width + Selector.cursor_width, self.height + Selector.cursor_height
        )
        pygame.draw.rect(surface, self.color, cursor_rect, 1)


class StartMenu:
    UP = 1
    DOWN = 2

    def __init__(self, menu_itens: List[MenuItem]):
        self.menu_itens = menu_itens
        self.selected_item_index = 0
        self.should_close = False
        self.keys = {
            pygame.K_ESCAPE: lambda: self.Close(),
            pygame.K_w: lambda: self.MoveCursor(StartMenu.UP),
            pygame.K_s: lambda: self.MoveCursor(StartMenu.DOWN)
        }

    def Close(self):
        self.should_close = True

    def OpenMenu(self, surface: pygame.Surface):
        self.should_close = False
        self.Run(surface)

    def Draw(self, surface: pygame.Surface):
        for menu in self.menu_itens:
            menu.Draw(surface)

    def DrawCursor(self, surface: pygame.Surface):
        self.menu_itens[self.selected_item_index].DrawCursor(surface)

    def CenterMenu(self, center_x: int, center_y: int):
        pass

    def MoveCursor(self, direction: int):
        if direction == StartMenu.UP:
            # if self.selected_item_index > 0:
            #     self.selected_item_index *= -1
            self.selected_item_index = (self.selected_item_index - 1) % len(self.menu_itens)
        
        elif direction == StartMenu.DOWN:
            self.selected_item_index = (self.selected_item_index + 1) % len(self.menu_itens)


    def Run(self, surface: pygame.Surface):
        while not self.should_close:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in self.keys.keys():
                        self.keys[event.key]()
            
            surface.fill((0, 0, 0))
            self.Draw(surface)
            self.DrawCursor(surface)
            pygame.display.update()
