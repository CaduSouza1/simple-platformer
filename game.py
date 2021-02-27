import pygame
import pygame.constants as constants
import ui.menu


class Game:
    def __init__(self):
        pygame.init()

        self.running = True
        self.playing = False
        self.in_main_menu = True
        self.display = pygame.Surface((1280, 720))
        self.font_path = "fonts\8_bit_arcade\8-bit Arcade In.ttf"

        self.window = pygame.display.set_mode(
            (self.display.get_width(), self.display.get_height())
        )

        self.keys = {
            # Keys to move in the main menu
            constants.K_UP: False,
            constants.K_DOWN: False,
            constants.K_RETURN: False,
            constants.K_ESCAPE: False
        }

        self.game_keys = {
            constants.K_RETURN: lambda: self.StartMenu()
        }

        self.start_menu_keys = {
            constants.K_RETURN: lambda: self.CloseMenu(),
            constants.K_UP: lambda: self.start_menu.MoveCursor(ui.menu.StartMenu.UP),
            constants.K_DOWN: lambda: self.start_menu.MoveCursor(
                ui.menu.StartMenu.DOWN)
        }

        self.start_menu = ui.menu.StartMenu([
            ui.menu.SelectionBar(
                text="Start",
                font_path=self.font_path,
                font_size=50,
                x=self.display.get_width() // 2,
                y=self.display.get_height() // 2,
                color=pygame.Color(255, 255, 255, 0)
            ),
            ui.menu.SelectionBar(
                text="Options",
                font_path=self.font_path,
                font_size=50,
                x=self.display.get_width() // 2,
                y=self.display.get_height() // 2 + 60,
                color=pygame.Color(255, 255, 255, 0)
            )
        ])

    def CloseMenu(self):
        self.in_main_menu = False

    def CloseGame(self):
        self.in_main_menu = False
        self.running = False
        self.playing = False

    def Run(self):
        self.StartMenu()
        self.GameLoop()

    def GameLoop(self):
        while self.playing:
            self.Events()
            self.ParseGameEvents()
            self.DrawGame()
            self.ResetKeys()

    def StartMenu(self):
        while self.in_main_menu:
            self.Events()
            self.ParseMenuEvents()
            self.DrawMenu()
            self.ResetKeys()

    def DrawMenu(self):
        self.display.fill((0, 0, 0))

        self.start_menu.Draw(self.display)
        self.start_menu.DrawCursor(self.display)

        self.window.blit(self.display, (0, 0))
        pygame.display.update()

    def ParseGameEvents(self):
        for pressed_key in filter(lambda key: key == True, self.keys.keys()):
            if pressed_key in self.game_keys.keys():
                self.game_keys[pressed_key]()

    def ParseMenuEvents(self):
        for pressed_key in filter(lambda key: key == True, self.keys.keys()):
            if pressed_key in self.start_menu_keys.keys():
                self.start_menu_keys[pressed_key]()

    def ResetKeys(self):
        for key in self.keys.keys():
            self.keys[key] = False

    def DrawGame(self):
        self.display.fill((0, 0, 0))
        self.DrawText("Game", 50, 100, 100)
        self.window.blit(self.display, (0, 0))

        pygame.display.update()

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
                    self.keys[event.key] = True

        if self.keys[constants.K_RETURN]:
            self.in_main_menu = False
