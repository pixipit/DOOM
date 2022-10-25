from Custum_Components.bullet_etalons import BulletEtalons
from Custum_Components.enemies.boss_budai import BossBudai
from Custum_Components.weapon import Weapon
from game import Game
from game_object import GameObject


class Klickova(BossBudai):
    def start(self):
        bullet = BulletEtalons().bullets["basic"]
        bullet.rotation = [0.0, -1.0]
        weapons = [Weapon(bullet, 0.6, [0.0, 0.0]),
                   Weapon(bullet, 0.6, [100.0, 0.0]),
                   Weapon(bullet, 0.6, [200.0, 0.0]),
                   Weapon(bullet, 0.6, [-100.0, 0.0]),
                   Weapon(bullet, 0.6, [-200.0, 0.0])]

        guns = GameObject(position=[300.0, -10.0], components=weapons, name='guns')
        Game.game.create_game_object(guns)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()
            Game.game.find_by_name('guns').destroy()
            return True
        return False
