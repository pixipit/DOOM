import numpy as np

import user_interface
from Custum_Components.upgrade_ui_manager import UpgradeUIManager
from game import Game
from game_object import GameObject


class MenuManager(user_interface.UI):
    upgrade_manager: UpgradeUIManager = None
    ui = []
    info_ui = []
    active = False
    selected = 0
    info_mode = False

    def start(self):
        self.upgrade_manager = Game.game.find_by_name('UpgradeManager').get_component(UpgradeUIManager)
        self.show()

    def update(self):
        if Game.game.input.key_downs['escape'] and not self.upgrade_manager.active:
            if not Game.game.isPaused:
                self.show()

        if self.active:
            if self.info_mode:
                if Game.game.input.key_downs['space']:
                    for ui_element in self.info_ui:
                        ui_element.destroy()
                        self.info_mode = False
                return

            if Game.game.input.key_downs['w']:
                self.selected -= 1
            if Game.game.input.key_downs['s']:
                self.selected += 1
            self.selected = self.clamp(self.selected, 0, 2)

            position = np.array([300, 245 + 80 * self.selected])
            Game.game.find_by_name('selector').position = position

            if Game.game.input.key_downs['space']:
                if self.selected == 1:
                    from Custum_Components.the_creator import TheCreator
                    Game.game.find_by_name('TheCreator').get_component(TheCreator).restart()
                    self.hide()
                    Game.game.isPaused = False
                elif self.selected == 2:
                    self.info_mode = True
                    self.show_info()
                else:
                    self.hide()

    def hide(self):
        for ui_element in self.ui:
            ui_element.destroy()
        self.ui = []
        self.active = False
        Game.game.isPaused = False

    @staticmethod
    def clamp(n, smallest, largest):
        return max(smallest, min(n, largest))

    def show(self):
        position = [300.0, 220.0]
        back_ground1 = GameObject(position=position,
                                  components=[user_interface.UIElement([180, 50], [255, 255, 255], False)])
        text1 = GameObject(position=position,
                           components=[user_interface.UIText(text='continue', color=[0, 0, 0])])
        position = [300.0, 300.0]
        back_ground = GameObject(position=position,
                                 components=[user_interface.UIElement([180, 50], [255, 255, 255], False)])
        text = GameObject(position=position,
                          components=[user_interface.UIText(text='restart', color=[0, 0, 0])])

        text_info = GameObject(position=[300.0, 500.0],
                               components=[user_interface.UIText(text='(press space to confirm)', color=[0, 0, 0])])

        position = [300.0, 245.0]
        selector = GameObject(position=position,
                              components=[user_interface.UIElement([180, 10], [255, 0, 0], False)], name='selector')

        position = [300.0, 380.0]
        back_ground_extra = GameObject(position=position,
                                       components=[user_interface.UIElement([180, 50], [255, 255, 255], False)])
        text_extra = GameObject(position=position,
                                components=[user_interface.UIText(text='info', color=[0, 0, 0])])

        self.ui.append(Game.game.create_game_object(text_info))
        self.ui.append(Game.game.create_game_object(selector))
        self.ui.append(Game.game.create_game_object(back_ground))
        self.ui.append(Game.game.create_game_object(text))
        self.ui.append(Game.game.create_game_object(back_ground1))
        self.ui.append(Game.game.create_game_object(text1))
        self.ui.append(Game.game.create_game_object(back_ground_extra))
        self.ui.append(Game.game.create_game_object(text_extra))
        self.active = True
        Game.game.isPaused = True

    def show_info(self):
        position = [300.0, 300.0]
        back_ground = GameObject(position=position,
                                 components=[user_interface.UIElement([350, 250], [255, 255, 255], False)])
        text_1 = GameObject(position=[300.0, 200.0],
                            components=[user_interface.UIText(text='1. Use WASD to control everything',
                                                              color=[0, 0, 0], small=True)])
        text_2 = GameObject(position=[300.0, 220.0],
                            components=[
                                user_interface.UIText(text='2. by default every upgrade ugrades your stat by q=5%',
                                                      color=[0, 0, 0], small=True)])
        text_3 = GameObject(position=[300.0, 240.0],
                            components=[
                                user_interface.UIText(text='3. ^upgrades increases q by one 1%',
                                                      color=[0, 0, 0], small=True)])
        text_4 = GameObject(position=[300.0, 260.0],
                            components=[
                                user_interface.UIText(text='4. every difficulty makes the game 30% harder',
                                                      color=[0, 0, 0], small=True)])
        text_5 = GameObject(position=[300.0, 280.0],
                            components=[
                                user_interface.UIText(text='5. ESCAPE to pause the game',
                                                      color=[0, 0, 0], small=True)])
        position = [300.0, 450.0]
        text_extra = GameObject(position=position,
                                components=[user_interface.UIText(text='(press space to comeback)', color=[0, 0, 0])])
        self.info_ui.append(Game.game.create_game_object(back_ground))
        self.info_ui.append(Game.game.create_game_object(text_extra))
        self.info_ui.append(Game.game.create_game_object(text_1))
        self.info_ui.append(Game.game.create_game_object(text_2))
        self.info_ui.append(Game.game.create_game_object(text_3))
        self.info_ui.append(Game.game.create_game_object(text_4))
        self.info_ui.append(Game.game.create_game_object(text_5))
