import copy

from game_object import GameObject


class Component:
    game_object: GameObject = None

    def copy(self):
        g = copy.copy(self.game_object)
        self.game_object = None
        new_c = copy.deepcopy(self)
        self.game_object = g
        return new_c

    def start(self):
        pass

    def update(self):
        pass
