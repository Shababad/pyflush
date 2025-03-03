# Methods
## `Game()`
The main class for running the game. Handles the deck, rounds, players, and game logic.

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

## `Deck()`
The class for the playing deck of the game.

- `draw()`  
Draws a card from the deck

- `shuffle()`  
Shuffles the deck

- `collect()`  
Collect every card that has been used
