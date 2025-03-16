#!/usr/bin/env python3

def is_prime(number: int)-> bool:
	"""
	Returns True if the number is prime
	"""
	result = True
	for i in range(2,number):
		if number % i == 0:
			result = False
			break
	return result

def main():
	total = 2
	n = 1
	while n < 2000000:
		if is_prime(n):
			total = total + n
		n+=1
		
	print(total)

if __name__ == '__main__':	
	main()
