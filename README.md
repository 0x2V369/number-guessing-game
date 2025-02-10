
# Number Guessing Game

A simple interactive number guessing game built with Python. In this game, the computer selects a random number between 1 and 100, and the player must guess the number within a limited number of attempts. The game offers two difficulty levels:

- **Easy:** 10 attempts  
- **Hard:** 3 attempts

The program provides hints if your guess is too high or too low—and even distinguishes when your guess is "way too high" or "way too low". After each round, you have the option to play again.

---

## Features

- **Difficulty Levels:** Choose between Easy (10 attempts) and Hard (3 attempts).
- **User-Friendly Interface:** Clear instructions and hints guide you through the game.
- **Intelligent Feedback:** Get differentiated hints for "too high/low" and "way too high/low" guesses.
- **Replay Option:** Easily play multiple rounds without restarting the program.
- **Screen Clearing:** The screen is cleared between rounds for a fresh start.

---

## Requirements

- Python 3.x

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/0x2V369/number-guessing-game.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd number-guessing-game
   ```

---

## How to Run

Run the game using Python:

```bash
python number_guessing_game.py
```

If your system uses Python 3 as the default, you can also use:

```bash
python3 number_guessing_game.py
```

---

## How to Play

1. **Select a Difficulty:**  
   When prompted, type `easy` or `hard` to choose your difficulty level. This will determine the number of guesses you get (10 for easy, 3 for hard).

2. **Make Your Guesses:**  
   The computer selects a random number between 1 and 100. Enter your guesses when prompted. The game will tell you if your guess is too high or too low—and even whether it's "way too high" or "way too low" based on the difference.

3. **Winning or Losing:**  
   You win if you guess the correct number within the allowed attempts. If you run out of guesses, the game will reveal the correct number.

4. **Replay Option:**  
   After each round, you'll be asked if you'd like to play another round. Simply type `y` to continue or `n` to exit.

---

## Code Overview

The main Python script includes:

- **Difficulty Selection:** The `get_difficulty` function lets you choose between easy and hard modes.
- **Input Validation:** The `get_user_guess` function ensures that you enter a valid integer between 1 and 100.
- **Game Logic:** Compares your guess to the randomly chosen number and provides appropriate feedback.
- **Replay Mechanism:** The game runs in a loop, allowing you to play multiple rounds without restarting the program.
- **Screen Clearing:** The `clear_screen` function clears the terminal between rounds for a clean user interface.

---

## Contributing

Contributions are welcome! If you have suggestions or improvements, please feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

Developed by [0x2V](https://github.com/0x2V369)
```