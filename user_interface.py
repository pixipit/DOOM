import pygame

from component import Component


class UI(Component):
    pass


class UIElement(UI):

    def __init__(self, size, color=[255, 255, 255], center=True):
        self.size = size
        self.color = color
        self.center = center

    def start(self):
        self.game_object.size = self.size
        self.game_object.image = pygame.Surface([self.size[0], self.size[1]])
        self.game_object.image.fill(self.color)
        self.game_object.rect = self.game_object.image.get_rect()

    def update(self):
        if self.center:
            self.game_object.rect.topleft = [int(self.game_object.position[0]), int(self.game_object.position[1])]


class UIText(UI):
    font_basic = None
    font_small = None

    def __init__(self, text, color=[255, 255, 255], center=True, getter=None, small=False):
        if UIText.font_basic is None:
            UIText.font_basic = pygame.font.SysFont('chalkduster.ttf', 30)
            UIText.font_small = pygame.font.SysFont('chalkduster.ttf', 20)
        self.text = text
        self.color = color
        self.getter = getter
        self.small = small

    def set_text(self, text):
        self.text = text
        if self.small:
            self.game_object.image = UIText.font_small.render(self.text, True, self.color)
        else:
            self.game_object.image = UIText.font_basic.render(self.text, True, self.color)
        self.game_object.rect = self.game_object.image.get_rect()
        self.game_object.rect.topleft = self.game_object.position

    def start(self):
        self.set_text(self.text)

    def update(self):
        if self.getter is None:
            return
        self.set_text(self.getter())


class Filler(UIElement):
    def __init__(self, size, color=[255, 255, 255], getter=None):
        super(Filler, self).__init__(size, color)
        self.getter = getter

    def set_value(self, val):
        self.game_object.image = pygame.Surface([self.size[0] * val, self.size[1]])
        self.game_object.image.fill(self.color)
        self.game_object.rect = self.game_object.image.get_rect()
        self.game_object.rect.topleft = self.game_object.position

    def update(self):
        if self.getter is None:
            return
        self.set_value(self.getter())


