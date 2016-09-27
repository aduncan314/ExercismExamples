#Andrew Duncan August 2016
#
#exercism practice exercise 'Hamming'

def distance(X, Y):
	'Checks if the sequences are the same length. If so, computes the Hamming distance between sequence \'X\' and sequence \'Y\'.'

	if len(X) != len(Y):
		return 'The Hamming distance is not well defined when the sequences have different lengths.'
	else:
		xList = list(X)
		yList = list(Y)
		dist = 0
		for i in range(len(xList)):
			if xList[i] != yList[i]:
				dist += 1

		return dist