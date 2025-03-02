# PyFlush Documentation
## Overview
`PyFlush` is a Python-based poker game module designed to simulate the mechanics of a Texas Hold'em poker game. It includes support for basic game rules, player and bot management, rounds, betting, and custom poker game rules. This module can be used as a foundation for creating a more complex poker game, integrating AI, or building a poker-related application.

## Features
- Texas Hold'em Rules: Core rules for poker gameplay including betting rounds, community cards, and hand evaluation.
- Players and Bots: The ability to add human players and AI-driven bots with customizable behavior.
- Betting System: Supports different betting rounds (pre-flop, flop, turn, river) with customizable limits.

## Installation
### Requirements:
- Python 3.x
- No external libraries are required (though you might want to install `numpy` for any future optimizations or improvements).
### Clone the Repository
```bash
git clone https://github.com/Shababad/pyflush.git
cd pyflush
```
## Usage:
To use the module, simply import the class and start a game (detailed methods documentation below):
```py
from pyflush import Game

# Create a game instance
game = Game()

# Adds a player to the game
game.add_player("Bob", 100000)

# Adds a bot to the game
game.add_bot("Tom", 100)

# Sets the blind amount of the game
game.set_blind(20)

# Start a round
game.start_round()
```
## Methods
`Game()`: the main class for running the game. Handles the deck, rounds, players, and game logic.

- `add_player(name, balance)`  
Adds player object to game player list

- `add_bot(name, balance, [{configurations}])`  
Adds bot object to game player list, `{configurations}` are optional due to bots default configurations

- `remove(name)`  
Removes player/bot from game player list with name

- `set_blind(amount)`  
Sets game blind amount, must be even and greater than 1

- `toggle_print()`  
Toggles print configuration process status