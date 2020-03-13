import pygame as pg


class Settings:

    def __init__(self):
        # frames per second
        self.FPS = 60

        # colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.ORANGE = (251, 191, 72)
        self.PINK = (255, 108, 216)
        self.RED = (234, 17, 17)
        self.CYAN = (67, 204, 249)
        self.ELECTRIC_BLUE = (41, 69, 255)
        self.FRUIT_PINK = (255, 48, 76)

        # fonts
        self.pac_man_font = pg.font.SysFont(None, 48)
        self.ghost_font = pg.font.SysFont(None, 20)
        self.game_font = pg.font.SysFont(None, 24)

        # window size
        self.GAME_WIDTH = 610
        self.GAME_HEIGHT = 670

        # buffer space to display the score information
        self.BUFFER = 50

        # the maze lies within the window, so must be smaller than window
        self.MAZE_WIDTH = self.GAME_WIDTH-self.BUFFER
        self.MAZE_HEIGHT = self.GAME_HEIGHT-self.BUFFER

        # size of each brick that comprises the walls
        self.BRICK_SIZE = 5

        # numbers of rows and columns in the maze
        self.MAZE_ROWS = 30
        self.MAZE_COLUMNS = 28

        # width of each cell in the game
        self.CELL_WIDTH = self.MAZE_WIDTH // self.MAZE_COLUMNS
        self.CELL_HEIGHT = self.MAZE_HEIGHT // self.MAZE_ROWS

        # player settings
        self.player_starting_position_x = 0
        self.player_starting_position_y = 0

        # speed of pacman
        self.pacman_speed = 3

    def set_pacman_spawn(self, x, y):
        self.player_starting_position_x = x
        self.player_starting_position_y = y
