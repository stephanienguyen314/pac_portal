# from textbook

import pygame.font
import pygame as pg


class Buttons:

    def __init__(self, screen, msg, button_location_x, button_location_y, text_font):
        self.pac_man_font = pg.font.SysFont(None, 48)
        self.ghost_font = pg.font.SysFont(None, 20)
        self.button_rect = pg.Rect(button_location_x, button_location_y, 100, 100)
        self.pac_man_text_color = (251, 191, 72)
        self.button_color = (0, 0, 0)

        self.msg = msg
        self.screen = screen
        self.font = text_font

        self.msg_image = None
        self.msg_image_rect = None

    def prep_msg(self, text_color, button_color):
        self.msg_image = self.font.render(self.msg, True, text_color,
                                          button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.button_rect.center

        self.draw_button()

    def draw_button(self):
        # Draw the blank button and draw message
        self.screen.fill(self.button_color, self.button_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
