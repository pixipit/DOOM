import copy
import random

import pygame.image

from Custum_Components.bullet_etalons import BulletEtalons
from Custum_Components.enemies.Zdenek import Zdenek
from Custum_Components.enemies.boss_budai import BossBudai
from Custum_Components.enemies.creeper import Creeper
from Custum_Components.enemies.klickova import Klickova
from Custum_Components.enemies.sykora import Sykora
from Custum_Components.weapon import Weapon
from game_object import GameObject
import numpy as np
from Custum_Components.box_collider import BoxCollider
from Custum_Components.enemy import Enemy
import Custum_Components.basic_enemy_weapon as enemy_weapons


def get_spawn_pos_basic_side():
    return np.array([random.choice([-100.0, 700.0]), random.uniform(200, 450)])


class EnemyEtalons:
    def __init__(self, speed, health_q):
        bullets = BulletEtalons().bullets

        jura_weapon = enemy_weapons.BasicWeapon(bullet=bullets["basic"], fire_rate=1.4 * speed)
        jura = GameObject(np.array([0.0, 0.0]),
                          components=[BoxCollider(), jura_weapon,
                                      Enemy(max_health=7 * health_q, speed=0.6 * speed)],
                          img=pygame.image.load('sprites/Jura.png'),
                          tag='Enemy')

        # Velich
        velich = GameObject(np.array([0.0, 0.0]),
                            components=[BoxCollider(), Enemy(max_health=1 * health_q, speed=speed)],
                            img=pygame.image.load('sprites/Velich.png'),
                            tag='Enemy')
        velich.get_component(Enemy).get_spawn_pos = lambda: np.array([-100, random.randrange(300, 550)])
        velich.rotation = [1, 0]

        velich2 = copy.deepcopy(velich)
        velich2.get_component(Enemy).get_spawn_pos = lambda: np.array([700, random.randrange(300, 550)])
        velich2.rotation = [-1, 0]

        lopocha = GameObject(np.array([0.0, 0.0]),
                            components=[BoxCollider(), Enemy(max_health=6 * health_q, speed=2 * speed)],
                            img=pygame.image.load('sprites/Lopocha.jpeg'),
                            tag='Enemy')

        # Hrabalova
        h_weapon = enemy_weapons.EnemyTripleWeapon(bullet=bullets["basic"], fire_rate=0.7 * speed)
        hrabalova = GameObject(np.array([0.0, 0.0]),
                               components=[BoxCollider(), Enemy(max_health=15 * health_q, speed=0.1 * speed), h_weapon],
                               img=pygame.image.load('sprites/Hrabalova.png'),
                               tag='Enemy')

        b_weapon1 = enemy_weapons.EnemyTripleWeapon(bullet=bullets["basic"], fire_rate=speed, offset=[60, 0])

        budai = GameObject(np.array([0.0, 0.0]),
                           components=[BoxCollider(),
                                       BossBudai(max_health=500 * health_q, speed=0.5 * speed, boss=True),
                                       b_weapon1],
                           img=pygame.image.load('sprites/budai.png'),
                           tag='Enemy')

        rasek_weapon = enemy_weapons.BasicWeapon(bullet=bullets["explosive"], fire_rate=0.4 * speed)
        rasek = GameObject(np.array([0.0, 0.0]),
                           components=[BoxCollider(), Enemy(max_health=7 * health_q, speed=0.5 * speed), rasek_weapon],
                           img=pygame.image.load('sprites/Rasek.png'),
                           tag='Enemy')

        herman_weapon = enemy_weapons.Weapon(bullet=bullets["zig_zag"], fire_rate=0.4 * speed)
        herman = GameObject(np.array([0.0, 0.0]),
                            components=[BoxCollider(), Enemy(max_health=7 * health_q, speed=0.5 * speed),
                                        herman_weapon],
                            img=pygame.image.load('sprites/Herman.png'),
                            tag='Enemy')

        jedlicka = GameObject(np.array([0.0, 0.0]),
                              components=[BoxCollider(), Creeper(max_health=15 * health_q, speed=1.0 * speed,
                                                                 get_spawn_pos=get_spawn_pos_basic_side)],
                              img=pygame.image.load('sprites/Jedlicka.png'),
                              tag='Enemy')

        klickova = GameObject(np.array([0.0, 0.0]),
                              components=[BoxCollider(),
                                          Klickova(max_health=400 * health_q, speed=1.0 * speed, boss=True)],
                              img=pygame.image.load('sprites/Jedlicka.png'),
                              tag='Enemy')
        zdenda_weapon = enemy_weapons.BasicWeapon(bullet=bullets["basic"], fire_rate=1.4 * speed)
        zdenda = GameObject(np.array([0.0, 0.0]),
                            components=[BoxCollider(), Zdenek(max_health=200 * health_q, speed=1.0 * speed, boss=True),
                                        zdenda_weapon],
                            img=pygame.image.load('sprites/Zdenek.png'),
                            tag='Enemy')

        sykora = GameObject(np.array([0.0, 0.0]),
                            components=[BoxCollider(), Sykora(max_health=300 * health_q, speed=1.0 * speed, boss=True)],
                            img=pygame.image.load('sprites/Sykora.png'),
                            tag='Enemy')

        vondra_weapon1 = Weapon(bullet=bullets["basic"], fire_rate=1.0 * speed, direction=[0.0, -1.0])
        vondra_weapon2 = Weapon(bullet=bullets["basic"], fire_rate=1.0 * speed, direction=[1.0, -1.0])
        vondra_weapon3 = Weapon(bullet=bullets["basic"], fire_rate=1.0 * speed, direction=[-1.0, -1.0])

        vondra_ = GameObject(np.array([0.0, 0.0]),
                             components=[BoxCollider(), Enemy(max_health=4 * health_q, speed=0.5 * speed),
                                         vondra_weapon1, vondra_weapon2, vondra_weapon3],
                             img=pygame.image.load('sprites/Vondra.png'),
                             tag='Enemy')

        self.enemies = {
            "Jura": jura,
            "Velich": velich,
            "Velich2": velich2,
            "Vondra": vondra_,
            "Hrabalova": hrabalova,
            "budai": budai,
            "Rasek": rasek,
            "Herman": herman,
            "Jedlicka": jedlicka,
            "Zdenda": zdenda,
            "Sykora": sykora,
            "Klickova": klickova,
            "Zelenka": None,
            "Studenkova": None,
            "Lopocha": lopocha
        }
