# Pong Game
A classic Pong game implemented using Python's `turtle` module. This is a two-player game where each player controls a paddle, and the objective is to score points by making the opponent miss the ball.

## Features
- Two-player controls: Players can move their paddles up and down using keyboard keys.
- Scoring system: The game ends when one player scores 11 points more than the opponent.
- Dynamic ball speed: The ball speeds up with each paddle hit to increase the challenge.
- Customizable paddles and ball mechanics: Includes basic collision detection for walls and paddles.
  
## Getting Started
### Prerequisites
Python 3.8 or higher must be installed on your machine. 

To check if Python is installed and verify the version, run the following command in your terminal or command prompt:

```bash
python --version
```

If the installed version is below 3.8, please update Python before proceeding.

### Installation
1. Clone this repository or download the source code.
```bash
git clone https://github.com/dimitra-savvani/Pong-Game.git
```
2. Navigate to the project directory:
```bash
cd Pong-Game
```
3. Run the game:
```bash
python main.py
```

### Controls
- Right paddle (controlled by player 1):
  - Move up: `Up Arrow`
  - Move down: `Down Arrow`
- Left paddle (controlled by player 2):
  - Move up: `W`
  - Move down: `S`
  - 
## How to Play
1. Launch the game by running `main.py`.
2. Each player controls a paddle, aiming to prevent the ball from passing their side.
3. The ball will bounce off the top and bottom walls and the paddles.
4. A player scores if the ball passes the other player's paddle.
5. The game ends when one player scores 11 points.
6. The winner is declared at the end, along with the score difference.
   
## Code Structure
- `main.py`: Contains the game loop and initializes all game elements.
- `ball.py`: Defines the behavior of the ball, including movement, collision detection, and resetting the ball.
- `paddle.py`: Defines the behavior of paddles, including movement controls.
- `score.py`: Manages the score and displays it on the screen.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
