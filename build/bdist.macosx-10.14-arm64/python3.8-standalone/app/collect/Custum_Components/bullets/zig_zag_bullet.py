from Custum_Components.bullet import Bullet
from game import Game


class ZigZagBullet(Bullet):
    timer = 0.0
    turn_time = 1.0
    
    def start(self):
        super().start()
        self.game_object.rotation = [1.0, -1.0]

    def update(self):
        super().update()
        self.timer += Game.game.get_delta_time()
        if self.timer > self.turn_time:
            self.timer = 0.0
            self.game_object.rotation = [-self.game_object.rotation[0], -1]
    