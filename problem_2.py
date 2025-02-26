#!/usr/bin/env python3

def even_fibonacci_values(limit: int)->int:
	"""
	Returns the sum of even Fibonacci sequence numbers
	below the limit.

	Args: 
		limit (int): Non negative integer.
	"""
	f1 = 0 
	f2 = 1
	total = 0

	while f2 < limit:
		if f2 % 2 == 0:
			total += f2
		f1, f2 = f2, (f1 + f2)
	return total
	

if __name__ == '__main__':
	print(even_fibonacci_values(4000000))

