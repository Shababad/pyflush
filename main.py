from pyflush import Game

# Create a game instance
game = Game()

# Adds a player to the game
game.add_player("Chai", 10000)

# Adds bots to the game
game.add_bot("Bob", 10000)
game.add_bot("Tom", 10000)
game.add_bot("Max", 10000)

# Removes player/bot by name
game.remove("Max")

# Sets big blind
game.set_blind(20)