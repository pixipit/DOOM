import pygame

from Custum_Components.box_collider import BoxCollider


class CollisionEngine:
    def __init__(self, game_objects, debug: bool, window=None):
        self.game_objects = game_objects
        self.debug: bool = debug
        self.window = window

    def update(self):
        colliders = []
        for game_object in self.game_objects:
            if game_object.get_component(BoxCollider) is not None:
                colliders.append(game_object.get_component(BoxCollider))

        if self.debug and self.window is not None:
            for collider in colliders:
                position = [collider.game_object.position[0] + collider.offset[0],
                            collider.game_object.position[1] + collider.offset[1]]
                pygame.draw.rect(self.window, (0, 255, 0),
                                 [position[0], position[1], collider.size[0], collider.size[1]], 2)

        for colliderA in colliders:
            for colliderB in colliders:
                if colliderB is colliderA:
                    continue

                position_a = [colliderA.game_object.position[0] + colliderA.offset[0],
                              colliderA.game_object.position[1] + colliderA.offset[1]]
                position_b = [colliderB.game_object.position[0] + colliderB.offset[0],
                              colliderB.game_object.position[1] + colliderB.offset[1]]

                if position_b[0] < position_a[0] + colliderA.size[0] and \
                        position_a[0] < position_b[0] + colliderB.size[0] and \
                        position_b[1] < position_a[1] + colliderA.size[1] and \
                        position_a[1] < colliderB.size[1] + position_b[1]:
                    if colliderA.on_trigger_entry is not None:
                        colliderA.on_trigger_entry(colliderB.game_object)
