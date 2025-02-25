#!/usr/bin/env python3

def sum_multiples_of_3_or_5(limit: int)->int:
	"""
	Returns the sum of multiples of 3 or 5 below the limit.

	Args: 
		limit (int): Non negative integer.
	"""
	return sum([i for i in range(limit-1) if i % 3 == 0 or i % 5 == 0])



if __name__ == '__main__':
	print(sum_multiples_of_3_or_5(1000))
