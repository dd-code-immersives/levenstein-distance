import csv
from pprint import pprint

cache = {}
def run_examples():
	with open('data/wordlist_example.csv', newline='') as csvfile:
		examples = csv.reader(csvfile)
		for row in examples:

			w1 = row[0]
			w2 = row[1]
			dist = None
			example_key = "||".join([w1, w2])
			if example_key in cache:
				print(f"cached {example_key} =  {cache[example_key]}")
			else:		
				dist = calc_lev(w1, w2)
				cache[example_key] = dist
		pprint(cache)

def calc_lev(word1, word2):

	""" 
	Calculate the levenstein distance between two words
	"""

	counter = 0

	edits = {'insert or del': [], 
			 'replace':[]
			}

	# case 1: words are the same (distance of 0)
	if word1 == word2:
		return counter

	# case 2: the words have the same length 
	if len(word1) == len(word2):
		for idx, lett in enumerate(word1):
			if lett != word2[idx]:
				counter += 1
				edits['replace'].append(f"replace {lett} with {word2[idx]}")
		return counter

	# case 3: lengths are not the same
	# "kitten", 
	# "sitting" 

	if len(word2) > len(word1):
		short_wd = word1 
		long_wd = word2
	elif len(word1) > len(word2):
		short_wd = word2 
		long_wd = word1


	for idx, lett in enumerate(long_wd):
		if idx < len(short_wd):
			if lett != short_wd[idx]:
				counter += 1
				edits['replace'].append(f"replace {lett} with {short_wd[idx]}")

		elif idx >= len(short_wd):
			counter += 1
			edits['insert or del'].append(f"insert or delete {lett}")

	#pprint(edits)
	return counter


if __name__ == '__main__':
	# print(calc_lev("kitten", "sitten"))
	# print(calc_lev("sitten", "sittin"))
	# print(calc_lev("sittin", "sitting"))
	# print(calc_lev("kitten", "sitting"))
	# print(calc_lev("kitten", "kitten"))
	run_examples()