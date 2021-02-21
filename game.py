import pygame
import pygame.constants as constants
import UI.SelectBar


class Game:
    def __init__(self):
        pygame.init()

        self.font_path = "fonts\8_bit_arcade\8-bit Arcade In.ttf"
        self.running, self.playing = True, False
        self.display = pygame.Surface((1280, 720))

        self.window = pygame.display.set_mode(
            (self.display.get_width(), self.display.get_height())
        )

        self.keys = {
            # Keys to move in the main menu
            constants.K_UP: False,
            constants.K_DOWN: False,
            constants.K_RETURN: False
        }

        self.menu_select_bars = [
            UI.SelectBar(
                "Start",
                self.font_path,
                20,
                self.display.get_width() // 2,
                self.display.get_height() // 2,
                pygame.Color(255, 255, 255, 0),
                pygame.Color(0, 0, 255, 0)
            )
        ]

    def GameLoop(self):
        while self.playing:
            self.Events()
            # self.DrawText(
            #     text="Hello",
            #     size=20,
            #     x=self.display.get_width() // 2,
            #     y=self.display.get_height() // 2
            # )

            self.Draw()

    def Draw(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.display, (0, 0))
        pygame.display.update()

    def DrawText(self, text: str, size: int, x: int, y: int):
        font = pygame.font.Font(self.font_path, size)
        font_surface = font.render(text, True, (255, 255, 255))
        self.display.blit(font_surface, (x, y))

    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key in self.keys.keys():
                    self.keys[event.key] = True
