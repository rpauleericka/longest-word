# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import string
import random


class Game:
    def __init__(self):
        self.grid = self.random_grid(9)

    @classmethod
    def random_grid(cls, grid_length):
        grid = []
        while len(grid) < grid_length:
            alphabet = string.ascii_uppercase  # alphabet majuscule
            # prendre une lettre aléatoirement
            lettre = alphabet[random.randint(0, len(alphabet) - 1)]
            grid.append(lettre)
        return grid

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy()  # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
