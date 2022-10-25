import numpy as np

from Custum_Components.box_collider import BoxCollider
from Custum_Components.bullet import Bullet
from Custum_Components.explosion import Explosion
from game import Game
from game_object import GameObject


class ExplosiveBullet(Bullet):
    position = None
    offset = [10.0, 10.0]

    def start(self):
        super().start()
        self.position = np.array(Game.game.find_by_name('Player').position)
        
    def update(self):
        super().update()
        p = self.game_object.position - self.position
        if abs(p[0]) < self.offset[0] and abs(p[1]) < self.offset[1]:
            self.game_object.destroy()
            explosion = GameObject(position=self.position, components=[Explosion(100, self.kill_tag), BoxCollider()])
            Game.game.create_game_object(explosion)
