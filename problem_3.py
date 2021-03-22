def is_prime(number):
	for i in range(2,number):
		if number % i == 0:
			return False
		
	return True

def prime_factors(number):
	import math
	factor = 0
	for n in range(1,int(round(math.sqrt(number)))+1):
		if number % n == 0 and is_prime(n) and n > factor	:
			factor = n
		
		
	return factor 
	
print prime_factors(600851475143)
				
			
	

