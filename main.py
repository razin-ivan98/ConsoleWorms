from maps.map import map
from GameEngine import GameEngine

game = GameEngine(map)
worm = game.add_worm()
game.init_control(worm)
game.run()

