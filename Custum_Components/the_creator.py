import pygame.image

from Custum_Components.UI.menu_manager import MenuManager
from Custum_Components.dumb_line_creator import DumbLineCreator
from Custum_Components.level_holder import LevelHolder
from Custum_Components.upgrade_ui_manager import UpgradeUIManager
from component import Component
from game_object import GameObject
import numpy as np
from Custum_Components.player import Player
from Custum_Components.box_collider import BoxCollider
from Custum_Components.EnemyManager import EnemyManager
from Custum_Components.weapon import Weapon
from game import Game
from user_interface import UIElement, UIText, Filler


def get_player_health() -> str:
    p_g = Game.game.find_by_name('Player')
    if p_g is None:
        return '0/0'
    p = p_g.get_component(Player)
    if p.health < 0:
        return '0/0'
    return "{:.1f}".format(p.health) + '/' + "{:.1f}".format(p.max_health)


def get_player_speed() -> str:
    p_g = Game.game.find_by_name('Player')
    if p_g is None:
        return 'speed: 0'
    return 'speed: ' + "{:.1f}".format(p_g.get_component(Player).speed / 300)


def get_player_attack_speed() -> str:
    p_g = Game.game.find_by_name('Player')
    if p_g is None:
        return 'bullets/s: 0'
    return 'bullets/s: ' + "{:.1f}".format(p_g.get_component(Weapon).fire_rate)


def get_player_bullet_speed() -> str:
    p_g = Game.game.find_by_name('Player')
    if p_g is None:
        return 'blt_spd: 0'
    from Custum_Components.bullet import Bullet
    return 'blt_spd: ' + "{:.1f}".format(p_g.get_component(Weapon).bullet.get_component(Bullet).speed)


def get_player_q() -> str:
    p_g = Game.game.find_by_name('Player')
    if p_g is None:
        return 'q: 0'
    return 'q: ' + "{:.0f}".format((p_g.get_component(Player).upgrade_q - 1) * 100) + '%'


def get_player_health_percent() -> float:
    p_g = Game.game.find_by_name('Player')
    if p_g is None:
        return 0.0
    p = p_g.get_component(Player)
    if p.health < 0:
        return 0
    return p.health / p.max_health


def get_player_level_percent() -> float:
    p_g = Game.game.find_by_name('Player')
    if p_g is None:
        return 0.0
    p: Player = p_g.get_component(Player)
    return p.current_kills / p.kill_to_level_up


