def main():
#Longest Collatz sequence
	sequence = {}
	largest = 1000000
	for n in range(1,largest):
		number = n
		if(n % 100000 == 0):
			print(n)

		counter = 0
		while n > 1:
			counter = counter + 1
			if n % 2 :
				n = 3*n + 1
			else:
				n = n/2

		sequence[counter] = number

	print(sequence[max(sequence.keys())])

	
if __name__ == "__main__": main()
