class Settings():
    """A class to store all the settings of the game."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.screen_colour = (230, 230, 230)

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10


        # Ship settings
        self.ship_limit = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction of 1 represents right; -1 represent left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale