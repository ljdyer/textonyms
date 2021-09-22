#!/usr/bin/env python3
"""tests for textonyms.py"""

import os
import re
from subprocess import getstatusoutput
from textonyms import *

prg ='textonyms.py'

num_letter_pairs = [("2", "b"), ("9", "z"), ("4", "h")]
num_word_pairs = [("43556", "hello"), ("666539", "monkey"), ("8398", "text")]

# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_num_to_words():
    """test pairs"""
    for num, word in num_word_pairs:
        assert word in num_to_words(num)


# --------------------------------------------------
def test_letter_to_num():
    """test pairs"""
    for num, letter in num_letter_pairs:
        assert num == letter_to_num(letter)


# --------------------------------------------------
def test_word_to_num():
    """test pairs"""
    for num, word in num_word_pairs:
        assert word_to_num(word) == num