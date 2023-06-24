from lib import game
from lib import story

story = story.load_story('game/game.yaml')
game = game.Game(story)

game.play()
