#!/usr/bin/env python3
import math

def is_prime(number)->bool:
  """
  Checks if a number is prime by checking
  all values between 2 and it's square root.

  Args:
	number (int) any positive integer.
  
  Returns: 
	(bool) True if the number is prime, otherwise false.
    
  """
  for i in range(2,int(math.sqrt(number))):
    if number % i == 0:
      return False
    
  return True

def prime_factors(number)->int:
  """
  Finds the largest prime factor of a number.

  Args:
	number (int) any positive integer.
  
  Returns:
	(int) Largest prime factor of the number.
  
  """
  factor = 0
  for n in range(1,int(round(math.sqrt(number)))+1):
    if number % n == 0 and is_prime(n) and n > factor:
      factor = n
  return factor 
  
if __name__ == '__main__':
  print(prime_factors(600851475143))
  

