import csv
import pytest
from levenstein import calc_lev


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
	with open('data/wordlist.csv', newline='') as csvfile:
		examples = csv.reader(csvfile)
		for row in examples:
			w1 = row[0]
			w2 = row[1]
			dist = int(row[2])
			error_msg = f"distance between {w1}/{w2} is not {dist}"
			assert calc_lev(row[0], row[1]) == int(row[2]), error_msg