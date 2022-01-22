class Settings:
    """a class to store all settings for alien invension"""

    def __init__(self):
        """initialize the game's settings"""

        self.screen_width = 1200    # 1360  #1200
        self.screen_height = 800   # 768   #800

        self.bg_color = (255, 255, 255)

        # ship setting speed
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # BULLET SETTINGS
        self.bullet_speed_factor = 1
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # fleet direction of 1 represent right ; -1 represent left
        self.fleet_direction = 1

        # how quickly  the game speed up
        self.speedup_scale = 1.1

        # how quickly the alien point values increase
        self.score_scale = 0.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ initialize settings that change throughout the game """
        self.ship_speed_factor = 1.5
        self. bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet direction of 1 represents right ; -1 represents left
        self.fleet_direction = 1
        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """ increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        """ increase speed setting and alien point values"""
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)