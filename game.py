import pygame

from game_object import GameObject
from input_module import Input
from collision_engine import CollisionEngine
import copy

import user_interface


class Game:
    game = None

    def __init__(self, width, height, fps=60):
        pygame.init()
        pygame.font.init()

        Game.game = self
        self.debug_colliders = False
        self.speed = 1.0
        self.level = 1
        self.isPaused = False

        is_initialized = pygame.get_init()

        # printing the result
        print('Is pygame modules initialized:',
              is_initialized)

        self.window = pygame.display.set_mode((width, height))
        # creating a bool value which checks
        # if game is running
        self.running = True
        self.game_objects = []
        self.events = None
        self.input = Input()
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.collision_engine = CollisionEngine(self.game_objects, self.debug_colliders, self.window)
        self.sprite_group = pygame.sprite.Group()
        self.ui_elements_group = pygame.sprite.Group()

    def run(self):
        while self.running:
            self.clock.tick(self.fps)
            self.events = pygame.event.get()
            self.window.fill((200, 200, 200))
            self.input.update(self.events)
            # print(len(self.game_objects))
            # print(self.clock.get_fps())

            # update game_objects
            for game_object in self.game_objects:
                is_game_object_ui: bool = game_object.get_component(user_interface.UI) is not None
                if game_object.dead:
                    self.game_objects.remove(game_object)
                    if is_game_object_ui:
                        self.ui_elements_group.remove(game_object)
                    else:
                        self.sprite_group.remove(game_object)
                    continue

                if not game_object.started:
                    game_object.start()
                    game_object.started = True

                if not self.isPaused or is_game_object_ui:
                    game_object.update()

            self.sprite_group.draw(self.window)
            self.ui_elements_group.draw(self.window)

            self.collision_engine.update()

            # Draws the surface object to the screen.
            pygame.display.update()
            # Check for event if user has pushed
            for event in self.events:
                # if event is of type quit then
                # set running bool to false
                if event.type == pygame.QUIT:
                    self.running = False

    def get_delta_time(self):
        return 1 / self.fps

    def create_game_object(self, game_object: GameObject, position=None, rotation=None) -> GameObject:
        g = copy.deepcopy(game_object)
        # g = game_object
        self.game_objects.append(g)
        if game_object.get_component(user_interface.UI) is not None:
            self.ui_elements_group.add(g)
        else:
            self.sprite_group.add(g)

        if position is not None:
            g.position = copy.deepcopy(position)
        if rotation is not None:
            g.rotation = copy.deepcopy(rotation)
        return g

    @staticmethod
    def find_by_name(g_name: str) -> GameObject:
        for game_object in Game.game.game_objects:
            if game_object.name is not None and game_object.name is g_name:
                return game_object
        return None

    @staticmethod
    def find_by_tag(g_name: str) -> GameObject:
        game_objects = []
        for game_object in Game.game.game_objects:
            if game_object.tag is not None and game_object.tag is g_name:
                game_objects.append(game_object)
        return game_objects
