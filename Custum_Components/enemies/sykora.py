import random

import numpy as np
import pygame

from Custum_Components.box_collider import BoxCollider
from Custum_Components.enemies.boss_budai import BossBudai
from Custum_Components.enemy import Enemy
from game import Game
from game_object import GameObject


class Sykora(BossBudai):
    gap = 0.1
    timer = 0.0
    spawn_time = 3.0

    def start(self):
        super().start()
        self.spawn_obstacle()

    def update(self):
        super().update()
        self.timer += Game.game.get_delta_time()
        if self.timer > self.spawn_time:
            self.timer = 0.0
            self.spawn_obstacle()

    def spawn_obstacle(self):
        size_y = 15.0
        f = random.uniform(0.1, 0.9)
        size1 = (f - self.gap) * 600
        size2 = (1 - f + self.gap) * 600
        pos1 = size1/2
        pos2 = size2/2 + (f+self.gap)*600

        img1 = pygame.Surface([size1, size_y])
        img1.fill([255, 0, 0])
        img2 = pygame.Surface([size2, size_y])
        img2.fill([255, 0, 0])

        o1 = GameObject(position=np.array([pos1, 0.0]), img=img1, components=[BoxCollider(), Enemy(1000)])
        o2 = GameObject(position=np.array([pos2, 0.0]), img=img2, components=[BoxCollider(), Enemy(1000)])
        Game.game.create_game_object(o1)
        Game.game.create_game_object(o2)

