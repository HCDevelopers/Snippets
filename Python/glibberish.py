# Author: Deque
#
# Have you ever wondered how spam bots create their spam messages?
#
# This is one possibility: They use Markov-Chains.
# Given one word as input, a Markov Chain will put out another word. The output word is defined by a certain probability. It might be word A with probability of 20% or word B with probability of 80%. This word output is again used as input to get the next word, thus forming a chain of words.
#
# This is my Glibberish-O-Mat that uses this principle. It takes as input a text file (you can use one from Project Gutenberg to get a reasonably long text: http://www.gutenberg.org/ ), analyses the probabilities of the words following other words and then produces a text with the given amount of words using these probabilities.

import sys
import operator
import random

markov_chain = {}

#adds the specified word to the markov chain
def add_to_chain(lastword, word):
	if not markov_chain.has_key(lastword):
		markov_chain[lastword] = {}
	if not markov_chain[lastword].has_key(word):
		markov_chain[lastword][word] = 1
	else:
		markov_chain[lastword][word] += 1

#builds up the markov chain using the specified file
def build_chain_from(filename):
	file = open(filename, 'r')
	lastword = "first"
	for word in words(file):
		add_to_chain(lastword, word)
		lastword = word

#iterates over words in a file
def words(file):
    for line in file:
        for word in line.split():
            yield word

#returns a random word with the probability based on the given lastword
def get_rand_word(lastword):
	chain = markov_chain[lastword]
	total = sum(chain.itervalues())
	randval = random.randint(1, total)
	for key in chain:
		randval -= chain[key]
		if randval <= 0:
			return key
	return ""

#generates a text with the given amount of words
def generate_text(amount):
	lastword = "first"
	word = get_rand_word(lastword)
	for i in range(0, amount):
		word = word + " " + get_rand_word(lastword)
	return word

def print_title():
    print('''
 _____  _  _  _      _                  _       _
|  __ \| |(_)| |    | |                (_)     | |
| |  \/| | _ | |__  | |__    ___  _ __  _  ___ | |__
| | __ | || || '_ \ | '_ \  / _ \| '__|| |/ __|| '_ \
| |_\ \| || || |_) || |_) ||  __/| |   | |\__ \| | | |
 \____/|_||_||_.__/ |_.__/  \___||_|   |_||___/|_| |_|
          _____         ___  ___        _
         |  _  |        |  \/  |       | |
  ______ | | | | ______ | .  . |  __ _ | |_
 |______|| | | ||______|| |\/| | / _` || __|
         \ \_/ /        | |  | || (_| || |_
          \___/         \_|  |_/ \__,_| \__|
''')

def main():
	print_title()
	if len(sys.argv) != 3 or not sys.argv[2].isdigit():
		print "usage: markov.py <filename> <wordstogenerate>"
		return
	filename = sys.argv[1]
	amount = int(sys.argv[2])

	build_chain_from(filename)

	print generate_text(amount)
	print

main()
