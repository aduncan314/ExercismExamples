#Andrew Duncan August 2016
#
#exercism practice exercise Word Count

import re

class word_count(object):
	"""
	Count the occurence of each distinct word.
	
	Any sequence of characters that are unicode alphanumeric and separated by any non-alphanumeric character except for an underscore ('_') is considered a word
	"""

#	Creates dictionary 'counted_words' with KEY = word and VALUE = number of occurrences
	def __init__(self, phrase):
		phrase = phrase.lower().decode('utf-8')
		phrase = re.sub('[\W|^\\\\]|_',' ',phrase, flags = re.UNICODE)

		self._wordList = phrase.split()
		self._wordSet = set(self._wordList)
		self.counted_words = {}
		
		for word in self._wordSet:
			self.counted_words[word] = self.count(word)


	def __repr__(self):
		return str(self.counted_words)


	def __eq__(self, other):
		return self.counted_words == other


	def values(self):
		return self.counted_words.values()


	def count(self, newWord):
		count = 0
		for item in self._wordList:
			if item == newWord:
				count += 1
		return count