import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stat import GameStats
from button import Button
from scoreboard import Scoreboard
import game_function as gf


def run_game():
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make the play button.
    play_button = Button(ai_settings, screen, "Play")
    ship = Ship(ai_settings, screen)

    # create an instance to store  game statistics
    stats = GameStats(ai_settings)

    # create an instance to store game statistics and create a score board
    sb = Scoreboard(ai_settings, screen, stats)

    # bg_color = (255, 255, 255)
    # make a group to store bullet in .
    bullets = Group()

    # make a ship, a group of bullets and a group of aliens.
    aliens = Group()

    # create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # make an alien.
    alien = Alien(ai_settings, screen)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        # for event in pygame.event.get():
        #   if event.type == pygame.QUIT:
        #      sys.exit()

        if stats.game_active:
            ship.update()
            bullets.update()

            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # get rid of bullets that have disappeared.
            #    for bullet in bullets.copy():
            #        if bullet.rect.bottom<=0:
            #            bullets.remove(bullet)
            #    print(len(bullets))
            gf.update_aliens(ai_settings, stats, screen,sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()

        pygame.display.flip()


run_game()

"""page no 337
"""