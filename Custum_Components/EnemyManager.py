from Custum_Components.enemy import Enemy
from Custum_Components.player import Player
from component import Component
import numpy as np
from game import Game
import random

from user_interface import UIText


class Level:
    def __init__(self, enemy_wave_list: list):
        self.enemy_wave_list: list = enemy_wave_list
        self.wave_count = 0
        self.current_wave: Wave = self.enemy_wave_list[0]
        self.finished: bool = False
        self.delay_wave_gap = 5
        self.wait = False
        self.wave_delay_timer = 0.0

    def update(self):
        if self.finished:
            return

        if self.wait:
            self.wait_gap()

        if self.current_wave.finished:
            self.wave_count += 1
            if self.wave_count == len(self.enemy_wave_list):
                self.finished = True
                return
            self.current_wave = self.enemy_wave_list[self.wave_count]
            self.wait = True
            return
        self.current_wave.update()

    def wait_gap(self):
        self.wave_delay_timer += Game.game.get_delta_time()
        if self.wave_delay_timer < self.delay_wave_gap:
            return
        self.wave_delay_timer = 0.0
        self.wait = False


class Wave:
    def __init__(self, enemy_arr: list, delay_range: list = [1.0, 2.0]):
        self.count: int = 0
        self.line: list = []
        self.delay_range = delay_range
        self.timer = 0.0
        self.finished = False

        self.current_delay = random.uniform(self.delay_range[0], self.delay_range[1])
        for enemy in enemy_arr:
            for i in range(enemy[1]):
                self.line.append(enemy[0])
        random.shuffle(self.line)

    def update(self):
        if self.finished:
            return
        self.timer += Game.game.get_delta_time()
        if self.timer > self.current_delay:
            self.timer = 0
            self.current_delay = random.uniform(self.delay_range[0], self.delay_range[1])
            return self.spawn_next()

    def get_next_enemy(self):
        if self.count == len(self.line) or self.finished:
            return None
        enemy = self.line[self.count]
        self.count += 1
        return enemy

    def spawn_next(self):
        current_enemy = self.get_next_enemy()
        if current_enemy is None:
            self.finished = True
            return
        enemy_c = current_enemy.get_component(Enemy)
        Game.game.create_game_object(current_enemy, enemy_c.get_spawn_pos())


class EnemyManager(Component):
    timer = 0.0
    current_delay = 0

    def __init__(self, level_list: list):
        self.level_list: list = level_list
        self.level_count = 0
        self.current_level: Level = self.level_list[0]
        self.finished: bool = False
        self.delay_level_gap = 5
        self.wait = False
        self.level_delay_timer = 0.0

    def update(self):
        if self.finished:
            return

        if self.wait:
            self.wait_gap()

        if self.current_level.finished:
            self.level_count += 1
            Game.game.find_by_name('level_text').get_component(UIText).set_text('ročník=' + str(self.level_count + 1))
            if self.level_count == len(self.level_list):
                self.finished = True
                return
            self.current_level = self.level_list[self.level_count]
            self.wait = True
            return
        self.current_level.update()

    def wait_gap(self):
        self.level_delay_timer += Game.game.get_delta_time()
        if self.level_delay_timer < self.delay_level_gap:
            return
        self.level_delay_timer = 0.0
        self.wait = False
