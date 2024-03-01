# Python Pong Game

The `PythonPong` class is a Python implementation of the classic Pong game. It offers various features and modes of play, including player vs player and player vs CPU modes, score tracking, ball bouncing and collision detection, AI opponent in CPU mode, and a responsive design using Turtle graphics.

## Features

- **Player vs Player mode:** Play against another player using keyboard controls.
- **Player vs CPU mode:** Play against a computer-controlled opponent with AI.
- **Score tracking:** Keep track of player scores and declare a winner.
- **Ball bouncing and collision detection:** The ball bounces off walls and paddles accurately.
- **AI opponent in Player vs CPU mode:** A computer-controlled opponent adjusts its paddle position based on the ball's movement.
- **Responsive design using Turtle graphics:** The game features a colorful and visually appealing interface.

## Usage

To use the Python Pong game:

1. Run the `python python_pong.py` command to start the game.
2. Once the game window opens, you'll see three buttons:
   - **Player VS Player:** Click this button to start a game where two players can compete against each other. Player 1 controls the red paddle with the 'W' and 'S' keys to move up and down, respectively, while Player 2 controls the blue paddle with the 'Up' and 'Down' arrow keys.
   - **Player VS CPU:** Click this button to start a game against the computer. Player 1 controls the red paddle with the 'W' and 'S' keys as before, while the CPU controls the blue paddle. The CPU uses AI to move its paddle and try to intercept the ball.
   - **Exit:** Click this button to exit the application.
4. The game keeps track of the score, and the first player to reach the maximum score wins the game.
5. Enjoy playing Python Pong!

## Requirements

- Python 3.x
- Tkinter library (usually included with Python installations)
- Turtle graphics library (included in the standard Python distribution)

## Example

```python
import tkinter as tk
from PythonPong import PythonPong

root = tk.Tk()
root.title("Python Pong")

pong_game = PythonPong(root)

# Add buttons and other GUI elements as needed

root.mainloop()
