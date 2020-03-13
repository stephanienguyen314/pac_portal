# miscellaneous functions that did not necessarily have to be a part of game.py
# stored here for organization
import pygame as pg


# play the start screen music
def start_screen_music():
    pg.mixer.init()
    pg.mixer.music.load('sounds/pacman_start_music.wav')
    pg.mixer.music.play(-1)


# when the game begins, stop the start screen music
def stop_start_screen_music():
    pg.mixer.music.stop()


# check if the first button on the start screen was clicked on
def check_button_clicked_one(play_button, high_scores_button, mouse_x, mouse_y):
    state = ''
    play_button_clicked = play_button.button_rect.collidepoint(mouse_x, mouse_y)
    high_scores_button_clicked = high_scores_button.button_rect.collidepoint(mouse_x, mouse_y)
    if play_button_clicked:
        state = 'playing'
    elif high_scores_button_clicked:
        state = 'high scores'
    return state


# check if the second button on the start screen was clicked
def check_button_clicked_two(go_back_button, mouse_x, mouse_y):
    state = ''
    go_back_button_clicked = go_back_button.button_rect.collidepoint(mouse_x, mouse_y)
    if go_back_button_clicked:
        state = 'start'
    return state


# drawing the text on the playing screen; this text didn't need to be a Button, so it's just text
def draw_text(msg, screen, position_x, position_y, color, font):
    text_font = font
    text_msg = text_font.render(msg, False, color)
    screen.blit(text_msg, (position_x, position_y))


# draw all the points in the game; note that points is constantly being updated depending on what the player has eaten
def draw_points(screen, points, settings):
    counter = 0
    for _ in points:
        pg.draw.circle(screen, settings.WHITE,
                       (int(points[counter][0] * settings.CELL_WIDTH +
                            settings.BUFFER - settings.CELL_WIDTH // 2 - 5),
                        int(points[counter][1] * settings.CELL_HEIGHT +
                            settings.BUFFER - settings.CELL_HEIGHT // 2 - 5)), 5)
        counter += 1


# same as draw_points, but with fruits
def draw_fruits(screen, fruits, settings):
    counter = 0
    for _ in fruits:
        pg.draw.circle(screen, settings.FRUIT_PINK,
                       (int(fruits[counter][0] * settings.CELL_WIDTH +
                            settings.BUFFER - settings.CELL_WIDTH // 2 - 5),
                        int(fruits[counter][1] * settings.CELL_HEIGHT +
                            settings.BUFFER - settings.CELL_HEIGHT // 2 - 5)), 5)
        counter += 1
