import numpy as np
import pygame

from Custum_Components.box_collider import BoxCollider
from Custum_Components.enemy import Enemy
from Custum_Components.explosion import Explosion
from game import Game
from game_object import GameObject


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)


class Creeper(Enemy):
    player: GameObject = None
    offset = [100.0, 100.0]
    creep = False
    timer = 0.0
    swap_timer = 0.0
    creep_time = 1.0
    swapped = False

    def start(self):
        self.player = Game.game.find_by_name('Player')

    def update(self):
        if self.player is None:
            return

        if self.creep:
            self.timer += Game.game.get_delta_time()
            self.swap_timer += Game.game.get_delta_time()

            if self.swap_timer > self.creep_time/7:
                self.swap(self.swapped)
                self.swapped = not self.swapped
                self.swap_timer = 0.0

            if self.timer > self.creep_time:
                self.game_object.destroy()
                explosion = GameObject(position=np.copy(self.game_object.position),
                                       components=[Explosion(200, 'Player'), BoxCollider()])
                Game.game.create_game_object(explosion)
            return

        p = self.game_object.position - self.player.position
        if abs(p[0]) < self.offset[0] and abs(p[1]) < self.offset[1]:
            self.creep = True
            return

        dir = self.player.position - self.game_object.position
        normalized_dir = unit_vector(dir)
        self.game_object.rotation = normalized_dir
        super().update()

    def swap(self, swapped):
        if not swapped:
            self.game_object.image = pygame.image.load('sprites/Jedlicka2.png')
        else:
            self.game_object.image = pygame.image.load('sprites/Jedlicka.png')
        self.game_object.rect = self.game_object.image.get_rect()
        self.game_object.rect.center = self.game_object.position
