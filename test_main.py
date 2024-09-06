"""Test file for main.py"""
import pytest
import string

from main import calculate_score, assign_rack


@pytest.fixture
def get_bag():
    return {"E": 12, "A": 9, "I": 9, "O": 8, "N": 6, "R": 6, "T": 6, "L": 4, "S": 4, "U": 4, "D": 4, "G": 3, "B": 2,
            "C": 2, "M": 2, "P": 2, "F": 2, "H": 2, "V": 2, "W": 2, "Y": 2, "K": 1, "J": 1, "X": 1, "Q": 1, "Z": 1}


@pytest.fixture
def get_half_bag():
    return {"E": 2, "A": 2, "I": 2, "O": 2, "N": 2, "R": 2, "T": 1}


def test_calculate_score_guardian():
    assert calculate_score("GUARDIAN") == 10


def test_calculate_score_a():
    assert calculate_score("A") == 1


def test_calculate_score_invalid():
    assert calculate_score("aaaaa") == 5


def test_calculate_score_invalid_empty_string():
    assert calculate_score("") == 0


def test_assign_rack_islist(get_bag):
    players_rack = assign_rack(get_bag)
    assert isinstance(players_rack, list)


def test_assign_rack_is_correct_length(get_bag):
    players_rack = assign_rack(get_bag)
    assert len(players_rack) == 7


def test_assign_rack_are_letters(get_bag):
    players_rack = assign_rack(get_bag)

    alphabet = string.ascii_letters

    for l in players_rack:
        assert l in alphabet


def test_assign_rack_takes_away_from_bag(get_half_bag):

    players_rack = assign_rack(get_bag)

    for letter in players_rack:

    pass
