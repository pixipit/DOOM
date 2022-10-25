import pygame

from Custum_Components.UI.menu_manager import MenuManager
from Custum_Components.character import Character
from Custum_Components.upgrade_ui_manager import UpgradeUIManager
from Custum_Components.weapon import Weapon
from game import Game


class Player(Character):
    speed = 300
    level = 0

    current_kills = 0
    kill_to_level_up = 5
    upgrade_manager = None
    upgrade_q = 1.05

    def __init__(self, max_health):
        self.max_health = max_health
        self.health = self.max_health

    def die(self):
        super().die()
        print("Dead")
        Game.game.find_by_name("MenuManager").get_component(MenuManager).show()

    def start(self):
        manager = Game.game.find_by_name('UpgradeManager')
        self.upgrade_manager = manager.get_component(UpgradeUIManager)

    def update(self):
        self.game_object.position[0] += self.speed * Game.game.speed * Game.game.input.val[0] * Game.game.get_delta_time()
        self.game_object.position[1] -= self.speed * Game.game.speed * Game.game.input.val[1] * Game.game.get_delta_time()

        self.game_object.position[1] = self.clamp(self.game_object.position[1], 0, 600)
        self.game_object.position[0] = self.clamp(self.game_object.position[0], 0, 600)

        if self.current_kills >= self.kill_to_level_up:
            self.current_kills = 0
            self.kill_to_level_up += 1
            Game.game.isPaused = True
            self.upgrade_manager.show()

    def upgrade_fire_rate(self, amount):
        weapons = self.game_object.get_components(Weapon)
        for weapon in weapons:
            weapon.fire_rate *= amount

    def upgrade_bullet_speed(self, amount):
        weapons = self.game_object.get_components(Weapon)
        for weapon in weapons:
            from Custum_Components.bullet import Bullet
            weapon.bullet.get_component(Bullet).speed *= amount

    @staticmethod
    def clamp(n, smallest, largest):
        return max(smallest, min(n, largest))
