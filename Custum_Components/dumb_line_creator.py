import pygame

from Custum_Components.EnemyManager import EnemyManager
import user_interface
from game import Game
from game_object import GameObject


class DumbLineCreator(user_interface.Component):
    def start(self):
        e = Game.game.find_by_name("Enemy_Manager")
        if e is None:
            return
        e_c: EnemyManager = e.get_component(EnemyManager)

        total_amount = 0
        for wave in e_c.current_level.enemy_wave_list:
            total_amount += len(wave.line)

        line_count = len(e_c.current_level.enemy_wave_list) - 1
        total_count = 0.0
        for i in range(line_count):
            l = len(e_c.current_level.enemy_wave_list[i].line)
            x_pos = ((l + total_count)/total_amount) * self.game_object.size[0] + self.game_object.position[0]
            line = GameObject([x_pos, self.game_object.position[1] - 5],
                              components=[user_interface.UIElement([3, 20], [0, 0, 0])])
            Game.game.create_game_object(line)
            total_count += l
