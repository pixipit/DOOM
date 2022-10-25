import random

import numpy as np

from component import Component
from game import Game


class Weapon(Component):
    timer = 0.0

    def __init__(self, bullet, fire_rate: float, offset=[0, 0], time_offset=0.0, direction=[0.0, 1.0]):
        self.bullet = bullet
        self.fire_rate = fire_rate
        self.offset = offset
        self.time_offset = time_offset
        self.direction = direction

    def update(self):
        self.timer += Game.game.get_delta_time()
        if self.timer > 1/self.fire_rate:
            self.timer = 0
            self.shoot()

    def shoot(self):
        Game.game.create_game_object(self.bullet,
                                     np.array(self.game_object.position) + np.array(self.offset), self.direction)
