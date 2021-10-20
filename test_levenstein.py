import csv
import pytest
from edit_distance import calc_lev


def test_same_word():
	assert calc_lev("this", "this") == 0

def test_w1_shorter_than_w2():
	assert calc_lev("the", "that is correct") == 13

def test_w1_larger_than_w2():
	assert calc_lev("that is correct", "the") == 13

def test_w1_larger_than_w2_v2():
	assert calc_lev("the", "that") == 2

def test_same_length():
	assert calc_lev("this", "that") == 2

def test_examples():
	with open('data/examples.csv', newline='') as csvfile:
		examples = csv.reader(csvfile)
		for row in examples:
			assert calc_lev(row[0], row[1]) == int(row[2])