class TheCreator(Component):
    enemy_manager: GameObject = None
    e_c: EnemyManager = None
    upgrade_manager: UpgradeUIManager = None

    def d(self, x):
        if x.tag == 'Wall':
            return
        if x.tag == 'Player':
            x.get_component(Player).die()
            return
        x.destroy()

    def restart(self):
        self.enemy_manager.destroy()
        enemies = Game.game.find_by_tag('Enemy')
        for enemy in enemies:
            enemy.destroy()

        Game.game.speed = 1.0
        self.enemy_manager = self.create_enemy_manager()
        self.e_c: EnemyManager = self.enemy_manager.get_component(EnemyManager)
        Game.game.level = 1
        Game.game.find_by_name("level_text").get_component(UIText).set_text('ročník=' + str(Game.game.level))

        p = Game.game.find_by_name('Player')
        if p is not None:
            p.destroy()
        self.create_player()
        new_player = Game.game.find_by_name('Player').get_component(Player)
        Game.game.find_by_name('UpgradeManager').get_component(UpgradeUIManager).player = new_player

    def start_new_level(self):
        Game.game.speed *= 1.3
        self.enemy_manager = self.create_enemy_manager()
        self.e_c: EnemyManager = self.enemy_manager.get_component(EnemyManager)
        Game.game.level += 1
        Game.game.find_by_name("difficulty_text").get_component(UIText).set_text('difficulty=' + str(Game.game.level))
        Game.game.find_by_name('level_text').get_component(UIText).set_text('ročník=1')

    def update(self):
        if self.e_c.finished:
            enemies = Game.game.find_by_tag('Enemy')
            if len(enemies) > 0:
                return
            self.enemy_manager.destroy()
            self.start_new_level()

    def create_walls(self):
        # wall horizontal
        wall_offset = 300
        position = [0, 0]
        img = pygame.Surface([Game.game.window.get_size()[0] + wall_offset * 2, 20])
        img.fill([0, 0, 0])
        wall = GameObject(np.array(position), img, [BoxCollider(img.get_rect().size)], tag='Wall')
        wall.get_component(BoxCollider).on_trigger_entry = self.d
        # wall vertical
        position = [0, 0]
        img = pygame.Surface([20, Game.game.window.get_size()[0] + 80])
        img.fill([0, 0, 0])
        wall2 = GameObject(np.array(position), img, [BoxCollider(img.get_rect().size)], tag='Wall')
        wall2.get_component(BoxCollider).on_trigger_entry = self.d

        Game.game.create_game_object(wall, position=np.array([0, -wall_offset]))
        Game.game.create_game_object(wall, position=np.array([0, 600 + wall_offset]))
        Game.game.create_game_object(wall2, position=np.array([-wall_offset, 0]))
        Game.game.create_game_object(wall2, position=np.array([600 + wall_offset, 0]))

    @staticmethod
    def create_info_text():
        hp_text = GameObject(position=np.array([300, 532]),
                             components=[UIText('', color=[0, 0, 0], getter=get_player_health, center=True)])
        speed_text = GameObject(position=np.array([15, 562]),
                                components=[UIText('', color=[0, 0, 0], getter=get_player_speed)])
        attack_speed_text = GameObject(position=np.array([15, 532]),
                                       components=[UIText('', color=[0, 0, 0], getter=get_player_attack_speed)])
        bullet_speed_text = GameObject(position=np.array([420, 532]),
                                       components=[UIText('', color=[0, 0, 0], getter=get_player_bullet_speed)])
        q_text = GameObject(position=np.array([420, 562]),
                            components=[UIText('', color=[0, 0, 0], getter=get_player_q)])
        Game.game.create_game_object(hp_text)
        Game.game.create_game_object(attack_speed_text)
        Game.game.create_game_object(speed_text)
        Game.game.create_game_object(bullet_speed_text)
        Game.game.create_game_object(q_text)

    def start(self):
        self.create_walls()
        # UI
        back_ground = GameObject(position=np.array([200, 530]), components=[UIElement([200, 30], [255, 0, 0])])
        getter = get_player_health_percent
        fill = GameObject(position=np.array([200, 530]), components=[Filler([200, 30], [0, 255, 0], getter)])

        player_level_back_ground = GameObject(position=np.array([200, 560]),
                                              components=[UIElement([200, 30], [100, 100, 100])])
        player_level_getter = get_player_level_percent
        player_level_fill = GameObject(position=np.array([200, 560]),
                                       components=[Filler([200, 30], [0, 0, 150], player_level_getter)])

        difficulty_text = GameObject(position=np.array([500, 30]),
                                     components=[UIText('difficulty=1', color=[255, 0, 0])], name='difficulty_text')
        level_text = GameObject(position=np.array([70, 30]),
                                components=[UIText('ročník=1', color=[255, 0, 0])], name='level_text')

        self.create_wave_bar()

        manager: GameObject = Game.game.create_game_object(GameObject([0.0, 0.0], components=[UpgradeUIManager()],
                                                                      name='UpgradeManager'))

        Game.game.create_game_object(difficulty_text)
        Game.game.create_game_object(level_text)
        Game.game.create_game_object(back_ground)
        Game.game.create_game_object(fill)
        Game.game.create_game_object(player_level_back_ground)
        Game.game.create_game_object(player_level_fill)
        self.create_player()
        self.create_info_text()

        self.enemy_manager = self.create_enemy_manager()
        self.e_c: EnemyManager = self.enemy_manager.get_component(EnemyManager)
        Game.game.create_game_object(GameObject([0.0, 0.0], components=[MenuManager()], name='MenuManager'))

    @staticmethod
    def create_enemy_manager():
        enemy_manager = GameObject(np.array([0, 700]),
                                   components=[EnemyManager(LevelHolder.get_levels())],
                                   name='Enemy_Manager')
        return Game.game.create_game_object(enemy_manager)

    @staticmethod
    def create_player():
        position = [250, 400]

        p = Player(4)
        b_img = pygame.Surface([10, 10])
        b_img.fill([100, 255, 100])
        from Custum_Components.bullet import Bullet
        bullet = GameObject([0.0, 0.0], b_img,
                            [Bullet('Enemy', speed=6), BoxCollider()])

        players_weapon0 = Weapon(bullet=bullet, fire_rate=2, offset=[-20, 0])
        players_weapon1 = Weapon(bullet=bullet, fire_rate=2, offset=[20, 0])
        players_weapon2 = Weapon(bullet=bullet, fire_rate=2, offset=[0, 0])

        player = GameObject(np.array(position), pygame.image.load('sprites/peeter.jpeg'),
                            components=[players_weapon0, players_weapon1, players_weapon2, p, BoxCollider()],
                            name="Player", tag='Player')
        Game.game.create_game_object(player)

    @staticmethod
    def create_wave_bar():
        def getter():
            e = Game.game.find_by_name("Enemy_Manager")
            if e is None:
                return 1
            e_c: EnemyManager = e.get_component(EnemyManager)
            total_amount = 0
            finish_amount = 0
            b = False
            for wave in e_c.current_level.enemy_wave_list:
                total_amount += len(wave.line)
                if e_c.current_level.current_wave == wave:
                    b = True
                    finish_amount += e_c.current_level.current_wave.count
                if not b:
                    finish_amount += len(wave.line)

            return finish_amount / total_amount

        back_ground = GameObject(position=np.array([150, 30]), components=[UIElement([250, 10], [50, 50, 50])])
        fill = GameObject(position=np.array([150, 30]), components=[Filler([250, 10], [150, 0, 0], getter),
                                                                    DumbLineCreator()])
        Game.game.create_game_object(back_ground)
        Game.game.create_game_object(fill)
