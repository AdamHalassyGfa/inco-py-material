from lib import game

story = game.load_story('game/game.yaml')
game = game.Game(story)

print(game)
