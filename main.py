"""Script for technical Interview"""

import random

LETTER_SCORES = {"E": 1, "A": 1, "I": 1, "O": 1,
                 "N": 1, "R": 1, "T": 1, "L": 1, "S": 1, "U": 1, "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3,
                 "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10}

TILES_DISTRIBUTION = {"E": 12, "A": 9, "I": 9, "O": 8, "N": 6, "R": 6, "T": 6, "L": 4, "S": 4, "U": 4, "D": 4, "G": 3, "B": 2,
                      "C": 2, "M": 2, "P": 2, "F": 2, "H": 2, "V": 2, "W": 2, "Y": 2, "K": 1, "J": 1, "X": 1, "Q": 1, "Z": 1}


def calculate_score(name_to_be_scored: str) -> int:

    score = 0

    name_to_be_scored = name_to_be_scored.upper()

    for letter in name_to_be_scored:
        score += LETTER_SCORES[letter]

    return score


def assign_rack(bag: dict) -> list:

    players_rack = []

    for x in range(0, 7):
        random_letter = random.choice(list(LETTER_SCORES.keys()))

        players_rack.append(random_letter)

    return players_rack


if __name__ == "__main__":

    bag = {"E": 12, "A": 9, "I": 9, "O": 8, "N": 6, "R": 6, "T": 6, "L": 4, "S": 4, "U": 4, "D": 4, "G": 3, "B": 2,
           "C": 2, "M": 2, "P": 2, "F": 2, "H": 2, "V": 2, "W": 2, "Y": 2, "K": 1, "J": 1, "X": 1, "Q": 1, "Z": 1}

    assign_rack(bag)
