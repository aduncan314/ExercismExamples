#Andrew Duncan August 2016
#
#exercism practice exercise 'Difference of Squares'

def square_of_sum(N):
	N = float(N)
	return int(((N+1) * (N/2))**2)


def sum_of_squares(N):
	N = float(N)
	return int((2*(N**3) + 3*N*N + N)/6)


def difference(N):
	return square_of_sum(N) - sum_of_squares(N)