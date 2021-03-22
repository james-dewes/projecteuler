def is_prime(number):
	for i in range(2,number):
		if number % i == 0:
			return False
		
	return True

number = 1
prime = 0
prime_count = 0
while prime_count < 10001:
	number+=1
	if is_prime(number):
		prime = number
		prime_count+=1
		print str(prime_count) + ': ' + str(prime)
		

print prime
	
