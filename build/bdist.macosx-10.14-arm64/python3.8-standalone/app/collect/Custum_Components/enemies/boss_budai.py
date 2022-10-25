from Custum_Components.enemy import Enemy


class BossBudai(Enemy):
    done = False

    def update(self):
        self.game_object.position[0] += self.game_object.rotation[0] * self.speed
        self.game_object.position[1] += self.game_object.rotation[1] * self.speed

        if self.game_object.position[1] > 100:
            if not self.done:
                self.game_object.rotation = [1.0, 0.0]
                self.done = True
            if self.game_object.position[0] < 100 or self.game_object.position[0] > 500:
                self.game_object.rotation[0] = -self.game_object.rotation[0]