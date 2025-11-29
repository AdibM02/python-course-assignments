# Day 05: Guessing Game with Unit Tests

A Python number guessing game featuring clean code architecture with separated business logic and comprehensive unit tests.

## Overview

This project demonstrates:
- ✓ Clean separation of concerns (game logic vs user interaction)
- ✓ Testable functions with pure logic
- ✓ Comprehensive unit testing with `unittest`
- ✓ Error handling and input validation
- ✓ Interactive command-line game

## Project Structure

```
day05/
├── game.py              # Core game logic and main game loop
├── test_main.py         # Comprehensive unit test suite
├── Guess_game.py        # Original simple version (reference)
└── README.md           # This file
```

## How It Works

### Game Logic

The game operates on these simple rules:

1. **Target**: Computer generates a random number between 1 and 100
2. **Guessing**: Player enters guesses
3. **Feedback**: Program returns:
   - `"Found"` — Correct guess!
   - `"Larger"` — Target is larger than guess
   - `"Smaller"` — Target is smaller than guess
4. **Winning**: Player wins when they find the number, counter shows attempts

### Architecture

**game.py** contains two functions:

- **`check_guess(guess, target_number)`** — Pure logic function
  - Takes a guess and target number
  - Returns "Found", "Larger", or "Smaller"
  - No I/O, fully testable

- **`run_game()`** — Interactive game loop
  - Generates random target number
  - Handles user input
  - Provides feedback using `check_guess()`
  - Counts and displays attempts

## Installation

### Requirements

- **Python**: 3.7 or higher
- **Libraries**: Only standard library (no external dependencies)

### No Installation Needed

All functionality uses Python's standard library:
- `random` — Generate random numbers
- `unittest` — Test framework (built-in)

Simply clone/download and run!

## Usage

### Run the Game

```bash
python game.py
```

**Example Game Session:**
```
Welcome to the Guessing Game!
Your guess is? 50
Larger
Your guess is? 75
Smaller
Your guess is? 60
Found
You found the number in 3 moves.
```

### Run Tests

```bash
python test_main.py
```

**Test Output:**
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

Or with more verbose output:

```bash
python -m unittest test_main.py -v
```

## File Descriptions

### game.py

**Purpose**: Core game module with business logic

```python
def check_guess(guess, target_number):
    """Compare guess to target. Returns 'Found', 'Larger', or 'Smaller'."""
    if guess == target_number:
        return "Found"
    elif guess < target_number:
        return "Larger"
    else:
        return "Smaller"

def run_game():
    """Main game loop with user interaction."""
    # Generate random number
    # Accept guesses
    # Provide feedback using check_guess()
```

**Key Features:**
- `check_guess()` is pure logic (testable, no I/O)
- `run_game()` handles all user interaction
- Input validation for non-numeric entries
- Move counter tracks attempts

### test_main.py

**Purpose**: Unit tests for `check_guess()` function

**Test Cases (5 total):**

1. **`test_correct_guess`** — Verifies correct guess returns "Found"
   - Guess: 50, Target: 50 → "Found" ✓

2. **`test_too_low_guess`** — Verifies low guess returns "Larger"
   - Guess: 50, Target: 75 → "Larger" ✓

3. **`test_too_high_guess`** — Verifies high guess returns "Smaller"
   - Guess: 30, Target: 20 → "Smaller" ✓

4. **`test_near_miss_low`** — Verifies boundary at -1
   - Guess: 14, Target: 15 → "Larger" ✓

5. **`test_near_miss_high`** — Verifies boundary at +1
   - Guess: 16, Target: 15 → "Smaller" ✓

All tests verify core comparison logic without random number generation or user input.

### Guess_game.py

**Purpose**: Original simple version (for reference)

Simple, linear script without separation of logic. Shows the "before" state of refactoring.

## Development Workflow

### Running Tests After Changes

If you modify `check_guess()`:

```bash
python test_main.py
```

All 5 tests should pass. If a test fails, your changes broke the contract.

### Adding New Tests

To add a test, create a new method in `TestGuessingGame`:

```python
def test_example_case(self):
    """Describe what this tests."""
    target = 50
    guess = 40
    result = check_guess(guess, target)
    self.assertEqual(result, "Larger")
```

Then run:
```bash
python test_main.py
```

## Code Quality

- ✓ Type hints in docstrings
- ✓ Clear docstrings for all functions
- ✓ Comprehensive unit tests
- ✓ Input validation with error messages
- ✓ Separated concerns (logic vs I/O)
- ✓ DRY principle (no code duplication)

## Troubleshooting

### "ModuleNotFoundError: No module named 'game'"

**Cause**: Running test from wrong directory

**Solution**: Make sure you're in the `day05` folder
```bash
cd day05
python test_main.py
```

### "ValueError: invalid literal for int()"

**Cause**: Entering non-numeric input

**Solution**: Game catches this and asks for a number. Just enter an integer.

### Tests fail

**Cause**: `check_guess()` logic may be modified

**Solution**: Check that function returns correct values:
- Equal → "Found"
- Guess < Target → "Larger"
- Guess > Target → "Smaller"

## Learning Points

This project demonstrates:

1. **Testable Functions** — Pure logic separated from I/O
2. **Unit Testing** — How to test without user interaction
3. **Error Handling** — Graceful handling of invalid input
4. **Code Organization** — Functions with single responsibility
5. **Documentation** — Clear docstrings and comments

## Next Steps

To extend this project:

- [ ] Add difficulty levels (1-50, 1-1000, etc.)
- [ ] Track best scores in a file
- [ ] Implement AI player that learns
- [ ] Add Tkinter GUI version
- [ ] Support multiplayer mode
- [ ] Export statistics to CSV

## References

- [Python random module](https://docs.python.org/3/library/random.html)
- [unittest framework](https://docs.python.org/3/library/unittest.html)
- [Python docstring conventions](https://www.python.org/dev/peps/pep-0257/)

---

**Difficulty**: Beginner  
**Topics**: Functions, Unit Testing, Input Validation, Game Logic  
**Python Version**: 3.7+  
**External Dependencies**: None
