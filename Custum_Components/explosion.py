import pygame

from Custum_Components.box_collider import BoxCollider
from Custum_Components.character import Character
from Custum_Components.player import Player
from component import Component
from game import Game


class Explosion(Component):
    def __init__(self, range: float, kill_tag: str):
        self.range = range
        self.kill_tag = kill_tag
        self.lifespan = 0.3
        self.timer = 0.0
        self.self_destruct = False
        self.exploded = False

    def start(self):
        self.game_object.size = [self.range, self.range]
        self.game_object.image = pygame.Surface([self.range, self.range])
        self.game_object.image.fill([255, 255, 255])
        self.game_object.rect = self.game_object.image.get_rect()
        box_collider = self.game_object.get_component(BoxCollider)
        box_collider.size = [self.range, self.range]
        box_collider.on_trigger_entry = self.hit
        self.game_object.rect.center = self.game_object.position

    def update(self):
        self.timer += Game.game.get_delta_time()
        if self.timer > self.lifespan/2.0:
            if self.self_destruct:
                self.game_object.destroy()
                return
            self.self_destruct = True
            self.timer = 0.0
            self.game_object.image = pygame.Surface([self.range, self.range])
            self.game_object.image.fill([0, 0, 0])
            self.game_object.rect = self.game_object.image.get_rect()

    def hit(self, x):
        if self.exploded:
            return
        if x.tag is not self.kill_tag:
            return
        self.exploded = True
        c = x.get_component(Character)
        dead = c.take_damage(1)
        if self.kill_tag is 'Enemy' and dead:
            p = Game.game.find_by_name('Player')
            if p is not None:
                p.get_component(Player).current_kills += 1
        self.game_object.destroy()


