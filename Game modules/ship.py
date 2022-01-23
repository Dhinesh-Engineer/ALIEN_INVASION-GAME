import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """initialise the ship and set its starting position"""
        super(Ship, self).__init__()
        
        self.screen = screen

        # ship speed by ai_settings
        self.ai_settings = ai_settings

        self.image = pygame.image.load('../images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.top = self.screen_rect.top

        # movement flags
        self.moving_right = False
        self.moving_left = False
        # self.moving_up = False
        # self.moving_down = False

    def update(self):
        """update the ship positon based on the movement flags"""
        """update the ship's center value,not the rect"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # if self.moving_up:
        #    self.rect.bottom -= self.ai_settings.ship_speed_factor
        # if self.moving_down:
        #    self.rect.top += self.ai_settings.ship_speed_factor

        # update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """draw the ship at its current location """

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ center the ship on the screen."""
        self.center = self.screen_rect.centerx
