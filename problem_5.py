def main():
	counter = 20
	check = False
	while not check:
		notch = 0	
		for i in range(1,21):
			#print str(counter) + ' ' + str(i) + ' ' +  str( not counter % i)
			if not counter % i:
				notch = notch + 1
			
		#check = True
		if notch == 20:
			check = True
		else:
			counter = counter + 20
	
	print counter 
	
		

if __name__=='__main__':main()
