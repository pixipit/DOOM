import pygame

from Custum_Components.box_collider import BoxCollider
from Custum_Components.bullet import Bullet
from Custum_Components.bullets.explosive_bullet import ExplosiveBullet
from Custum_Components.bullets.zig_zag_bullet import ZigZagBullet
from game_object import GameObject


class BulletEtalons:
    def __init__(self):
        b_img = pygame.Surface([10, 10])
        b_img.fill([255, 100, 100])
        bullet = GameObject([0.0, 0.0], b_img,
                            [Bullet('Player', speed=2), BoxCollider()])

        zig_zag_img = pygame.Surface([10, 10])
        zig_zag_img.fill([255, 127, 0])
        zig_zag_bullet = GameObject([0.0, 0.0], zig_zag_img,
                            [ZigZagBullet('Player', speed=2), BoxCollider()])

        explosive_bullet_img = pygame.Surface([10, 10])
        explosive_bullet_img.fill([255, 255, 100])
        explosive_bullet = GameObject([0.0, 0.0], explosive_bullet_img,
                                      [ExplosiveBullet('Player', speed=2), BoxCollider()])

        self.bullets = {
            "basic": bullet,
            "explosive": explosive_bullet,
            "zig_zag": zig_zag_bullet
        }
