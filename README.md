# Tic-Tac-Toe Game in Python with Pygame

## Description
This is a simple implementation of the Tic-Tac-Toe game and ultimate tic tac toe game in Python using the Pygame library for the graphical interface. The computer opponent uses a neural network for decision-making.

## Prerequisites
- Python 3.x
- Pygame (install with `pip install pygame`)
- TensorFlow (install with `pip install tensorflow`)

## How to Play
1. Run the `launcher.py` file to start the game.
2. Chose if you want to play tic tac toe or ultimate tic tac toe
3. Click on an empty cell to place your symbol (X or O).
4. The game will automatically alternate between player and computer turns.
5. The game will display the result (win, draw), waiting for a click to restart after the game ends.

## Features
- Simple graphical interface with Pygame.
- Automatic alternating between player and computer turns.
- Implementation of a neural network for decision-making by the computer.
- Basic Minimax algorithm for the computer's strategy for the ultimate tic tac toe

## Project Structure
- `tic_tac_toe.py`: The main file containing the classic tic tac toe game class.
- `launcher.py` : The launcher to chose between tic tac toe and ultimate tic tac toe.
- `ultimate_tic_tac_toe.py` : The main file containing the ultimate tic tac toe game class.
- `croix.png`: Image of the X symbol.
- `cercle.png`: Image of the O symbol.
- `OIP.jpeg`: Background image for the classic game window.
- `ultimate-tic-tac-toe.webp`: Background image for the ultimate game window.
- `barre_hori.png` `barre_verti.png` `barre_diag_droite.png` and `barre_diag_gauche.png`: Line for the win.


## Notes
This project is intended for my personal purposes to help me understand the implementation of Pygame, the Minimax algorithm, and neural networks. Feel free to enhance and customize it according to your needs.
