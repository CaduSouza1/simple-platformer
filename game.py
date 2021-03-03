import pygame
import ui.menu


class Game:
    def __init__(self):
        pygame.init()

        self.running = True
        self.playing = False
        self.display = pygame.Surface((1280, 720))
        self.font_path = "fonts\8_bit_arcade\8-bit Arcade In.ttf"

        self.window = pygame.display.set_mode(
            (self.display.get_width(), self.display.get_height())
        )

        self.keys = {
            # Keys to move in the main menu
            pygame.K_UP: False,
            pygame.K_DOWN: False,
            pygame.K_RETURN: False,
            pygame.K_ESCAPE: False
        }

        self.game_keys = {
            pygame.K_ESCAPE: lambda: self.start_menu.Run(self.display)
        }

        self.start_menu = ui.menu.StartMenu([
            ui.menu.Selector(
                text="Start",
                font_path=self.font_path,
                font_size=50,
                x=self.display.get_width() // 2,
                y=self.display.get_height() // 2,
                color=pygame.Color(255, 255, 255, 0)
            ),
            ui.menu.Selector(
                text="Options",
                font_path=self.font_path,
                font_size=50,
                x=self.display.get_width() // 2,
                y=self.display.get_height() // 2 + 60,
                color=pygame.Color(255, 255, 255, 0)
            ),
            ui.menu.Selector(
                text="Exit",
                font_path=self.font_path,
                font_size=50,
                x=self.display.get_width() // 2,
                y=self.display.get_height() // 2 + 120,
                color=pygame.Color(255, 255, 255, 0)
            )
        ])

    def CloseGame(self):
        self.running = False
        self.playing = False

    def Run(self):
        self.start_menu.Run(self.window)
        self.GameLoop()

    def GameLoop(self):
        while self.playing:
            self.Events()
            self.display.fill((0, 0, 0))
            self.Draw()
            self.window.blit(self.display, (0, 0))
            pygame.display.update()

    def Draw(self):
        self.DrawText("Game", 50, 100, 100)
        
    def DrawText(self, text: str, size: int, x: int, y: int):
        font = pygame.font.Font(self.font_path, size)
        font_surface = font.render(text, True, (255, 255, 255))
        self.display.blit(font_surface, (x, y))

    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.CloseGame()

            if event.type == pygame.KEYDOWN:
                if event.key in self.keys.keys():
                    self.keys[event.key]()
