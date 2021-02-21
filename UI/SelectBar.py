import pygame


class SelectionBar:
    def __init__(self, text, font_path, font_size, x, y, color, selected_color):
        self.text = text
        self.font = pygame.font.Font(font_path, font_size)
        self.position = (x, y)
        self.selected = False
        self.color = color
        self.selected_color = selected_color
    
    def Draw(self, surface):
        font_rect = pygame.Rect(
            self.x, 
            self.y, 
            self.font.get_width(), 
            self.font.get_height()
        )

        if self.selected:
            font_surface = self.font.render(
                self.text,
                True,
                self.selected_color
            )

            surface.blit(font_surface, self.position)
            pygame.draw.rect(surface, self.selected_color, font_rect)

        else:           
            font_surface = self.font.render(
                self.text,
                True,
                self.selected_color
            )

            surface.blit(font_surface, self.position)
            pygame.draw.rect(surface, self.color, font_rect)
