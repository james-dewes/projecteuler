#!/usr/bin/env python3
def is_palindrome(string)->bool:
	"""Test if a string is a palindrome.
	   
	   Args:
	   	string (str): any string.
		   
	   Returns:
	    (bool)  True if the string is a palindrome.
	   	
	"""
	return string == string[::-1]

def palindromic_number(n)->int:
	"""
	Find the largest palindromic number made with
	the product of n digit numbers.

	Args:
		n (int): The number of digits to search.
	
	Returns:
		(int): The largest palindromic number.

	"""
	n1 = int('9'*n)
	n2 = n1
	palindromes = []
	while n1 > 0:
		while n2 > 0:
			if is_palindrome(str(n1 * n2)):
				palindromes.append(n1 * n2)
				break
			n2-=1
		n2 = n1
		n1 -=1
	return max(palindromes)

if __name__=='__main__':
	print(palindromic_number(3))
