#!/usr/bin/env python3

def sum_sqare_differnce(number: int)->int:
  """
  Returns differnce beween the sum of the natural numbers
  squared up to and including the number and the sum of 
  the square of the natural numbers up to and including 
  the number.

  Args: 
    number (int): Non negative integer.
 
  Returns:
  (int): Calcuated difference.
  """
  sum_of_squares = sum([num**2 for num in range(1, number+1)])
  square_of_sum = sum(range(1, number+1))**2
  return square_of_sum - sum_of_squares
  

if __name__ == '__main__':
  print(sum_sqare_differnce(100))

