from game import Game
from game_object import GameObject
import numpy as np
from Custum_Components.the_creator import TheCreator

my_game = Game(600, 600)

position = [250, -100]
god_game_object = GameObject(np.array(position), name='TheCreator')
p = TheCreator()
god_game_object.game = my_game
god_game_object.add_component(p)

Game.game.create_game_object(god_game_object)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_game.run()
