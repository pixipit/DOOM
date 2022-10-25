from Custum_Components.weapon import Weapon
from game import Game
import numpy as np


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)


class BasicWeapon(Weapon):
    def shoot(self):
        if Game.find_by_name('Player') is None:
            return
        player_pos = Game.find_by_name('Player').position
        dir = self.game_object.position - player_pos
        normalized_dir = unit_vector(dir)
        Game.game.create_game_object(self.bullet, self.game_object.position + self.offset, rotation=normalized_dir)


class EnemyTripleWeapon(Weapon):
    def shoot(self):
        if Game.find_by_name('Player') is None:
            return
        player_pos = Game.find_by_name('Player').position
        dir = self.game_object.position - player_pos
        normalized_dir = unit_vector(dir)
        dir2 = np.array([-normalized_dir[1], normalized_dir[0]]) + normalized_dir
        dir3 = np.array([normalized_dir[1], -normalized_dir[0]]) + normalized_dir
        Game.game.create_game_object(self.bullet, self.game_object.position, rotation=normalized_dir)
        Game.game.create_game_object(self.bullet, self.game_object.position, rotation=unit_vector(dir2))
        Game.game.create_game_object(self.bullet, self.game_object.position, rotation=unit_vector(dir3))


class EnemySimpleTripleWeapon(Weapon):
    def shoot(self):
        if Game.find_by_name('Player') is None:
            return
        normalized_dir = [0, -1]
        dir2 = np.array([-normalized_dir[1], normalized_dir[0]]) + normalized_dir
        dir3 = np.array([normalized_dir[1], -normalized_dir[0]]) + normalized_dir
        Game.game.create_game_object(self.bullet, self.game_object.position + self.offset, rotation=normalized_dir)
        Game.game.create_game_object(self.bullet, self.game_object.position + self.offset, rotation=unit_vector(dir2))
        Game.game.create_game_object(self.bullet, self.game_object.position + self.offset, rotation=unit_vector(dir3))

