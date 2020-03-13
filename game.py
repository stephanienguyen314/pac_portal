from starting import *
from buttons import Buttons
from player import Player
from ghosts import Ghosts
import functions as fun
from settings import Settings


class Game:

    def __init__(self):

        # create settings
        self.settings = Settings()

        # create screen of game
        self.screen = pg.display.set_mode((self.settings.GAME_WIDTH, self.settings.GAME_HEIGHT))

        # set caption of game
        pg.display.set_caption("Pac Man!")

        # draws the initial background of title card
        self.screen.fill(self.settings.BLACK)

        # determines if user clicked to close the game window
        self.finished: bool = False

        self.clock = pg.time.Clock()

        # game always starts at this stage; if user clicks button to start, this will change to 'playing'
        self.state = 'start'

        # all starting objects for the start screen
        self.starting_pinky = StartingPinky(location_x=125, location_y=300)
        self.starting_screen_pinky_group = pg.sprite.Group(self.starting_pinky)

        self.intro_starting_pinky = IntroPinkGhost(location_x=(self.settings.GAME_WIDTH / 2) - 300, location_y=100)
        self.intro_starting_pinky_group = pg.sprite.Group(self.intro_starting_pinky)

        self.starting_blinky = StartingBlinky(location_x=85, location_y=300)
        self.starting_screen_blinky_group = pg.sprite.Group(self.starting_blinky)

        self.intro_starting_blinky = IntroRedGhost(location_x=(self.settings.GAME_WIDTH / 2) - 300, location_y=200)
        self.intro_starting_blinky_group = pg.sprite.Group(self.intro_starting_blinky)

        self.starting_clyde = StartingClyde(location_x=5, location_y=300)
        self.starting_screen_clyde_group = pg.sprite.Group(self.starting_clyde)

        self.intro_starting_clyde = IntroOrangeGhost(location_x=(self.settings.GAME_WIDTH / 2) + 100, location_y=100)
        self.intro_starting_clyde_group = pg.sprite.Group(self.intro_starting_clyde)

        self.starting_inkey = StartingInkey(location_x=45, location_y=300)
        self.starting_screen_inkey_group = pg.sprite.Group(self.starting_inkey)

        self.intro_starting_inkey = IntroBlueGhost(location_x=(self.settings.GAME_WIDTH / 2) + 100, location_y=200)
        self.intro_starting_inkey_group = pg.sprite.Group(self.intro_starting_inkey)

        self.starting_pacman = StartingPacMan()
        self.starting_screen_pacman_group = pg.sprite.Group(self.starting_pacman)

        self.starting_pacman2 = StartingPacMan2()
        self.starting_screen_pacman_group_2 = pg.sprite.Group(self.starting_pacman2)

        self.starting_point = Point()
        self.starting_screen_point_group = pg.sprite.Group(self.starting_point)

        self.starting_eyes = Eyes()
        self.starting_screen_eyes_group = pg.sprite.Group(self.starting_eyes)

        # stores lists of these objects
        self.walls = []
        self.points = []
        self.ghosts = []
        self.ghosts_positions = []
        self.portals = []
        self.fruits = []

        # draw the maze
        self.load_maze()
        self.player = Player(game=self, settings=self.settings, screen=self.screen,
                             position_x=self.settings.player_starting_position_x,
                             position_y=self.settings.player_starting_position_y)
        self.make_enemies()

        # sounds
        self.eating = pg.mixer.Sound('sounds/pacman_eat.wav')
        self.fruit = pg.mixer.Sound('sounds/pacman_fruit.wav')
        self.fire_portal = pg.mixer.Sound('sounds/portal_open.wav')
        self.close_portal = pg.mixer.Sound('sounds/portal_close.wav')
        self.transport_portal = pg.mixer.Sound('sounds/portal_transport.wav')

        # buttons
        # the Play Game button on the start screen
        self.play_button = Buttons(screen=self.screen, msg='Play Game!',
                                   button_location_x=(self.settings.GAME_WIDTH / 2) - 50, button_location_y=500,
                                   text_font=self.settings.pac_man_font)

        # then the High Scores button on the start screen
        self.high_score_button = Buttons(screen=self.screen, msg='High Scores!',
                                         button_location_x=(self.settings.GAME_WIDTH / 2) - 50, button_location_y=580,
                                         text_font=self.settings.pac_man_font)

        # the title button on the start screen
        self.title_button = Buttons(screen=self.screen, msg='PAC MAN!',
                                    button_location_x=(self.settings.GAME_WIDTH / 2) - 50, button_location_y=10,
                                    text_font=self.settings.pac_man_font)

        # introducing the ghosts on the start screen
        # starting with pink ghost
        self.pink_ghost_button = Buttons(screen=self.screen, msg='Pinky!',
                                         button_location_x=(self.settings.GAME_WIDTH / 2) - 200, button_location_y=100,
                                         text_font=self.settings.ghost_font)

        # then red ghost
        self.red_ghost_button = Buttons(screen=self.screen, msg='Blinky!',
                                        button_location_x=(self.settings.GAME_WIDTH / 2) - 200, button_location_y=200,
                                        text_font=self.settings.ghost_font)

        # then orange ghost
        self.orange_ghost_button = Buttons(screen=self.screen, msg='Clyde!',
                                           button_location_x=(self.settings.GAME_WIDTH / 2) + 200,
                                           button_location_y=100,
                                           text_font=self.settings.ghost_font)

        # then blue ghost
        self.blue_ghost_button = Buttons(screen=self.screen, msg='Inkey!',
                                         button_location_x=(self.settings.GAME_WIDTH / 2) + 200, button_location_y=200,
                                         text_font=self.settings.ghost_font)

        # in the High Scores menu
        self.high_scores_title = Buttons(screen=self.screen, msg='High Scores',
                                         button_location_x=(self.settings.GAME_WIDTH / 2) - 50, button_location_y=10,
                                         text_font=self.settings.pac_man_font)

        self.go_back_button = Buttons(screen=self.screen, msg='Go Back',
                                      button_location_x=(self.settings.GAME_WIDTH / 2) - 50, button_location_y=150,
                                      text_font=self.settings.pac_man_font)

        # game over button for ending screen
        self.game_over_button = Buttons(screen=self.screen, msg='GAME OVER',
                                        button_location_x=(self.settings.GAME_WIDTH // 2) - 50,
                                        button_location_y=(self.settings.GAME_HEIGHT // 2) - 50,
                                        text_font=self.settings.pac_man_font)

        self.total_score_button = Buttons(screen=self.screen, msg='Total score: {}'.format(self.player.score),
                                          button_location_x=(self.settings.GAME_WIDTH // 2) - 50,
                                          button_location_y=(self.settings.GAME_HEIGHT // 2) + 70,
                                          text_font=self.settings.pac_man_font)

    def start_process_events(self):
        for event in pg.event.get():
            e_type = event.type
            if e_type == pg.QUIT:
                self.finished = True
            if e_type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                self.state = fun.check_button_clicked_one(play_button=self.play_button,
                                                          high_scores_button=self.high_score_button,
                                                          mouse_x=mouse_x, mouse_y=mouse_y)

    def start_update(self):
        self.starting_pinky.update_pinky()
        self.starting_blinky.update_blinky()
        self.starting_clyde.update_clyde()
        self.starting_inkey.update_inkey()
        self.starting_pacman.update_pacman()
        self.starting_point.update_point()
        self.starting_eyes.update_eyes()
        self.starting_pacman2.update_pacman()
        self.intro_starting_pinky.update_pinky()
        self.intro_starting_blinky.update_blinky()
        self.intro_starting_clyde.update_clyde()
        self.intro_starting_inkey.update_inkey()
        self.screen.fill(self.settings.BLACK)
        self.starting_screen_pinky_group.draw(self.screen)
        self.starting_screen_blinky_group.draw(self.screen)
        self.starting_screen_clyde_group.draw(self.screen)
        self.starting_screen_inkey_group.draw(self.screen)
        self.starting_screen_pacman_group.draw(self.screen)
        self.starting_screen_point_group.draw(self.screen)
        self.starting_screen_eyes_group.draw(self.screen)
        self.starting_screen_pacman_group_2.draw(self.screen)
        self.intro_starting_pinky_group.draw(self.screen)
        self.intro_starting_blinky_group.draw(self.screen)
        self.intro_starting_clyde_group.draw(self.screen)
        self.intro_starting_inkey_group.draw(self.screen)

    def start_draw(self):
        self.play_button.prep_msg(text_color=self.settings.WHITE,
                                  button_color=self.settings.BLACK)

        self.high_score_button.prep_msg(text_color=self.settings.WHITE,
                                        button_color=self.settings.BLACK)

        self.title_button.prep_msg(text_color=self.settings.ORANGE,
                                   button_color=self.settings.BLACK)

        self.pink_ghost_button.prep_msg(text_color=self.settings.PINK,
                                        button_color=self.settings.BLACK)

        self.red_ghost_button.prep_msg(text_color=self.settings.RED,
                                       button_color=self.settings.BLACK)

        self.orange_ghost_button.prep_msg(text_color=self.settings.ORANGE,
                                          button_color=self.settings.BLACK)

        self.blue_ghost_button.prep_msg(text_color=self.settings.CYAN,
                                        button_color=self.settings.BLACK)

    # this populates the lists with the locations of where each wall block, point, and fruit is
    def load_maze(self):
        # maze key:
        # 1 = wall
        # 3 = pacman's spawn point
        # 5 = point
        # 7 = fruit
        # 9 = whitespace
        # 2 = red ghost spawn
        # 4 = cyan ghost spawn
        # 6 = pink ghost spawn
        # 8 = orange ghost spawn

        # open the maze text file and create the walls of the maze as a list
        # Used these websites for reference in using 'with' statement
        # https://www.pythonforbeginners.com/files/with-statement-in-python
        # and https://www.w3schools.com/python/ref_func_open.asp
        with open('maze.txt', 'r') as maze_file:
            # Used this website for enumerate(file)
            # https://www.geeksforgeeks.org/enumerate-in-python/
            for row, line in enumerate(maze_file):
                for column, character in enumerate(line):
                    if character == '1':
                        self.walls.append((column, row))
                    elif character == '3':
                        self.settings.set_pacman_spawn(x=column, y=row)
                    elif character == '5':
                        self.points.append((column, row))
                    elif character == '7':
                        self.fruits.append((column, row))
                    elif character in ['2', '4', '6', '8']:
                        self.ghosts_positions.append([column, row])

    # draws the grid based off of whatever is in the walls list
    def draw_grid(self):
        for wall in self.walls:
            pg.draw.rect(self.screen, self.settings.ELECTRIC_BLUE,
                         (wall[0] * self.settings.CELL_WIDTH + self.settings.BUFFER//2,
                          wall[1] * self.settings.CELL_HEIGHT + self.settings.BUFFER//2,
                          self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))

    # populates the ghosts list with whatever is currently in the ghosts_positions list
    # list ghosts_positions keeps track of ghost locations
    # list ghosts keeps track of Ghost objects
    def make_enemies(self):
        counter = 0
        for ghost_type, position in enumerate(self.ghosts_positions):
            self.ghosts.append(Ghosts(game=self, player=self.player, settings=self.settings,
                                      position_x=self.ghosts_positions[counter][0],
                                      position_y=self.ghosts_positions[counter][1], ghost_type=ghost_type))
            counter += 1

    def playing_process_events(self):
        for event in pg.event.get():
            e_type = event.type
            if e_type == pg.QUIT:
                self.state = 'finished'
            if e_type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.player.move(move_x=-1, move_y=0, direction='left')
                if event.key == pg.K_RIGHT:
                    self.player.move(move_x=1, move_y=0, direction='right')
                if event.key == pg.K_UP:
                    self.player.move(move_x=0, move_y=-1, direction='up')
                if event.key == pg.K_DOWN:
                    self.player.move(move_x=0, move_y=1, direction='down')
                if event.key == pg.K_SPACE:
                    self.player.create_portal()
                if event.key == pg.K_ESCAPE:
                    self.state = 'finished'
        for each_ghost in self.ghosts:
            each_ghost.move()

    def playing_update(self):
        self.screen.fill(self.settings.BLACK)
        self.player.update()
        for each_ghost in self.ghosts:
            each_ghost.update()
        for each_portal in self.portals:
            each_portal.open(game=self)

    def playing_draw(self):
        self.draw_grid()
        fun.draw_text(msg='score = {}'.format(self.player.score), screen=self.screen, position_x=30,
                      position_y=10,
                      color=self.settings.WHITE, font=self.settings.game_font)
        fun.draw_text(msg='lives', screen=self.screen, position_x=230, position_y=10,
                      color=self.settings.WHITE, font=self.settings.game_font)
        fun.draw_points(screen=self.screen, points=self.points, settings=self.settings)
        fun.draw_fruits(screen=self.screen, fruits=self.fruits, settings=self.settings)
        self.player.draw()
        for each_ghost in self.ghosts:
            each_ghost.draw()
        pg.display.update()

    def high_scores_update(self):
        self.screen.fill(self.settings.BLACK)

    def high_scores_process_events(self):
        for event in pg.event.get():
            e_type = event.type
            if e_type == pg.QUIT:
                self.finished = True
            if e_type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                self.state = fun.check_button_clicked_two(go_back_button=self.go_back_button,
                                                          mouse_x=mouse_x, mouse_y=mouse_y)

    def high_scores_draw(self):
        self.high_scores_title.prep_msg(text_color=self.settings.WHITE,
                                        button_color=self.settings.BLACK)
        self.go_back_button.prep_msg(text_color=self.settings.WHITE,
                                     button_color=self.settings.BLACK)

    def game_over_update(self):
        self.screen.fill(self.settings.BLACK)

    def game_over_process_events(self):
        for event in pg.event.get():
            e_type = event.type
            if e_type == pg.QUIT:
                self.finished = True

    def game_over_draw(self):
        self.game_over_button.prep_msg(text_color=self.settings.WHITE,
                                       button_color=self.settings.BLACK)
        self.total_score_button.prep_msg(text_color=self.settings.WHITE,
                                         button_color=self.settings.BLACK)

    def play(self):
        # when the game first starts, play the game music
        fun.start_screen_music()
        # this game is state-controlled; whatever the state is, the display will show something different, so that
        # we can easily switch back and forth between states if needed
        while not self.finished:
            if self.state == 'start':
                self.start_update()
                self.start_process_events()
                self.start_draw()
            elif self.state == 'playing':
                fun.stop_start_screen_music()
                self.playing_update()
                self.playing_process_events()
                self.playing_draw()
            elif self.state == 'high scores':
                self.high_scores_update()
                self.high_scores_process_events()
                self.high_scores_draw()
            elif self.state == 'finished':
                self.game_over_update()
                self.game_over_process_events()
                self.game_over_draw()
            else:
                pass
            pg.display.update()
            self.clock.tick(10)


def main():
    pg.init()
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
