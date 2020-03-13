import pygame as pg


class Ghosts:
    # note: many of the functions and variables used here are the same as in the player.py file
    # thus, explanations for these functions and variables are in player.py

    def __init__(self, game, player, settings, position_x, position_y, ghost_type):
        self.game = game
        self.settings = settings
        self.player = player
        # store whether the ghost is pink, red, orange, or blue
        self.type = ghost_type
        # didn't have time to animate the ghosts, and so the ghosts are simply drawn circles on the screen
        self.color = self.set_color()
        self.maze_position = [position_x, position_y]
        self.ghost_position = [(self.maze_position[0] * self.settings.CELL_WIDTH) +
                               self.settings.BUFFER // 2 + self.settings.CELL_WIDTH // 2,
                               (self.maze_position[1] * self.settings.CELL_HEIGHT) +
                               self.settings.BUFFER // 2 + self.settings.CELL_HEIGHT // 2]

        self.movement = [1, 0]
        self.current_movement = [0, 0]
        # each ghost has a different behavior, so store a different behavior trait for each of them
        self.behavior = self.set_behavior()

        self.can_move = True

        # keep track of ghost movements
        self.pink_counter = 0

        # load the ghost images
        self.red_left_images = []
        self.orange_left_images = []
        self.pink_left_images = []
        self.cyan_left_images = []
        self.red_right_images = []
        self.orange_right_images = []
        self.pink_right_images = []
        self.cyan_right_images = []
        self.red_up_images = []
        self.orange_up_images = []
        self.pink_up_images = []
        self.cyan_up_images = []
        self.red_down_images = []
        self.orange_down_images = []
        self.pink_down_images = []
        self.cyan_down_images = []

        # getting all the images...
        self.picture = pg.image.load('images/red_ghost_left_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.red_left_images.append(self.picture)
        self.picture = pg.image.load('images/red_ghost_left_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.red_left_images.append(self.picture)

        self.picture = pg.image.load('images/red_ghost_right_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.red_right_images.append(self.picture)
        self.picture = pg.image.load('images/red_ghost_right_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.red_right_images.append(self.picture)

        self.picture = pg.image.load('images/red_ghost_up_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.red_up_images.append(self.picture)
        self.picture = pg.image.load('images/red_ghost_up_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.red_up_images.append(self.picture)

        self.picture = pg.image.load('images/red_ghost_down_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.red_down_images.append(self.picture)
        self.picture = pg.image.load('images/red_ghost_down_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.red_down_images.append(self.picture)

        self.picture = pg.image.load('images/orange_ghost_left_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.orange_left_images.append(self.picture)
        self.picture = pg.image.load('images/orange_ghost_left_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.orange_left_images.append(self.picture)

        self.picture = pg.image.load('images/orange_ghost_right_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.orange_right_images.append(self.picture)
        self.picture = pg.image.load('images/orange_ghost_right_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.orange_right_images.append(self.picture)

        self.picture = pg.image.load('images/orange_ghost_up_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.orange_up_images.append(self.picture)
        self.picture = pg.image.load('images/orange_ghost_up_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.orange_up_images.append(self.picture)

        self.picture = pg.image.load('images/orange_ghost_down_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.orange_down_images.append(self.picture)
        self.picture = pg.image.load('images/orange_ghost_down_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.orange_down_images.append(self.picture)

        self.picture = pg.image.load('images/pink_ghost_left_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.pink_left_images.append(self.picture)
        self.picture = pg.image.load('images/pink_ghost_left_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.pink_left_images.append(self.picture)

        self.picture = pg.image.load('images/pink_ghost_right_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.pink_right_images.append(self.picture)
        self.picture = pg.image.load('images/pink_ghost_right_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.pink_right_images.append(self.picture)

        self.picture = pg.image.load('images/pink_ghost_up_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.pink_up_images.append(self.picture)
        self.picture = pg.image.load('images/pink_ghost_up_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.pink_up_images.append(self.picture)

        self.picture = pg.image.load('images/pink_ghost_down_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.pink_down_images.append(self.picture)
        self.picture = pg.image.load('images/pink_ghost_down_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.pink_down_images.append(self.picture)

        self.picture = pg.image.load('images/cyan_ghost_left_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.cyan_left_images.append(self.picture)
        self.picture = pg.image.load('images/cyan_ghost_left_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.cyan_left_images.append(self.picture)

        self.picture = pg.image.load('images/cyan_ghost_right_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.cyan_right_images.append(self.picture)
        self.picture = pg.image.load('images/cyan_ghost_right_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.cyan_right_images.append(self.picture)

        self.picture = pg.image.load('images/cyan_ghost_up_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.cyan_up_images.append(self.picture)
        self.picture = pg.image.load('images/cyan_ghost_up_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.cyan_up_images.append(self.picture)

        self.picture = pg.image.load('images/cyan_ghost_down_1.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.cyan_down_images.append(self.picture)
        self.picture = pg.image.load('images/cyan_ghost_down_2.png')
        self.picture = pg.transform.scale(self.picture, (self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT))
        self.cyan_down_images.append(self.picture)

        self.index_red = 0
        self.image_red = self.red_left_images[self.index_red]
        self.index_orange = 0
        self.image_orange = self.orange_left_images[self.index_orange]
        self.index_pink = 0
        self.image_pink = self.pink_left_images[self.index_pink]
        self.index_cyan = 0
        self.image_cyan = self.cyan_left_images[self.index_cyan]

        self.rect_red = self.image_red.get_rect()
        self.rect_red = pg.Rect(self.maze_position[0] * self.settings.CELL_WIDTH +
                                self.settings.BUFFER // 2,
                                self.maze_position[1] * self.settings.CELL_HEIGHT +
                                self.settings.BUFFER // 2,
                                self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT)
        self.rect_orange = self.image_orange.get_rect()
        self.rect_orange = pg.Rect(self.maze_position[0] * self.settings.CELL_WIDTH +
                                   self.settings.BUFFER // 2,
                                   self.maze_position[1] * self.settings.CELL_HEIGHT +
                                   self.settings.BUFFER // 2,
                                   self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT)
        self.rect_pink = self.image_pink.get_rect()
        self.rect_pink = pg.Rect(self.maze_position[0] * self.settings.CELL_WIDTH +
                                 self.settings.BUFFER // 2,
                                 self.maze_position[1] * self.settings.CELL_HEIGHT +
                                 self.settings.BUFFER // 2,
                                 self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT)
        self.rect_cyan = self.image_cyan.get_rect()
        self.rect_cyan = pg.Rect(self.maze_position[0] * self.settings.CELL_WIDTH +
                                 self.settings.BUFFER // 2,
                                 self.maze_position[1] * self.settings.CELL_HEIGHT +
                                 self.settings.BUFFER // 2,
                                 self.settings.CELL_WIDTH, self.settings.CELL_HEIGHT)

        self.rect_red.x = self.rect_red.width
        self.rect_red.y = self.rect_red.height
        self.red_x = float(self.rect_red.x)
        self.red_y = float(self.rect_red.y)
        self.center_red = float(self.rect_red.centerx)

        self.rect_orange.x = self.rect_orange.width
        self.rect_orange.y = self.rect_orange.height
        self.orange_x = float(self.rect_orange.x)
        self.orange_y = float(self.rect_orange.y)
        self.center_orange = float(self.rect_orange.centerx)

        self.rect_pink.x = self.rect_pink.width
        self.rect_pink.y = self.rect_pink.height
        self.pink_x = float(self.rect_pink.x)
        self.pink_y = float(self.rect_pink.y)
        self.center_pink = float(self.rect_pink.centerx)

        self.rect_cyan.x = self.rect_cyan.width
        self.rect_cyan.y = self.rect_cyan.height
        self.cyan_x = float(self.rect_cyan.x)
        self.cyan_y = float(self.rect_cyan.y)
        self.center_cyan = float(self.rect_cyan.centerx)

        # note: didn't implement ghost animations yet

    def update(self):
        # same functioning as in player.py

        self.can_move = self.peek()
        if self.can_move:
            self.ghost_position[0] += self.current_movement[0]
            self.ghost_position[1] += self.current_movement[1]

        if int(self.ghost_position[0] + self.settings.BUFFER // 2) % self.settings.CELL_WIDTH == 0:
            if (self.movement[0] == 1 and self.movement[1] == 0) \
                    or (self.movement[0] == -1 and self.movement[1] == 0):
                self.movement[0] = self.current_movement[0]
                self.movement[1] = self.current_movement[1]

        if int(self.ghost_position[1] + self.settings.BUFFER // 2) % self.settings.CELL_HEIGHT == 0:
            if (self.movement[0] == 0 and self.movement[1] == 1) \
                    or (self.movement[0] == 0 and self.movement[1] == -1):
                self.movement[0] = self.current_movement[0]
                self.movement[1] = self.current_movement[1]

        self.maze_position[0] = (self.ghost_position[0] - self.settings.BUFFER +
                                 self.settings.CELL_WIDTH // 2) // self.settings.CELL_WIDTH + 1
        self.maze_position[1] = (self.ghost_position[1] - self.settings.BUFFER +
                                 self.settings.CELL_HEIGHT // 2) // self.settings.CELL_HEIGHT + 1

    def move(self):
        # this function is called within the Game class; determine the ghost's behavior of movement
        if self.behavior == 'pink_behavior':
            self.current_movement = self.get_pink_movement()
        if self.behavior == 'cyan_behavior' or self.behavior == 'orange_behavior':
            self.current_movement = self.get_cyan_movement()
        if self.behavior == 'red_behavior':
            pass
            # self.current_movement = self.get_red_movement()

    def get_pink_movement(self):
        # this ghost moves counterclockwise and so, every 200 frames, change its direction in
        # counterclockwise fashion

        # initial values
        position_x = 0
        position_y = 0

        # so that the self.pink_counter does not get Way Too Big, reset the counter to 0 whenever it reaches 800
        if self.pink_counter == 800:
            self.pink_counter = 0

        # up
        if self.pink_counter < 200:
            position_x = 0
            position_y = -1
        # left
        if 200 <= self.pink_counter < 400:
            position_x = -1
            position_y = 0
        # down
        if 400 <= self.pink_counter < 600:
            position_x = 0
            position_y = 1
        # right
        if 600 <= self.pink_counter < 800:
            position_x = 1
            position_y = 0

        self.pink_counter += 1
        direction = [position_x, position_y]

        return direction

    def get_cyan_movement(self):
        # same as get_pink_movement above, but now moving clockwise

        position_x = 0
        position_y = 0
        if self.pink_counter == 800:
            self.pink_counter = 0
        if self.pink_counter < 200:
            position_x = 0
            position_y = -1
        if 200 <= self.pink_counter < 400:
            position_x = 1
            position_y = 0
        if 400 <= self.pink_counter < 600:
            position_x = 0
            position_y = 1
        if 600 <= self.pink_counter < 800:
            position_x = -1
            position_y = 0
        self.pink_counter += 1
        direction = [position_x, position_y]

        return direction

    def get_red_movement(self):
        # red is the most aggressive
        # not completed, but this is an attempt at getting the red ghost to move to wherever the player currently is

        # store the player's current location
        target_x = self.player.get_maze_position_x()
        target_y = self.player.get_maze_position_y()

        # list to keep track of all possible movements; there are 4 directions that the red ghost can travel in
        # we want the direction that'll bring him closest to the player
        test_movements = []

        # if red ghost moves 1 space in its current direction, this would be its new value,
        # as stored these test_ variables
        test_right = (self.ghost_position[0] + 1, self.ghost_position[1])
        test_left = (self.ghost_position[0] - 1, self.ghost_position[1])
        test_up = (self.ghost_position[0], self.ghost_position[1] - 1)
        test_down = (self.ghost_position[0], self.ghost_position[1] + 1)

        # add these test_ variables to test_movements
        test_movements.append(test_right)
        test_movements.append(test_left)
        test_movements.append(test_up)
        test_movements.append(test_down)

        # this variable keeps track of the current shortest distance; 100 is an arbitrary value
        shortest_distance = [100]

        # loop through test_movements and find whichever one has the shortest distance to the player
        # if the new distance found is shorter than whatever is currently in shortest_distance, then clear
        # shortest_distance and replace it with this new distance value
        for all_movements in test_movements:
            distance = (target_x - all_movements[0]) + (target_y - all_movements[1])
            if distance < shortest_distance[0]:
                shortest_distance.pop()
                new_shortest_distance = (all_movements[0], all_movements[1])
                shortest_distance[0] = new_shortest_distance

        # return the shortest_distance as the direction that the red ghost should be moving in
        return shortest_distance[0]

    def peek(self):
        for wall in self.game.walls:
            if (self.maze_position[0] + self.current_movement[0]) \
                    == wall[0] and (self.maze_position[1] + self.current_movement[1]) == wall[1]:
                return False
        return True

    def draw(self):
        # didn't animate ghosts, so ghosts are simply drawn circles on the screen
        pg.draw.circle(self.game.screen, self.color, (self.ghost_position[0], self.ghost_position[1]), 5)

    def set_color(self):
        if self.type == 0:
            return self.settings.RED
        if self.type == 1:
            return self.settings.CYAN
        if self.type == 2:
            return self.settings.PINK
        if self.type == 3:
            return self.settings.ORANGE

    def set_behavior(self):
        if self.type == 0:
            # aggressive
            return 'red_behavior'
        if self.type == 1:
            # clockwise
            return 'cyan_behavior'
        if self.type == 2:
            # counterclockwise
            return 'pink_behavior'
        if self.type == 3:
            # clockwise
            return 'orange_behavior'

    # function with intention of animating ghost
    def set_image(self):
        if self.type == 2:
            return self.red_left_images[self.index_red]
        elif self.type == 4:
            return self.cyan_left_images[self.index_cyan]
        elif self.type == 6:
            return self.pink_left_images[self.index_pink]
        elif self.type == 8:
            return self.orange_left_images[self.index_orange]
