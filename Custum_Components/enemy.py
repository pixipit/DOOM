import random

import numpy as np

from Custum_Components.box_collider import BoxCollider
from Custum_Components.character import Character


def get_spawn_pos_basic():
    return np.array([random.uniform(100, 500), -30.0])


class Enemy(Character):
    def __init__(self, max_health=5, speed=1, get_spawn_pos=get_spawn_pos_basic, boss=False):
        self.speed = speed
        self.max_health = max_health
        self.health = max_health
        self.get_spawn_pos = get_spawn_pos
        self.boss = boss

    def t(self, x):
        if x.tag == 'Player':
            if not self.boss:
                x.get_component(Character).take_damage(1)
                self.game_object.dead = True
            else:
                x.get_component(Character).take_damage(100)

    def start(self):
        self.game_object.get_component(BoxCollider).on_trigger_entry = self.t

    def update(self):
        self.game_object.position[0] += self.game_object.rotation[0] * self.speed
        self.game_object.position[1] += self.game_object.rotation[1] * self.speed
