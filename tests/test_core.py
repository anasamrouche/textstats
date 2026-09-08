import pytest

import textstats
from textstats.core import *


def test_longest_word_rejects_empty():
    with pytest.raises(ValueError):
        longest_word("")


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", 0),
        ("one", 1),
        ("the end.", 2),
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected


def test_left_priority():
    assert longest_word("aaaa bbbb") == "aaaa"
