import game
import sys

if len(sys.argv) == 1:
    source = game.import_file('words')
else:
    source = game.import_file(sys.argv[1])

run = game.Game(source)
run.game()
