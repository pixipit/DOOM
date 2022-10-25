import random

import numpy as np
import pygame

from Custum_Components.enemy import Enemy
from game import Game
from game_object import GameObject


class Zdenek(Enemy):
    timer = 0.0
    teleport_delay = 5.0
    next_teleport_pos = [300.0, 300.0]

    def start(self):
        super().start()
        self.set_up()

    def update(self):
        self.timer += Game.game.get_delta_time()
        if self.timer > self.teleport_delay:
            self.timer = 0
            self.teleport()
            self.set_up()

    def teleport(self):
        self.game_object.position = self.next_teleport_pos

    def set_up(self):
        position_range = [150.0, 450.0]
        self.next_teleport_pos = [random.uniform(position_range[0], position_range[1]),
                                  random.uniform(position_range[0], position_range[1])]
        prev_indication = Game.game.find_by_name('indication_zdenek')
        if prev_indication is not None:
            prev_indication.destroy()
        self.create_indication()

    def create_indication(self):
        img = pygame.Surface([70, 70])
        img.fill([100, 100, 155])
        g = GameObject(position=np.array(self.next_teleport_pos), img=img, name='indication_zdenek')
        Game.game.create_game_object(g)
