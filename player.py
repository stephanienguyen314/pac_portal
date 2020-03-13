import pygame as pg
from pygame.sprite import Sprite


class Player(Sprite):

    def __init__(self, game, screen, position_x, position_y, settings, *groups):

        super().__init__(*groups)
        self.settings = settings
        self.screen = screen
        self.game = game
        # the player's spawn position, as determined in the settings file
        self.maze_position = [position_x, position_y]
        # the player's x position is a function of their:
        # self.maze_position[0] = column number
        # self.settings.CELL_WIDTH = the size of each cell
        # self.settings.BUFFER = must add 1/2 the buffer space because the maze is drawn in the middle of the screen
        # self.settings.CELL_WIDTH // 2 = so that the player is blitted in the middle of the cell that it is curently
        #                                 in, otherwise it would default to be in the upper lefthand corner
        # same with the player's y position
        self.player_position = [(self.maze_position[0] * self.settings.CELL_WIDTH) +
                                self.settings.BUFFER // 2 + self.settings.CELL_WIDTH // 2,
                                (self.maze_position[1] * self.settings.CELL_HEIGHT) +
                                self.settings.BUFFER // 2 + self.settings.CELL_HEIGHT // 2]
        # initial values
        self.movement = [1, 0]
        self.current_movement = [0, 0]

        # to be used to determine if the player's next movement will make them run into a wall
        self.can_move = True

        # movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

        # load the player and portal images
        self.player_left_images = []
        self.player_right_images = []
        self.player_up_images = []
        self.player_down_images = []
        self.open_portal_images = []
        self.close_portal_images = []

        # getting all the images...
        self.picture = pg.image.load('images/pac_man_left_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_left_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_left_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_left_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_left_3.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_left_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_left_4.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_left_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_left_5.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_left_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_left_6.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_left_images.append(self.picture)

        self.picture = pg.image.load('images/pac_man_right_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_right_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_right_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_right_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_right_3.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_right_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_right_4.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_right_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_right_5.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_right_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_right_6.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_right_images.append(self.picture)

        self.picture = pg.image.load('images/pac_man_up_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_up_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_up_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_up_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_up_3.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_up_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_up_4.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_up_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_up_5.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_up_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_up_6.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_up_images.append(self.picture)

        self.picture = pg.image.load('images/pac_man_down_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_down_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_down_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_down_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_down_3.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_down_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_down_4.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_down_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_down_5.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_down_images.append(self.picture)
        self.picture = pg.image.load('images/pac_man_down_6.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.player_down_images.append(self.picture)

        self.picture = pg.image.load('images/portal_open_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.open_portal_images.append(self.picture)
        self.picture = pg.image.load('images/portal_open_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.open_portal_images.append(self.picture)
        self.picture = pg.image.load('images/portal_open_3.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.open_portal_images.append(self.picture)

        self.picture = pg.image.load('images/portal_close_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.close_portal_images.append(self.picture)
        self.picture = pg.image.load('images/portal_close_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.close_portal_images.append(self.picture)
        self.picture = pg.image.load('images/portal_close_3.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.close_portal_images.append(self.picture)

        self.index = 0
        if self.moving_left:
            self.image = self.player_left_images[self.index]
        elif self.moving_right:
            self.image = self.player_right_images[self.index]
        elif self.moving_up:
            self.image = self.player_up_images[self.index]
        elif self.moving_down:
            self.image = self.player_down_images[self.index]
        else:
            self.image = self.player_left_images[self.index]

        self.rect = self.image.get_rect()
        self.rect = pg.Rect(self.maze_position[0] * self.settings.CELL_WIDTH +
                            self.settings.BUFFER // 2,
                            self.maze_position[1] * self.settings.CELL_HEIGHT +
                            self.settings.BUFFER // 2,
                            self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT)

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.center = float(self.rect.centerx)

        # keep track of the player's score in the game
        self.score = 0

        # draw the initial portal anywhere off the screen
        self.portal_location_open_x = -10
        self.portal_location_open_y = -10
        self.portal_location_close_x = -10
        self.portal_location_close_y = -10

        # portals are stored as a list
        self.portals = []
        self.go_through_portal = True

    def update(self):
        # check if the next movement in the currently moving direction will make us run into a wall
        self.can_move = self.peek()
        if self.can_move:
            # if we can move, then set the new player position to be whatever direction it's currently moving in,
            # multipled by the speed factor of the player, which is stored in the settings class
            self.player_position[0] += self.current_movement[0] * self.settings.pacman_speed
            self.player_position[1] += self.current_movement[1] * self.settings.pacman_speed

        # check if the player is go through a portal; this happens when the player FAILS the wall test above
        # BUT if there's a portal, that means the player can still move through!
        self.go_through_portal = self.found_portal()
        if self.go_through_portal:
            self.player_position[0] += self.current_movement[0]
            self.player_position[1] += self.current_movement[1]
            pg.mixer.Sound.play(self.game.close_portal)

        # keep the player moving on the grid AKA no free movements, only right/left/up/down
        # take the player's current x position and add it to the half the buffer space; again, this must be done because
        # the maze is drawn in the middle of the screen, so we must always account for it
        # then we % by the cell width; if this value is 0, that means the player is perfectly within a cell
        # and we have confined the player's movement to be only within the cells of the maze grid
        # this works because the player's current x position is a function of their current column number and the
        # cell width
        # for example, if player_position = 20 and cell_width = 50, this would fail because then that means the player
        # might be trying to move somewhere that is not within the grid of available movements
        if int(self.player_position[0] + self.settings.BUFFER // 2) % self.settings.CELL_WIDTH == 0:
            if (self.movement[0] == 1 and self.movement[1] == 0) \
                    or (self.movement[0] == -1 and self.movement[1] == 0):
                self.movement[0] = self.current_movement[0]
                self.movement[1] = self.current_movement[1]

        # same thing with this, but it determines for the player's current y position, if the player is moving
        # up or down; the above is for if the player is moving right or left
        if int(self.player_position[1] + self.settings.BUFFER // 2) % self.settings.CELL_HEIGHT == 0:
            if (self.movement[0] == 0 and self.movement[1] == 1) \
                    or (self.movement[0] == 0 and self.movement[1] == -1):
                self.movement[0] = self.current_movement[0]
                self.movement[1] = self.current_movement[1]

        # this keeps track of where the player is in the maze
        self.maze_position[0] = (self.player_position[0] - self.settings.BUFFER +
                                 self.settings.CELL_WIDTH // 2) // self.settings.CELL_WIDTH + 1
        self.maze_position[1] = (self.player_position[1] - self.settings.BUFFER +
                                 self.settings.CELL_HEIGHT // 2) // self.settings.CELL_HEIGHT + 1

        # see if the player's movement has made it land on a point
        self.found_point()

        # see if the player's movement has made it land on a fruit
        self.found_fruit()

        # depending on player's current direction, show the correct set of images: right, left, up, or down
        if self.moving_right:
            self.index += 1
            if self.index >= len(self.player_right_images):
                self.index = 0
            self.image = self.player_right_images[self.index]
            self.x += self.current_movement[0]
            self.rect.x = self.x
        if self.moving_left:
            self.index += 1
            if self.index >= len(self.player_left_images):
                self.index = 0
            self.image = self.player_left_images[self.index]
            self.x += self.current_movement[0]
            self.rect.x = self.x
        if self.moving_up:
            self.index += 1
            if self.index >= len(self.player_up_images):
                self.index = 0
            self.image = self.player_up_images[self.index]
            self.y += self.current_movement[1]
            self.rect.y = self.y
        if self.moving_down:
            self.index += 1
            if self.index >= len(self.player_down_images):
                self.index = 0
            self.image = self.player_down_images[self.index]
            self.y += self.current_movement[1]
            self.rect.y = self.y

    def peek(self):
        # check to see if the next cell in the currently moving direction will cause the player to hit a wall
        # if yes, then return False which means we can't move in that direction anymore
        for wall in self.game.walls:
            if (self.maze_position[0] + self.current_movement[0]) \
                    == wall[0] and (self.maze_position[1] + self.current_movement[1]) == wall[1]:
                return False
        return True

    def draw(self):
        # blit player's current location
        # self.maze_position[0] = their x position
        # self.settings.CELL_WIDTH = the size of the player
        # self.settings.BUFFER // 2 = must divide by 2 because the maze is drawn with a buffer of 1/2 size of
        # self.settings.BUFFER
        self.screen.blit(self.image, (self.maze_position[0] * self.settings.CELL_WIDTH +
                                      self.settings.BUFFER // 2,
                                      self.maze_position[1] * self.settings.CELL_HEIGHT +
                                      self.settings.BUFFER // 2,
                                      self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        # originally had 'all_portals' in place of '_' in the for loop statement below, but PyCharm says that's an error
        # and wanted '_' instead
        for _ in self.portals:
            pg.draw.rect(self.game.screen, self.settings.ORANGE,
                         (self.portal_location_open_x * self.settings.CELL_WIDTH + self.settings.CELL_WIDTH + 5,
                          self.portal_location_open_y * self.settings.CELL_HEIGHT + self.settings.CELL_HEIGHT + 5,
                          self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
            pg.draw.rect(self.game.screen, self.settings.ORANGE,
                         (self.portal_location_close_x * self.settings.CELL_WIDTH + self.settings.CELL_WIDTH + 5,
                          self.portal_location_close_y * self.settings.CELL_HEIGHT + self.settings.CELL_HEIGHT + 5,
                          self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))

    def found_point(self):
        # function that determines if the player has hit any of the points on the maze
        # self.game.points stores all the points and their locations
        for point in self.game.points:
            if self.maze_position[0] == point[0] and self.maze_position[1] == point[1]:
                self.remove_point(x=point[0], y=point[1])
                self.score += 10
                pg.mixer.Sound.play(self.game.eating)
        return False

    def remove_point(self, x, y):
        # this function is called by self.found_point()
        # whenever the player hits a point, it must eat the point; thus, we must remove the point from the
        # points list, which is self.game.points, so that when the game redraws all the points, it won't draw
        # the eaten point
        for all_points in self.game.points:
            if all_points[0] == x and all_points[1] == y:
                self.game.points.remove((all_points[0], all_points[1]))

    def found_fruit(self):
        for fruit in self.game.fruits:
            if self.maze_position[0] == fruit[0] and self.maze_position[1] == fruit[1]:
                self.remove_fruit(x=fruit[0], y=fruit[1])
                self.score += 50
                pg.mixer.Sound.play(self.game.fruit)
        return False

    def remove_fruit(self, x, y):
        for all_fruits in self.game.fruits:
            if all_fruits[0] == x and all_fruits[1] == y:
                self.game.fruits.remove((all_fruits[0], all_fruits[1]))

    def move(self, move_x, move_y, direction):
        # this function is used in the main Game class
        # depending on which arrow key the player has pressed, it will pass in an x value and a y value, both
        # representing movements of the player
        self.current_movement[0] = move_x
        self.current_movement[1] = move_y

        # once a player presses a different arrow key, we must reset the movement flags so that only
        # 1 flag is true at a time
        if direction == 'right':
            self.moving_right = True
            self.moving_left = False
            self.moving_up = False
            self.moving_down = False
        if direction == 'left':
            self.moving_left = True
            self.moving_right = False
            self.moving_up = False
            self.moving_down = False
        if direction == 'up':
            self.moving_up = True
            self.moving_left = False
            self.moving_right = False
            self.moving_down = False
        if direction == 'down':
            self.moving_down = True
            self.moving_left = False
            self.moving_right = False
            self.moving_up = False

    def create_portal(self):
        # depending on which direction the player is moving, they can create an opening portal
        # and a closing portal in that direction - in front of them and behind them
        # at the beginning of the game, since the player is not moving, they cannot create a portal
        if self.moving_right:
            self.portal_location_open_x = 27
            self.portal_location_open_y = self.maze_position[1]
            self.portal_location_close_x = 0
            self.portal_location_close_y = self.maze_position[1]
            self.portals.append((self.portal_location_open_x, self.portal_location_open_y))
            self.portals.append((self.portal_location_close_x, self.portal_location_close_y))
        if self.moving_left:
            self.portal_location_open_x = 0
            self.portal_location_open_y = self.maze_position[1]
            self.portal_location_close_x = 27
            self.portal_location_close_y = self.maze_position[1]
            self.portals.append((self.portal_location_open_x, self.portal_location_open_y))
            self.portals.append((self.portal_location_close_x, self.portal_location_close_y))
        if self.moving_up:
            self.portal_location_open_x = self.maze_position[0]
            self.portal_location_open_y = 0
            self.portal_location_close_x = self.maze_position[0]
            self.portal_location_close_y = 30
            self.portals.append((self.portal_location_open_x, self.portal_location_open_y))
            self.portals.append((self.portal_location_close_x, self.portal_location_close_y))
        if self.moving_down:
            self.portal_location_open_x = self.maze_position[0]
            self.portal_location_open_y = 30
            self.portal_location_close_x = self.maze_position[0]
            self.portal_location_close_y = 0
            self.portals.append((self.portal_location_open_x, self.portal_location_open_y))
            self.portals.append((self.portal_location_close_x, self.portal_location_close_y))
        pg.mixer.Sound.play(self.game.fire_portal)

    def found_portal(self):
        # numbers below (541, 59, 601) obtained by just experimenting to see what values would make
        # PacMan teleport to where I wanted him to be
        for all_portals in self.portals:
            if (self.maze_position[0] + self.current_movement[0]) == all_portals[0] \
                    and (self.maze_position[1] + self.current_movement[1]) == all_portals[1]:
                if self.maze_position[0] == 1:
                    self.player_position[0] = 541
                    self.maze_position[0] = 541
                    self.portals.pop()
                    self.portals.pop()
                    pg.mixer.Sound.play(self.game.transport_portal)
                    return True
                if self.maze_position[0] == 26:
                    self.player_position[0] = 59
                    self.maze_position[0] = 59
                    self.portals.pop()
                    self.portals.pop()
                    pg.mixer.Sound.play(self.game.transport_portal)
                    return True
                if self.maze_position[1] == 1:
                    self.player_position[1] = 601
                    self.maze_position[1] = 601
                    self.portals.pop()
                    self.portals.pop()
                    pg.mixer.Sound.play(self.game.transport_portal)
                    return True
                if self.maze_position[1] == 29:
                    self.player_position[1] = 59
                    self.maze_position[1] = 59
                    self.portals.pop()
                    self.portals.pop()
                    pg.mixer.Sound.play(self.game.transport_portal)
                    return True
        return False
