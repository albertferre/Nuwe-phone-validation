"""This module contains the unit tests for the phone validator."""
import pytest

from src.phone_validator import phone_validator


test_dict = {
    "task_1": ("972-35-56-57", True),
    "task_2": ("(972) 35 56 57", True),
    "task_3": ("972355657", True),
    "task_4": ("972 35 46 97", True),
    "task_5": ("123**&!!asdf#", False),
    "task_6": ("55555555", False),
    "task_7": ("(6054756961)", False),
    "task_8": ("-34 972-35-56-57", False),
    "task_9": ("34 972 35 46 97", True),
}

@pytest.mark.parametrize("phone_number, expected", test_dict.values())
def test_phone_number(phone_number, expected):
    """This method tests the phone number validator."""

    assert phone_validator(phone_number) == expected
