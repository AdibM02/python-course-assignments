"""Unit tests for the guessing game module."""

import unittest
from game import check_guess


class TestGuessingGame(unittest.TestCase):
    """Test cases for the check_guess function."""

    def test_correct_guess(self):
        """Test that a correct guess returns 'Found'."""
        target = 50
        guess = 50
        result = check_guess(guess, target)
        self.assertEqual(result, "Found")

    def test_too_low_guess(self):
        """Test that a guess too low returns 'Larger'."""
        target = 75
        guess = 50
        result = check_guess(guess, target)
        self.assertEqual(result, "Larger")

    def test_too_high_guess(self):
        """Test that a guess too high returns 'Smaller'."""
        target = 20
        guess = 30
        result = check_guess(guess, target)
        self.assertEqual(result, "Smaller")

    def test_near_miss_low(self):
        """Test a guess one below the target."""
        target = 15
        guess = 14
        result = check_guess(guess, target)
        self.assertEqual(result, "Larger")

    def test_near_miss_high(self):
        """Test a guess one above the target."""
        target = 15
        guess = 16
        result = check_guess(guess, target)
        self.assertEqual(result, "Smaller")


if __name__ == '__main__':
    unittest.main()
