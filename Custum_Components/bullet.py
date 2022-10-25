from Custum_Components.player import Player
from component import Component
from Custum_Components.box_collider import BoxCollider
from Custum_Components.character import Character

from game import Game


class Bullet(Component):
    def __init__(self, kill_tag, speed=4):
        self.kill_tag = kill_tag
        self.speed = speed

    def t(self, x):
        if x.tag is not self.kill_tag:
            return
        c = x.get_component(Character)
        dead = c.take_damage(1)
        if self.kill_tag is 'Enemy' and dead:
            p = Game.game.find_by_name('Player')
            if p is not None:
                p.get_component(Player).current_kills += 1
        self.game_object.destroy()

    def start(self):
        self.game_object.get_component(BoxCollider).on_trigger_entry = self.t

    def update(self):
        self.game_object.position[0] -= self.game_object.rotation[0] * self.speed * Game.game.speed
        self.game_object.position[1] -= self.game_object.rotation[1] * self.speed * Game.game.speed
