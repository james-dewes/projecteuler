def is_prime(number):
	for i in range(2,number):
		if number % i == 0:
			return False
		
	return True
	
total = 2
n = 1
while n < 2000000:
	if is_prime(n):
		total = total + n
	n+=1
	
print total
