import copy
import numpy as np
import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, position=np.array([0.0, 0.0]),  img=pygame.Surface([0, 0]),
                 components=[], name=None, tag=None, rotation=[0.0, 1.0]):
        super().__init__()
        self.position = position
        self.components = []
        self.started = False
        self.dead = False
        self.name = name
        self.tag = tag
        self.rotation = rotation

        self.image: pygame.Surface = img
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.rect.center = self.position

        for component in components:
            self.add_component(component)

    def __deepcopy__(self, memodict={}):
        new_game_object = GameObject(copy.deepcopy(self.position), img=self.image,
                                     name=self.name, tag=self.tag, rotation=copy.deepcopy(self.rotation))
        for component in self.components:
            new_game_object.add_component(component.copy())
        return new_game_object

    def update(self):
        self.rect.center = [int(self.position[0]), int(self.position[1])]
        for component in self.components:
            component.update()

    def start(self):
        for component in self.components:
            component.start()

    def add_component(self, component):
        self.components.append(component)
        component.game_object = self

    def get_component(self, component_type):
        for component in self.components:
            if type(component) is component_type or issubclass(type(component), component_type):
                return component
        return None

    def get_components(self, component_type):
        components = []
        for component in self.components:
            if type(component) is component_type or issubclass(type(component), component_type):
                components.append(component)
        return components

    def destroy(self):
        self.dead = True
