import random

import numpy as np

import user_interface
from game import Game
from game_object import GameObject


def upgrade_health(amount, player):
    f = player.health/player.max_health
    player.max_health *= amount
    player.health = player.max_health * f


def upgrade_attack_speed(amount, player):
    player.upgrade_fire_rate(amount)


def upgrade_bullet_speed(amount, player):
    player.upgrade_bullet_speed(amount)


def upgrade_speed(amount, player):
    player.speed *= amount


def upgrade_q(amount, player):
    player.upgrade_q += 0.01


def heal(amount, player):
    player.health = player.max_health


class UpgradeUIManager(user_interface.UI):
    player = None
    current_upgradesUI = []
    current_upgrades_backgrounds = []
    active = False
    selectorUI = None
    selected = 1
    n_of_upgrades = 3
    current_upgrades = []

    upgrades = {
        "attack speed": upgrade_attack_speed,
        "max health": upgrade_health,
        "speed": upgrade_speed,
        "heal": heal,
        "bullet speed": upgrade_bullet_speed,
        "^upgrades": upgrade_q
    }

    @staticmethod
    def clamp(n, smallest, largest):
        return max(smallest, min(n, largest))

    def start(self):
        from Custum_Components.player import Player
        self.player = Game.game.find_by_name('Player').get_component(Player)

    def update(self):
        if not self.active:
            return
        if Game.game.input.key_downs['a']:
            self.selected -= 1
        if Game.game.input.key_downs['d']:
            self.selected += 1
        self.selected = self.clamp(self.selected, 0, self.n_of_upgrades - 1)

        position = np.array([100 + 200 * self.selected, 330])
        Game.game.find_by_name('selector').position = position

        if Game.game.input.key_downs['space'] != 0:
            upgrade = self.upgrades[self.current_upgrades[self.selected]]
            upgrade(self.player.upgrade_q, self.player)
            self.active = False
            self.hide()
            Game.game.find_by_name('selector').destroy()
            Game.game.isPaused = False

    def hide(self):
        for i in range(self.n_of_upgrades):
            self.current_upgrades_backgrounds[i].destroy()
            self.current_upgradesUI[i].destroy()
        self.current_upgrades_backgrounds = []
        self.current_upgradesUI = []
        self.selectorUI = None

    def show(self):
        self.current_upgrades = random.sample(list(self.upgrades), self.n_of_upgrades)
        self.active = True
        for i in range(self.n_of_upgrades):
            position = np.array([100 + 200 * i, 300])
            back_ground = GameObject(position=position,
                                     components=[user_interface.UIElement([180, 50], [255, 255, 255], False)])
            text = GameObject(position=position,
                              components=[user_interface.UIText(text=self.current_upgrades[i], color=[0, 0, 0])])
            self.current_upgrades_backgrounds.append(Game.game.create_game_object(back_ground))
            self.current_upgradesUI.append(Game.game.create_game_object(text))

        position = np.array([300, 500])
        selector = GameObject(position=position,
                              components=[user_interface.UIElement([180, 10], [255, 0, 0], False)], name='selector')
        # Game.game.create_game_object(selector)
        # self.selectorUI = Game.game.create_game_object(selector)
        Game.game.create_game_object(selector)
        # self.selectorUI = Game.game.find_by_name('selector')
        self.selected = 1
