#largets palindromic number made with 3 digits

def is_palindrome(n):
	return str(n) == str(n)[::-1]

def palindromic_number(places):
	n1 = int	('9'*places)
	n2 = n1
	palindromes = []
	while n1 != 1:
		while n2 != 1:
			if is_palindrome(n1 * n2):
				palindromes.append(n1 * n2)

			n2-=1
			
		n2 = n1
		n1 -=1
	return max(palindromes)


print palindromic_number(3)
