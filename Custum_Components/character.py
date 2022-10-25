from component import Component


class Character(Component):
    max_health = 0
    health = 0

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()
            return True
        return False

    def die(self):
        self.game_object.destroy()
